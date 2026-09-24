"""
Authenticated Private Google Sheets Connector
Supports:
1. Google OAuth 2.0 User Login (credentials.json -> local token.json)
2. Google Service Account (service_account.json)
Keeps the Google Sheet 100% private without public sharing.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
CREDENTIALS_PATH = BASE_DIR / "credentials.json"
SERVICE_ACCOUNT_PATH = BASE_DIR / "service_account.json"
TOKEN_PATH = BASE_DIR / "token.json"

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def get_authenticated_sheets_service():
    """Returns an authorized Google Sheets API service object."""
    try:
        from google.oauth2.credentials import Credentials
        from google.oauth2 import service_account
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        from googleapiclient.discovery import build
    except ImportError:
        print("[-] Required Google Auth libraries missing. Install with: pip install google-auth-oauthlib google-api-python-client")
        return None

    # 1. Try Service Account if present
    if SERVICE_ACCOUNT_PATH.exists():
        creds = service_account.Credentials.from_service_account_file(
            str(SERVICE_ACCOUNT_PATH), scopes=SCOPES
        )
        return build("sheets", "v4", credentials=creds)

    # 2. Try User OAuth Flow
    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_PATH.exists():
                print(f"[-] No credentials.json or service_account.json found in {BASE_DIR}")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    return build("sheets", "v4", credentials=creds)


def read_private_sheet(spreadsheet_id: str) -> Dict[str, List[Dict[str, Any]]]:
    """Reads all tabs from a private Google Sheet using authenticated credentials."""
    service = get_authenticated_sheets_service()
    if not service:
        return {}

    try:
        # Get metadata (tab names)
        meta = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheets = meta.get("sheets", [])
        
        all_tabs_data = {}
        for s in sheets:
            title = s.get("properties", {}).get("title", "Sheet1")
            res = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=f"'{title}'!A1:Z100"
            ).execute()
            rows = res.get("values", [])
            if len(rows) > 1:
                headers = rows[0]
                records = []
                for r in rows[1:]:
                    record = {headers[i]: r[i] if i < len(r) else "" for i in range(len(headers))}
                    records.append(record)
                all_tabs_data[title] = records
                print(f"✅ Loaded {len(records)} rows from tab: '{title}'")

        return all_tabs_data
    except Exception as e:
        print(f"[-] Error reading private Google Sheet: {e}")
        return {}
