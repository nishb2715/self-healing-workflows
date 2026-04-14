import json
import os

LOG_FILE = "observability/logs.json"

def log_event(step, status, details):
    # PRINT to terminal (🔥 important)
    print(f"{step} → {status} → {details}")

    # Ensure file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "step": step,
        "status": status,
        "details": details
    })

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)