import requests
from datetime import datetime, UTC
import json
from get_access_token import get_access_token

BASE_URL = "https://api.preview.platform.athenahealth.com"
PRACTICE_ID = "195900"

def bprint(msg):
    print(f"[{datetime.now(UTC).isoformat()}] {msg}")

def get_notes(token, appointment_id, show_deleted=False, limit=1500, offset=0):
    """
    Fetch all notes for a given appointment.

    Args:
        token (str): Bearer token for authentication
        appointment_id (int/str): Appointment ID to fetch notes for
        show_deleted (bool): Include deleted notes if True
        limit (int): Max number of notes to retrieve (default 1500, max 5000)
        offset (int): Starting offset for pagination

    Returns:
        list: List of note dicts (each dict contains full note details)
    """
    url = f"{BASE_URL}/v1/{PRACTICE_ID}/appointments/{appointment_id}/notes"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    params = {
        "showdeleted": str(show_deleted).lower(),
        "limit": limit,
        "offset": offset,
    }

    bprint(f"Fetching notes for appointment {appointment_id}...")
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    notes = data.get("notes", [])

    bprint(f"Found {len(notes)} notes.")
    return notes

def ask_yes_no(question):
    while True:
        ans = input(f"{question} (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please type 'y' or 'n'.")

def main():
    patient_id = input("Enter patient ID (optional, just for reference): ").strip()

    token = None
    appointment_id = None
    notes = None

    if ask_yes_no("Run get_access_token()?"):
        token = get_access_token()
    else:
        print("Skipping token fetch. Cannot proceed without token.")
        return

    appointment_id_input = input("Enter appointment ID to fetch notes for: ").strip()
    if not appointment_id_input.isdigit():
        print("Invalid appointment ID. Must be a number.")
        return
    appointment_id = int(appointment_id_input)

    if ask_yes_no("Run get_notes()?"):
        notes = get_notes(token, appointment_id, show_deleted=True)
        print(f"Notes:\n{json.dumps(notes, indent=2)}")
    else:
        print("Skipping get_notes.")

    print("\n=== Summary ===")
    print(json.dumps({
        "patient_id": patient_id,
        "appointment_id": appointment_id,
        "notes": notes
    }, indent=2))

if __name__ == "__main__":
    main()
