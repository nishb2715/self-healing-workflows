import requests
import time
from utils.logger import log_event

def call_api():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=2)
        return response.json()
    except:
        return None

def run_api_workflow():
    log_event("API", "START", "Calling primary API")

    retries = 3
    delay = 2

    for i in range(retries):
        result = call_api()

        if result:
            log_event("API", "SUCCESS", "Primary API worked")
            return result

        log_event("API", "RETRY", f"Retry attempt {i+1}")
        time.sleep(delay)
        delay *= 2

    # fallback
    log_event("API", "FALLBACK", "Switching to backup API")

    backup = requests.get("https://jsonplaceholder.typicode.com/posts/2").json()

    log_event("API", "SUCCESS", "Backup API worked")

    return backup