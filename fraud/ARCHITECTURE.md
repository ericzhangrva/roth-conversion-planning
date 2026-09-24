# Enterprise Credit Card Fraud Detection & Prevention Ecosystem Architecture

## 1. Executive Architecture Overview

This architecture is built for high-throughput, sub-50ms real-time card authorization decisioning, dual-path outcome routing (Synchronous Decline vs. Asynchronous Case Management), account restriction lifecycles, and a dynamic 30+ tool customer re-authentication matrix.

```mermaid
flowchart TD
    %% Styling
    classDef sync fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef async fill:#0f172a,stroke:#a855f7,stroke-width:2px,color:#f8fafc;
    classDef store fill:#1e1e2e,stroke:#f59e0b,stroke-width:2px,color:#f8fafc;
    classDef decision fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#f8fafc;
    classDef action fill:#701a75,stroke:#ec4899,stroke-width:2px,color:#f8fafc;

    subgraph ChannelSync ["1. Real-Time Synchronous Auth Flow (Budget < 50ms)"]
        POS[Payment Terminal / E-Comm] -->|ISO 8583 / REST| PaymentSwitch[Core Payment Switch]
        PaymentSwitch -->|Auth Request Payload| FraudGateway[Fraud Orchestration Gateway]
        
        FraudGateway -->|1. Fetch Features < 5ms| FeatureFactory[(Online Feature Store\nRedis / Aerospike)]:::store
        FraudGateway -->|2. Score Payload < 10ms| MLInference[ML Model Inference Engine\nXGBoost / ONNX]:::decision
        FraudGateway -->|3. Evaluate Policy < 3ms| RuleEngine[Decision & Policy Rule Engine]:::decision
        
        RuleEngine -->|Sync Decision| FraudGateway
        FraudGateway -->|Approve / Decline / Step-Up| PaymentSwitch
        PaymentSwitch -->|Auth Response| POS
    end

    subgraph EventStream ["2. Asynchronous Event Stream (Decoupled Kafka Backbone)"]
        FraudGateway -.->|Emit Enriched Event| KafkaBus{Kafka Event Backbone}:::async
    end

    subgraph AsyncActions ["3. Asynchronous Actioning & Case Pipeline"]
        KafkaBus -->|High Risk / Suspect| CaseEngine[Case Management & Alert Engine]:::action
        KafkaBus -->|Trigger Alerts| NotifEngine[Omnichannel Notification Engine]:::action
        KafkaBus -->|Restriction Events| AccountControl[Account Restriction Engine]:::action
        KafkaBus -->|CDC / Feature Aggregations| FlinkPipeline[Apache Flink Stream Processor]:::async
        FlinkPipeline -->|Write Sliding Windows| FeatureFactory
        FlinkPipeline -->|Write Raw / Curated| DataLake[(Offline Lakehouse\nIceberg / Snowflake)]:::store
    end

    subgraph ReAuthFlow ["4. Inbound Customer Contact & Dynamic Re-Auth"]
        Customer[Customer: Call / App / SMS] --> InboundGateway[Inbound Communication Gateway]
        InboundGateway --> AuthMatrix[Dynamic Step-Up Auth Engine]:::decision
        AuthMatrix --> ToolCatalog[30+ Verification Tools]
        ToolCatalog --> InboundGateway
        InboundGateway -->|Auth Success / Confirmed Fraud| AccountControl
    end
```

---

## 2. Real-Time Authorization & Feature Factory Architecture

### Synchronous vs. Asynchronous Boundary
* **Synchronous Path (In-Line, SLA < 50ms p99):**
  * Gateway receives transaction payload (PAN token, Amount, MCC, Merchant ID, Terminal Type, Geo/IP, 3DS flags).
  * Gateway queries the **Online Feature Factory** (low-latency key-value cache).
  * Gateway passes enriched vectors to **ML Inference Service** (LightGBM/XGBoost via ONNX).
  * Model score + raw attributes fed to the **Decision & Policy Rule Engine**.
  * Immediate return: `APPROVE`, `DECLINE`, or `CHALLENGE_3DS`.
* **Asynchronous Path (Off-Line, Event-Driven via Kafka):**
  * Full transaction event, feature snapshot, model scores, and rule match metadata are published to Kafka.
  * Downstream consumers handle **Case Creation**, **Notification Dispatch**, **Account State Locking**, and **Feature Store Updating**.

```mermaid
sequenceDiagram
    autonumber
    actor Terminal as Payment Switch / POS
    participant Gateway as Fraud Gateway
    participant FF as Feature Factory (Redis Cluster)
    participant ML as ML Inference (ONNX / Triton)
    participant Rules as Policy Rule Engine
    participant Kafka as Kafka Event Stream

    Terminal->>+Gateway: POST /v1/authorizations/evaluate (Auth Payload)
    par Feature Fetch & State Check
        Gateway->>+FF: Multi-Key Get (Entity: Card, Merchant, Device)
        FF-->>-Gateway: Velocity, Historical Baseline, Geodistance (3ms)
    end
    Gateway->>+ML: POST /v1/score (Merged Vector)
    ML-->>-Gateway: Fraud Probability Score (e.g. 0.87) (6ms)
    Gateway->>+Rules: Evaluate(Payload, Features, Score)
    Note over Rules: Evaluates Hard Rules,<br/>Score Cutoffs & Velocity
    Rules-->>-Gateway: Decision: DECLINE, Trigger: CASE_REQUIRED (2ms)
    Gateway-->>Terminal: Synchronous Response: DECLINE (Total: 15-25ms)
    Gateway--)Kafka: Publish Event: `auth.evaluated` (Async)
```

---

## 3. Dual-Decision Matrix (Decline vs. Case)

Every authorization undergoes dual-state evaluation:

| Quadrant | Model Score | Rule Trigger | Action to Terminal | Action to Operations / Customer |
| :--- | :--- | :--- | :--- | :--- |
| **Q1: Clean / Low Risk** | Low (< 0.20) | No rules fired | **APPROVE** | None. Standard ledger clearing. |
| **Q2: Soft Suspect** | Moderate (0.20 - 0.70) | First-time overseas / High Velocity | **APPROVE / STEP-UP** | **CASE GENERATED + 2-Way SMS Notification**. |
| **Q3: High-Risk Alert** | High (0.70 - 0.90) | Multiple Card-Not-Present spikes | **DECLINE** | **CASE GENERATED + Soft Restriction + Push/SMS Alert**. |
| **Q4: Critical / Confirmed Fraud**| Very High (> 0.90)| Stolen List / Impossible Travel Velocity | **DECLINE** | **HARD RESTRICTION (Card Freeze) + Urgent Case + Immediate Call/SMS**. |

```mermaid
flowchart LR
    Score[ML Risk Score] & Rules[Rule Engine Policy] --> Matrix{Dual-Decision Evaluator}
    
    Matrix -->|Authorization Outcome| AuthChoice[Terminal Response]
    AuthChoice --> Appr[APPROVE]
    AuthChoice --> Dec[DECLINE]
    AuthChoice --> Chlg[3DS CHALLENGE]

    Matrix -->|Operational Outcome| CaseChoice[Back-Office & Customer]
    CaseChoice --> NoCase[No Case / Silent Log]
    CaseChoice --> AlertQueue[Investigator Case Queue]
    CaseChoice --> AutoNotif[Automated Customer SMS / Push]
    CaseChoice --> Restrict[Soft / Hard Card Restriction]
```

---

## 4. Infrastructure Sizing for 100 TPS (with 3x Peak Sizing = 300 TPS)

### Traffic & Latency SLA Specs
* **Nominal Throughput**: 100 Transactions Per Second (~8.64 Million/day).
* **Peak Design Capacity (3x Headroom)**: 300 TPS.
* **Latency Budget (P99)**: **< 40ms** inside the fraud ecosystem.

```
+-------------------------------------------------------------------------+
| TOTAL FRAUD SERVICE LATENCY BUDGET (40ms P99)                           |
+-------------------+-------------------+-------------------+-------------+
| Gateway / Network | Feature Store MGet| Model Inference   | Rule Engine |
| 3 - 5 ms          | 3 - 6 ms          | 5 - 10 ms         | 2 - 4 ms    |
+-------------------+-------------------+-------------------+-------------+
```

### Component-by-Component Infrastructure Sizing Table

| Tier | Component | Sizing & Spec | Redundancy / HA | Projected Utilization @ 300 TPS |
| :--- | :--- | :--- | :--- | :--- |
| **Ingress** | API Gateway / Envoy Proxy | 2x `c6i.large` (2 vCPU, 4GB RAM) | Multi-AZ (Active-Active) | CPU < 15% |
| **Orchestration** | Fraud Gateway Microservice (Go / Rust / Java Quarkus) | 3x `c6i.xlarge` (4 vCPU, 8GB RAM) | Multi-AZ with HPA (Auto-scale) | CPU < 25%, P99 Latency ~2ms |
| **Online Feature Store** | Redis Cluster / Aerospike | 3 Primary + 3 Replica Shards (`r6g.large`, 13GB RAM each) | Multi-AZ, In-Memory Persistence | IOPS < 5%, Cache Hit > 99.8% |
| **ML Inference Service** | ONNX Runtime / Triton Inference Server | 3x `c6i.2xlarge` (8 vCPU, 16GB RAM) | CPU thread pooling (No GPU needed for tabular models) | P99 < 8ms |
| **Rule Engine** | Embedded Drools / Custom JSON-Logic Engine | In-process or 2x `c6i.xlarge` | Embedded sidecar in Gateway | P99 < 2ms |
| **Message Streaming**| Apache Kafka (AWS MSK / Confluent) | 3 Brokers (`m5.large`, 2 vCPU, 8GB RAM, 500GB gp3) | 3-AZ, Replication Factor = 3 | Throughput ~5MB/sec (Minimal load)|
| **Stream Processing**| Apache Flink / Spark Streaming | 2 JobManagers + 4 TaskManagers (`c6i.xlarge`) | RocksDB State Store checkpointing to S3 | Continuous sliding aggregation |

---

## 5. Account Actioning & Restriction State Machine

When risk is detected, the ecosystem issues both communications and dynamic restrictions:

```mermaid
stateDiagram-v2
    [*] --> Active_Unrestricted: Normal State

    Active_Unrestricted --> Soft_Restricted: Suspect Velocity / Unusual Overseas
    note right of Soft_Restricted
        - Blocks Card-Not-Present (CNP) e-Commerce
        - Allows Chip+PIN at Physical ATM/POS
        - Outbound 2-Way SMS / Push triggered
    end note

    Soft_Restricted --> Active_Unrestricted: Customer Confirmed "Legitimate" (via SMS/App OTP)
    Soft_Restricted --> Hard_Restricted: Customer Confirmed "Fraud" OR No response in 24h

    Active_Unrestricted --> Hard_Restricted: Confirmed Stolen / Critical Rule Trigger
    note right of Hard_Restricted
        - Total PAN Authorization Block
        - Digital Wallet Tokens Revoked (Apple/Google Pay)
        - Replacement Card Issued Workflow
    end note

    Hard_Restricted --> Active_Unrestricted: Tier-3 Identity Proofing Verified (KYC Re-auth)
    Hard_Restricted --> [*]: Account Closed / Chargeback Processed
```

### Omnichannel Communication Engine
1. **2-Way Interactive SMS**: Immediate trigger (`"Did you try $450 at Merchant X? Reply 1=Yes, 2=No"`).
2. **In-App Mobile Push Notification**: Rich biometric challenge inside mobile banking app.
3. **Outbound IVR / Automated Voice Call**: Escalation if SMS fails to deliver within 5 minutes.
4. **Email Notification**: Detailed summary of suspect activity with dispute links.
5. **Physical Mailer / Regulatory Notice**: Generated for adverse action notices (FCRA / regulatory compliance).

---

## 6. Inbound Customer Re-Authentication Matrix (30+ Tool Catalog)

When a customer contacts the institution (or responds to an alert), the **Dynamic Step-Up Auth Engine** determines the verification level based on current account restriction level and interaction channel.

```mermaid
flowchart TD
    Inbound[Customer Inbound Channel:\nCall Center / IVR / Mobile App / Web / Branch] --> Context[Context & Risk Profiler\nANI/Caller-ID Match, Device Fingerprint, SIM-Swap Check]
    
    Context --> RiskEngine{Determine Auth Tier Needed}
    
    RiskEngine -->|Tier 1: Low Friction| T1[Tier 1: Automated Low Friction]
    RiskEngine -->|Tier 2: Medium Friction| T2[Tier 2: Step-Up Challenge]
    RiskEngine -->|Tier 3: High Friction| T3[Tier 3: Full Identity Proofing]
    
    subgraph T1Tools ["Tier 1: Fast Verification (Self-Service / Frictionless)"]
        T1 --> A1[1. In-App Push Biometric]
        T1 --> A2[2. SMS One-Time Passcode - OTP]
        T1 --> A3[3. Voice Biometrics - Passive Call Stream]
        T1 --> A4[4. Behavioral Biometrics - Typing/Swipe]
        T1 --> A5[5. Silent Network Auth - Carrier OAuth]
        T1 --> A6[6. Device Hardware Token / Secure Enclave]
        T1 --> A7[7. Card PIN - In-Person / IVR]
        T1 --> A8[8. Email Magic Link / OTP]
        T1 --> A9[9. Card CVV2 / Expiry Verification]
        T1 --> A10[10. Last 4 Digits of SSN / Tax ID]
    end

    subgraph T2Tools ["Tier 2: Elevated Verification (Call Center / High-Risk Action)"]
        T2 --> B1[11. Dynamic KBA - Knowledge-Based Questions]
        T2 --> B2[12. Recent Transaction Verification Matrix]
        T2 --> B3[13. Linked Bank Account Micro-Deposit Check]
        T2 --> B4[14. MNO Real-Time SIM-Swap & Porting Age Check]
        T2 --> B5[15. Inbound Carrier ANI spoofing validation - STIR/SHAKEN]
        T2 --> B6[16. Secondary Emergency Contact OTP]
        T2 --> B7[17. FIDO2 / WebAuthn Hardware Security Key]
        T2 --> B8[18. Out-of-Band Callback Verification]
        T2 --> B9[19. WhatsApp Verified Business OTP]
        T2 --> B10[20. Mobile Device Geolocation Proximity Match]
    end

    subgraph T3Tools ["Tier 3: High Friction / Account Unfreeze / Identity Proofing"]
        T3 --> C1[21. Single Gov ID Scan - Driver License OCR + Barcode]
        T3 --> C2[22. 3-Document Package - ID + Utility Bill + Bank Stmt]
        T3 --> C3[23. Live 3D Facial Liveness & Selfie Matching]
        T3 --> C4[24. Video KYC Agent Interview with Geo-tagging]
        T3 --> C5[25. Credit Bureau Soft Inquiry & Credit File Match]
        T3 --> C6[26. Social Security Administration e-CBSV Check]
        T3 --> C7[27. In-Branch Physical ID Inspection & Notary]
        T3 --> C8[28. Passport Chip NFC Reading & Cryptographic Validation]
        T3 --> C9[29. Utility Account Direct API Verification - Plaid/MX]
        T3 --> C10[30. Device Forensic Certificate Re-Issuance]
    end

    T1Tools & T2Tools & T3Tools --> ResultEval{Verification Result}
    ResultEval -->|Pass| Unlock[Clear Case & Lift Restrictions]
    ResultEval -->|Fail| Escalation[Escalate to Fraud Investigator & Freeze]
```

---

## 7. Data Architecture & Event Streaming Backbone

```mermaid
flowchart LR
    subgraph Sources ["Ingestion Sources"]
        Auth[Card Authorizations]
        Clearing[Settlement / Batches]
        Disputes[Chargebacks & Disputes]
        Digital[Mobile / Web Telemetry]
    end

    subgraph StreamingEngine ["Streaming Event Bus & CDC"]
        Kafka[(Kafka Cluster)]
        Debezium[Debezium CDC]
    end

    subgraph FeatureStore ["Feature Store Architecture"]
        Flink[Apache Flink]
        OnlineRedis[(Online: Redis / Aerospike\nLat < 3ms)]
        OfflineLake[(Offline: Iceberg Lakehouse\nHistorical Feature Store)]
    end

    subgraph MLOps ["Continuous Learning & Model Serving"]
        MLOpsEngine[Feature Engineering & Retraining]
        Registry[MLflow / Model Registry]
        Triton[Real-Time Triton Inference]
    end

    Auth --> Kafka
    Clearing --> Kafka
    Disputes --> Debezium --> Kafka
    Digital --> Kafka

    Kafka --> Flink
    Flink -->|Push Online Aggregations: Velocity, Counts| OnlineRedis
    Flink -->|Append Parquet Partitions| OfflineLake

    OfflineLake --> MLOpsEngine
    MLOpsEngine --> Registry
    Registry -->|Automated Hot Reload| Triton
```
