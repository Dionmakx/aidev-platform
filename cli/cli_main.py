"""
Command Line Interface for AI Dev Platform.
"""

import sys
from cli.commands import analyze_code

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli_main.py <file_or_directory_to_analyze>")
        sys.exit(1)

    target = sys.argv[1]
    analyze_code(target)

if __name__ == "__main__":
    main()
