import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Develop regex for 0.0.0.0 to 255.255.255.255
    # 0-9
    # 1-9 + 0-9 (10-99)
    # 1 + 0-9 + 0-9 (100-199)
    # 2 + 0-4 + 0-9 (200-249)
    # 25 + 0-5 (250-255)

    if re.search(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|(2[0-4][0-9])|(25[0-5]))\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|(2[0-4][0-9])|(25[0-5]))$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
