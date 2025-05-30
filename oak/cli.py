import sys
import os
from .runtime import run_script

def main():
    print(f"Running from: {__file__}")
    print(f"sys.path: {sys.path}")
    if len(sys.argv) < 2:
        print("Usage: oak <script.oak>")
        sys.exit(1)

    script_path = sys.argv[1]
    if not os.path.isabs(script_path):
        script_path = os.path.abspath(script_path)

    with open(script_path, "r") as f:
        source = f.read()

    result = run_script(source)
    print(f"Result: {result}")
