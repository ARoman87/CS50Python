import sys
from pathlib import Path
import os
from PIL import Image, ImageOps

if len(sys.argv) == 3:
    root1, ext1 = os.path.splitext(sys.argv[1])
    root2, ext2 = os.path.splitext(sys.argv[2])
    output = sys.argv[2]
    path = Path(sys.argv[1])
    if (
        path.is_file()
        and not output.endswith(".jpeg")
        and not output.endswith(".jpg")
        and not output.endswith(".png")
    ):
        sys.exit("Invalid output")
    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")
    elif not path.is_file():
        sys.exit("Input does not exist")
        ...
    elif ext1 == ext2:
        with Image.open("shirt.png") as shirt:
            with Image.open(path) as background:
                background = ImageOps.fit(background, shirt.size)
                background.paste(shirt, shirt)
                background.save(sys.argv[2])
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")
