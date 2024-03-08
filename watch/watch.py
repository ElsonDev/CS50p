import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # match case
    if matches := re.search("^.+src=\"https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)\".+$", s, re.IGNORECASE):
        video = matches.group(1)
        url = f"https://youtu.be/{video}"
        return url
    else:
        return "None"



if __name__ == "__main__":
    main()