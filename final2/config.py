from datetime import datetime, timedelta, timezone

# Athena API config
BASE_URL = "https://api.preview.platform.athenahealth.com"
PRACTICE_ID = "195900"
CLIENT_ID = "0oayl77e4iEfC8TBD297"
CLIENT_SECRET = "v-PCXewvz3xGHtH6S-r4pXF-7w5wSZnwdtUfG-513wnqBwjXQiXb3HwYoq2K4vzx"

# Booking details
# PATIENT_ID = "60327"
DEPARTMENT_ID = 1
PROVIDER_ID = 2296
REASON_ID =1285
APPOINTMENT_TYPE_ID = 82
APPOINTMENT_DATE = (datetime.now(timezone.utc) + timedelta(days=1)).strftime("%m/%d/%Y")
APPOINTMENT_TIME = "09:30"
