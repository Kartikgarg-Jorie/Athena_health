import requests
import json
from config import BASE_URL, PRACTICE_ID, DEPARTMENT_ID, APPOINTMENT_TYPE_ID, REASON_ID
from utils import bprint

def book_appointment(token, appointment_id, patient_id):
    url = f"{BASE_URL}/v1/{PRACTICE_ID}/appointments/{appointment_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    payload = {
        "patientid": patient_id,
        "departmentid": DEPARTMENT_ID,
        "appointmenttypeid": APPOINTMENT_TYPE_ID,
        "reasonid":REASON_ID,
        "urgentyn": "true",
        "nopatientcase": "true",
        "donotsendconfirmationemail": "true",
        "ignoreschedulablepermission": "true",
        "reason": "Booked via API"
    }

    bprint(f"Booking appointment {appointment_id} for patient {patient_id}...")
    resp = requests.put(url, headers=headers, data=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    bprint(f"Appointment booked: {json.dumps(data, indent=2)}")
    return data
