import requests
import random
from config import OPENWEATHER_API_KEY
from core.monitor import monitor
from core.diagnosis_agent import diagnose
from core.recovery_engine import recover
from core.validator import validate

PRIMARY_URL = "https://api.openweathermap.org/data/2.5/weather"
BACKUP_URL  = "https://wttr.in/London?format=j1"

def fetch_primary(city="London"):
    if random.random() < 0.6:
        raise TimeoutError("Simulated API timeout")
    r = requests.get(PRIMARY_URL, params={"q": city, "appid": OPENWEATHER_API_KEY}, timeout=5)
    r.raise_for_status()
    data = r.json()
    return {"city": data["name"], "temp": data["main"]["temp"], "desc": data["weather"][0]["description"]}

def fetch_backup(city="London"):
    r = requests.get(BACKUP_URL, timeout=5)
    r.raise_for_status()
    data = r.json()
    return {"city": "London", "temp": data["current_condition"][0]["temp_C"], "desc": data["current_condition"][0]["weatherDesc"][0]["value"]}

def run():
    log_info("=== Scenario: API Failure ===")
    result = execute_with_recovery(
        step_name="fetch_weather",
        func=fetch_primary,
        args=("London",),
        fallback_func=fetch_backup,
        max_retries=3
    )
    if result["status"] == "failed":
        failure = capture_failure("fetch_weather", result["error"])
        diagnosis = diagnose(failure)
        log_info(f"Diagnosis: {diagnosis}")
    else:
        valid = validate(result, expected_keys=["city", "temp", "desc"])
        log_info(f"Final result: {result['result']} | Valid: {valid}")

if __name__ == "__main__":
    run()