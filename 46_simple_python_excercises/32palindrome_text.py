from sys import argv
import re


script, filename = argv
f = open(filename, 'rU')
lines = [line.rstrip('\n') for line in f]


def palindrome(text):
    text = re.sub(r"\W+", "", text)
    text = text.replace(" ", "")
    text = text.lower()
    if text[::-1] == text:
        return True
    else:
        return False


def main():

    for line in lines:
        if palindrome(line) == True:
            print line
        else:
            pass


if __name__ == '__main__':
    main()
