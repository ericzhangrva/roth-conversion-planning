# Self-Hosted Home VPN Guide (Xray VLESS-Reality)

Complete guide to hosting a private, high-speed, anti-DPI VPN on your home **Verizon FiOS 1 Gbps** network using a dedicated Linux box. Designed specifically for reliable, undetected access when traveling in China.

---

## 1. System Overview & Architecture

* **ISP & Bandwidth:** Verizon FiOS ~1 Gbps (Symmetric Download / Upload).
* **Router:** Verizon FiOS Router **CR1000A** (`192.168.1.1`).
* **Host Machine:** Dedicated 24/7 Linux Box (16GB RAM, Ethernet connection).
* **Protocol:** **Xray (VLESS + Reality + Vision)**.
  * **Why Reality?** It borrows the TLS 1.3 certificate of a legitimate public service (e.g. `swdist.apple.com`). DPI firewalls cannot distinguish your VPN traffic from standard web traffic to Apple. No custom domain or SSL certificate purchase required.

```
[Traveling Client in China (iPhone/Mac)]
                 │
                 ▼ (Encrypted TLS 1.3 masquerading as Apple/Microsoft)
    [The Great Firewall (DPI)] ──► Passes traffic through (looks like regular HTTPS)
                 │
                 ▼
     [Verizon CR1000A Router]
                 │ (Port Forward: 8443)
                 ▼
[Home Linux Box (Xray Server on 192.168.1.150)]
                 │
                 ▼ (Gigabit FiOS Outbound)
        [Global Internet]
```

---

## 2. Server Setup (On the Linux Box)

### Step 1: Assign a Fixed Local IP
1. Plug the Linux box into your Verizon CR1000A router using an **Ethernet cable**.
2. Find its IP address:
   ```bash
   ip a
   ```
   *(Note the local IP, e.g. `192.168.1.150`, and MAC address).*
3. Log into your router at `http://192.168.1.1` $\rightarrow$ **Advanced $\rightarrow$ DHCP Reservations**. Reserve this IP for the Linux box so it never changes.

---

### Step 2: Install Xray
Run the official installation script:
```bash
sudo bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
```

---

### Step 3: Generate Authentication Keys
Run each command and copy the outputs to a notepad:

```bash
# 1. Generate Client UUID:
xray uuid

# 2. Generate X25519 Keypair (Private & Public key):
xray x25519

# 3. Generate Short ID:
openssl rand -hex 8
```

You will receive:
* **UUID:** (e.g., `3c1b6e4a-8f92-4d1e-bf82-73a45c6d1234`)
* **Private Key:** (e.g., `2N7...`) $\rightarrow$ *Goes into server config*
* **Public Key:** (e.g., `8K2...`) $\rightarrow$ *Goes into client apps*
* **Short ID:** (e.g., `b4c91d8a2f0e3115`) $\rightarrow$ *Used on both*

---

### Step 4: Configure Xray Server
Open the configuration file:
```bash
sudo nano /usr/local/etc/xray/config.json
```

Replace the entire contents with:

```json
{
  "log": {
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "port": 8443,
      "protocol": "vless",
      "settings": {
        "clients": [
          {
            "id": "PASTE_YOUR_UUID_HERE",
            "flow": "xtls-rprx-vision"
          }
        ],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "show": false,
          "dest": "swdist.apple.com:443",
          "xver": 0,
          "serverNames": [
            "swdist.apple.com"
          ],
          "privateKey": "PASTE_YOUR_PRIVATE_KEY_HERE",
          "shortIds": [
            "PASTE_YOUR_SHORT_ID_HERE"
          ]
        }
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom"
    }
  ]
}
```

Save and exit:
* Press `Ctrl + O`, then `Enter`
* Press `Ctrl + X`

---

### Step 5: Start & Enable the Service
```bash
sudo systemctl enable --now xray
sudo systemctl status xray
```
Ensure it says **`active (running)`** in green.

---

## 3. Router Configuration (Verizon CR1000A)

1. Open your browser and go to `http://192.168.1.1`.
2. Log in using the admin credentials printed on the router label.
3. Navigate to **Advanced $\rightarrow$ Port Forwarding**.
4. Add a new port forwarding rule:
   * **Protocol:** TCP
   * **External / WAN Port:** `8443`
   * **Internal / LAN Port:** `8443`
   * **Target Device / IP:** Your Linux box's local IP (e.g. `192.168.1.150`).
5. Click **Save / Apply**.

---

## 4. Free Dynamic DNS (DuckDNS) Setup

Because your Verizon public IP (`74.110.241.197`) can change periodically:

1. Go to [DuckDNS.org](https://www.duckdns.org) and log in with Google or GitHub.
2. Create a subdomain (e.g., `myhome-fios.duckdns.org`).
3. Copy your account **token**.
4. On your Linux box, set up an automatic update cron job:
   ```bash
   mkdir -p ~/duckdns
   cat << 'EOF' > ~/duckdns/duck.sh
   echo url="https://www.duckdns.org/update?domains=YOUR_SUBDOMAIN&token=YOUR_TOKEN&ip=" | curl -k -o ~/duckdns/duck.log -K -
   EOF
   chmod 700 ~/duckdns/duck.sh
   ```
   *(Replace `YOUR_SUBDOMAIN` and `YOUR_TOKEN` with your actual DuckDNS details).*

5. Add it to crontab:
   ```bash
   (crontab -l 2>/dev/null; echo "*/10 * * * * ~/duckdns/duck.sh >/dev/null 2>&1") | crontab -
   ```
   Now, even if Verizon changes your IP, `myhome-fios.duckdns.org` will automatically update every 10 minutes.

---

## 5. Client Configuration (Phones & Laptops)

### Your One-Click VLESS Link
Construct your connection link using your credentials:

```text
vless://YOUR_UUID@YOUR_SUBDOMAIN.duckdns.org:8443?encryption=none&flow=xtls-rprx-vision&security=reality&sni=swdist.apple.com&fp=chrome&pbk=YOUR_PUBLIC_KEY&sid=YOUR_SHORT_ID&type=tcp#FiOS-Home
```

Simply copy this string to your clipboard and open your client app:

### Recommended Apps:
* **iOS (iPhone / iPad):**
  * **Shadowrocket** (US App Store, $2.99 — Gold standard, automatically imports from clipboard).
  * **Sing-box** or **V2Box** (Free).
* **macOS:**
  * **FoXray** (Mac App Store).
  * **Clash Verge Rev** or **V2RayXS**.
* **Android:**
  * **v2rayNG** or **Sing-box**.
* **Windows:**
  * **v2rayN** or **Sing-box**.

---

## 6. Pre-Departure Checklist

> [!IMPORTANT]
> **Always test from outside your home Wi-Fi before traveling!**

1. **Cellular Test:** Turn off Wi-Fi on your iPhone so you are strictly on LTE/5G.
2. Open **Shadowrocket / FoXray** and toggle the connection **ON**.
3. In Safari, open [whatismyip.com](https://whatismyip.com).
4. Verify that the displayed IP matches your **home Verizon public IP**.
5. **BIOS Power Setting (Crucial):** Enter your Linux PC's BIOS settings (reboot and press `Del` or `F2`), locate **Power Management**, and set **"AC Back / Power On After Failure"** to **"Always On"** or **"Last State"**. This ensures your server boots back up automatically if your house ever experiences a brief power outage while you are away.
