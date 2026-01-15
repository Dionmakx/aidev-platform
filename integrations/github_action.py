"""
Example integration with GitHub Actions.
This script could be called in CI to run checks automatically.
"""

import sys
from cli.commands import analyze_code

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    analyze_code(target)
