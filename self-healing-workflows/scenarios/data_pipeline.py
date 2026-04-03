import json
from groq import Groq
from config import GROQ_API_KEY
from workflows.monitor import log_info, log_error

client = Groq(api_key=GROQ_API_KEY)

RAW_DATA = {"user_name": "Alice", "age_years": 30, "email_address": "alice@example.com"}
EXPECTED_SCHEMA = ["name", "age", "email"]

def detect_schema_mismatch(data: dict, expected: list) -> list:
    return [k for k in expected if k not in data]

def auto_map_fields(data: dict, expected: list) -> dict:
    prompt = f"""
You are a data mapping agent.
Map the source fields to target fields and return ONLY a valid JSON object.

Source data: {data}
Target schema fields: {expected}

Return the mapped object with exactly these keys: {expected}
No explanation. No markdown. Just JSON.
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)

def run():
    log_info("=== Scenario: Data Pipeline Error ===")
    missing = detect_schema_mismatch(RAW_DATA, EXPECTED_SCHEMA)
    if missing:
        log_error(f"Schema mismatch. Missing fields: {missing}")
        log_info("Invoking AI field mapper...")
        fixed = auto_map_fields(RAW_DATA, EXPECTED_SCHEMA)
        log_info(f"Auto-mapped result: {fixed}")
    else:
        log_info(f"Schema OK: {RAW_DATA}")

if __name__ == "__main__":
    run()