def main():
    twt = input("Input: ")
    print("Output:", shorten(twt))

def shorten(word):
    excluded_char = ["a", "e", "i", "o", "u"]
    for c in word:
        if c in excluded_char:
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    main()
