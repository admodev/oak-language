import sys
import os
from .runtime import run, run_script

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m oak.main \"1 + 2 * 3\" OR python -m oak.main script.oak")
        return

    arg = sys.argv[1]

    if os.path.isfile(arg) and arg.endswith('.oak'):
        with open(arg, 'r') as f:
            source = f.read()
        result = run_script(source)
    else:
        result = run(arg)

    print("Result:", result)

if __name__ == '__main__':
    main()
