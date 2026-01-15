"""
CLI commands implementations.
"""

import os
from ai_checks.syntax import check_syntax
from ai_checks.style import check_style

def analyze_code(path: str):
    """
    Analyze a file or all files in a directory.
    """
    if os.path.isfile(path):
        files = [path]
    elif os.path.isdir(path):
        files = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.endswith(".py")  # start with Python, expand later
        ]
    else:
        print(f"Path {path} not found.")
        return

    for file in files:
        print(f"Analyzing {file} ...")
        syntax_ok, syntax_msg = check_syntax(file)
        style_ok, style_msg = check_style(file)

        print(f"Syntax: {syntax_msg}")
        print(f"Style: {style_msg}")
        print("-" * 30)
