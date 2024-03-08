import sys
from PIL import Image, ImageOps

def main():
    
    if isvalid(sys.argv):
        shirt = Image.open("shirt.png")
        size = shirt.size
        with Image.open(sys.argv[1]) as img:
            img = ImageOps.fit(img, size, bleed=0.0, centering=(0.5, 0.5))
            img.paste(shirt, shirt)
            img.save(sys.argv[2], format=None)


def isvalid(cli):
    if len(cli[1:]) < 2:
        sys.exit("Too few command-line arguments")

    elif len(cli[1:]) > 2:
        sys.exit("Too many command-line arguments")

    cli[1] = cli[1].lower()
    cli[2] = cli[2].lower()

    if cli[1].endswith(".jpg") and cli[2].endswith(".jpg"):
        return True

    elif cli[1].endswith(".jpeg") and cli[2].endswith(".jpeg"):
        return True

    elif cli[1].endswith(".png") and cli[2].endswith(".png"):
        return True

    else:
        sys.exit("Invalid input")



















if __name__ == "__main__":
    main()