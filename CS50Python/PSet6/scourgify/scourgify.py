import sys
from pathlib import Path
import csv

students = []

if len(sys.argv) == 3:
    path = Path(sys.argv[1])
    if path == path:
        if path.is_file() and sys.argv[1].endswith(".csv"):
            with open(path) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})

            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for student in students:
                    last, first = student["name"].split(",")
                    writer.writerow(
                        {
                            "first": first.strip(),
                            "last": last,
                            "house": student["house"],
                        }
                    )

        else:
            sys.exit(f"Could not read {path}")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")
