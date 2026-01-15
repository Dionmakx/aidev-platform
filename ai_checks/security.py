"""
Basic security heuristics for Python code.
"""

def check_security(file_path: str):
    issues = []
    with open(file_path, "r") as f:
        content = f.read()

    if "eval(" in content:
        issues.append("Use of eval detected")
    if "exec(" in content:
        issues.append("Use of exec detected")

    if issues:
        return False, "; ".join(issues)
    return True, "Security checks passed"
