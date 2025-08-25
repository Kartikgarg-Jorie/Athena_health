from datetime import datetime, timezone

def bprint(msg):
    print(f"[{datetime.now(timezone.utc).isoformat()}] {msg}")
