import time
from workflows.monitor import log_info, log_error

def execute_with_recovery(step_name, func, args=(), kwargs={}, fallback_func=None, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            log_info(f"Attempt {attempt}: Running '{step_name}'")
            result = func(*args, **kwargs)
            log_info(f"'{step_name}' succeeded on attempt {attempt}")
            return {"status": "success", "result": result, "attempts": attempt}
        except Exception as e:
            log_error(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                wait = 2 ** attempt
                log_info(f"Retrying in {wait}s (exponential backoff)...")
                time.sleep(wait)
            else:
                if fallback_func:
                    log_info(f"All retries exhausted. Trying fallback for '{step_name}'...")
                    try:
                        result = fallback_func(*args, **kwargs)
                        return {"status": "fallback_success", "result": result, "attempts": attempt}
                    except Exception as fe:
                        log_error(f"Fallback also failed: {fe}")
                return {"status": "failed", "error": str(e), "attempts": attempt}