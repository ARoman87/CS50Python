import sys
from pathlib import Path


if len(sys.argv) == 2:
    path = Path(sys.argv[1])
    if path == path:
        if path.is_file() and sys.argv[1].endswith(".py"):
            with open(path) as file:
                line_count = len(open(path).readlines())
                for line in file:
                    if line.strip().startswith("#") or line.startswith("\n"):
                        line_count -= 1
                    elif line.isspace():
                        line_count -= 1
            print(line_count)
        elif path.is_file() and not sys.argv[1].endswith("py"):
            sys.exit("Not a Python file")
        else:
            sys.exit("File does not exits")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")
