import requests
import json
from config import BASE_URL, PRACTICE_ID, DEPARTMENT_ID, PROVIDER_ID, APPOINTMENT_DATE, APPOINTMENT_TIME, APPOINTMENT_TYPE_ID
from utils import bprint

def create_open_slot(token):
    url = f"{BASE_URL}/v1/{PRACTICE_ID}/appointments/open"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    payload = {
        "departmentid": DEPARTMENT_ID,
        "providerid": PROVIDER_ID,
        "appointmentdate": APPOINTMENT_DATE,
        "appointmenttime": APPOINTMENT_TIME,
        "appointmenttypeid": APPOINTMENT_TYPE_ID
    }

    bprint(f"Creating open slot for {APPOINTMENT_DATE} at {APPOINTMENT_TIME}...")
    resp = requests.post(url, headers=headers, data=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    print(f"Open slot created: {json.dumps(data, indent=2)}")
    return data
