from utils.logger import log_event

def run_schema_workflow():
    log_event("SCHEMA", "START", "Checking schema consistency")

    # Simulated incoming data
    data = {
        "name": "John",
        "agee": 25   # ❌ wrong key (should be 'age')
    }

    expected_schema = ["name", "age"]

    corrected_data = {}

    for key in data:
        if key in expected_schema:
            corrected_data[key] = data[key]
        else:
            log_event("SCHEMA", "MISMATCH", f"Unexpected field: {key}")

            # simple correction logic
            if key == "agee":
                corrected_data["age"] = data[key]
                log_event("SCHEMA", "FIXED", "Mapped 'agee' → 'age'")

    log_event("SCHEMA", "SUCCESS", f"Final data: {corrected_data}")

    return corrected_data