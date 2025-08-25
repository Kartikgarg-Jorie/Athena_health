import base64
import requests
from datetime import datetime, UTC

BASE_URL = "https://api.preview.platform.athenahealth.com"
PRACTICE_ID = "195900"
CLIENT_ID = "0oayl77e4iEfC8TBD297"
CLIENT_SECRET = "v-PCXewvz3xGHtH6S-r4pXF-7w5wSZnwdtUfG-513wnqBwjXQiXb3HwYoq2K4vzx"

def bprint(msg):
    """Print message with current UTC timestamp."""
    print(f"[{datetime.now(UTC).isoformat()}] {msg}")

def get_access_token():
    url = f"{BASE_URL}/oauth2/v1/token"
    auth_str = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_b64 = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_b64}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "athena/service/Athenanet.MDP.*"
    }

    bprint("Requesting access token...")
    resp = requests.post(url, headers=headers, data=data, timeout=30)
    resp.raise_for_status()
    token = resp.json()["access_token"]
    bprint("Access token acquired.")
    return token

if __name__ == "__main__":
    token = get_access_token()
    print(f"Access token: {token}")
