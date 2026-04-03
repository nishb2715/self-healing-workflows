from workflows.monitor import log_info, log_error

def run_step(step_name: str, func, *args, **kwargs):
    """Execute a single workflow step and return structured result."""
    log_info(f"Executing step: '{step_name}'")
    try:
        result = func(*args, **kwargs)
        log_info(f"Step '{step_name}' completed successfully.")
        return {"step": step_name, "status": "success", "result": result}
    except Exception as e:
        log_error(f"Step '{step_name}' failed: {e}")
        return {"step": step_name, "status": "failed", "error": str(e)}

def run_pipeline(steps: list) -> list:
    """
    Run a list of steps in sequence.
    Each step is a dict: {"name": str, "func": callable, "args": tuple, "kwargs": dict}
    Stops pipeline on first failure.
    """
    results = []
    for step in steps:
        result = run_step(
            step["name"],
            step["func"],
            *step.get("args", ()),
            **step.get("kwargs", {})
        )
        results.append(result)
        if result["status"] == "failed":
            log_error(f"Pipeline halted at step '{step['name']}'.")
            break
    return results