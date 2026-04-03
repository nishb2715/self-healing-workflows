import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/workflow.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_info(msg): logging.info(msg); print(f"[INFO] {msg}")
def log_error(msg): logging.error(msg); print(f"[ERROR] {msg}")

def capture_failure(step_name, error):
    log_error(f"FAILURE at '{step_name}': {error}")
    return {"step": step_name, "error": str(error)}