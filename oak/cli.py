import sys
import os
from .script_parser import parse_script
from .compiler import compile_script, save_binary_script
from .runtime import run_script

def main():
    print(f"Running from: {__file__}")
    print(f"sys.path: {sys.path}")

    if len(sys.argv) < 2:
        print("Usage: oak <script.oak> or oak -c <script.oak>")
        sys.exit(1)

    if sys.argv[1] == "-c":
        script_path = sys.argv[2]
        output_path = script_path.replace(".oak", ".oakc")
        with open(script_path, "r") as f:
            source = f.read()
        sections = parse_script(source)
        compiled = compile_script(sections)
        save_binary_script(compiled, output_path)
        print(f"Compiled successfully to {output_path}")
    elif sys.argv[1].endswith(".oakc"):
        from .runtime import run_compiled_script
        result = run_compiled_script(sys.argv[1])
        print(f"Result: {result}")
    else:
        script_path = sys.argv[1]
        with open(script_path, "r") as f:
            source = f.read()
        result = run_script(source)
        print(f"Result: {result}")
