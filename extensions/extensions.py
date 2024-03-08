def main():

    # ask the user for file name #
    # remove any whitespace and force all lower caps #

    file_type = input("File name: ").strip(" ").lower()

    # match the inputed file type and print the relevant media type

    if ".gif" in file_type:
        print("image/gif")
    elif ".jpeg" in file_type:
        print("image/jpeg")
    elif ".jpg" in file_type:
        print("image/jpeg")
    elif ".png" in file_type:
        print("image/png")
    elif ".pdf" in file_type:
        print("application/pdf")
    elif ".txt" in file_type:
        print("text/plain")
    elif ".txt" in file_type:
        print("text/plain")
    elif ".zip" in file_type:
        print("application/zip")
    else:
        print("application/octet-stream")

main()