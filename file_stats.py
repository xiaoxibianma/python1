import sys


def stats(filename):
    words = 0
    i = 0
    character = 0
    maxline = 0
    with open(filename) as fh:
        for line in fh:
            character = len(line) + character
            line = line.rstrip()
            if len(line) > maxline:
                maxline = len(line)
            words = len(line.split()) + words
            i += 1
    return (character, words, i, maxline)


if __name__ == "__main__":
    filename = sys.argv[1]
    char, word, line, lonline = stats(filename)
    print("Characters:", char)
    print("Words:", word)
    print("Lines:", line)
    print("Longest line:", lonline)
