import sys
from pathlib import Path
from tabulate import tabulate

table = []

if len(sys.argv) == 2:
    path = Path(sys.argv[1])
    if path == path:
        if path.is_file() and sys.argv[1].endswith(".csv"):
            with open(path) as file:
                for line in file:
                    i = line.rstrip().split(",")
                    table.append(i)

                print(tabulate(table, headers="firstrow", tablefmt="grid"))

        elif path.is_file() and not sys.argv[1].endswith("py"):
            sys.exit("Not a Python file")
        else:
            sys.exit("File does not exits")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")
