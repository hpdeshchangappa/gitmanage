# Copilot: please generate a small helper function `format_task` that formats a task dict
# Example output: "Task: <title> [status]"

def format_task(task: dict) -> str:
    """
    Format a task dict into a short string.
    Example output: "Task: <title> [Status]"
    """
    title = task.get("title") if task.get("title") else "<untitled>"
    status = task.get("status") if task.get("status") else "unknown"
    # Normalize status presentation
    try:
        status_str = str(status).strip().capitalize()
    except Exception:
        status_str = "unknown"
    return f"Task: {title} [{status_str}]"

