from workflows.monitor import log_info, log_error

def validate(result: dict, expected_keys: list) -> bool:
    if result.get("status") not in ("success", "fallback_success"):
        log_error(f"Validation failed: workflow did not succeed. Status: {result.get('status')}")
        return False
    data = result.get("result", {})
    if isinstance(data, dict):
        missing = [k for k in expected_keys if k not in data]
        if missing:
            log_error(f"Validation failed: missing keys {missing}")
            return False
    log_info("Validation passed.")
    return True