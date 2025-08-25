import requests
import json
from config import BASE_URL, PRACTICE_ID
from utils import bprint
from datetime import datetime

def create_note(token, appointment_id):
    # Ask for note text
    note_text = input("Enter note text: ").strip()
    if not note_text:
        note_text = f"Automated note created on {datetime.utcnow().isoformat()} UTC"

    display_flag = input("Display on schedule? (y/n): ").strip().lower()
    display_flag = "true" if display_flag == "y" else "false"

    url = f"{BASE_URL}/v1/{PRACTICE_ID}/appointments/{appointment_id}/notes"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    payload = {
        "notetext": note_text,
        "displayonschedule": display_flag
    }

    bprint(f"Creating note for appointment {appointment_id}...")
    resp = requests.post(url, headers=headers, data=payload, timeout=60)
    resp.raise_for_status()
    print(resp)
    data = resp.json()
    bprint(f"Note created: {json.dumps(data, indent=2)}")
    return data

