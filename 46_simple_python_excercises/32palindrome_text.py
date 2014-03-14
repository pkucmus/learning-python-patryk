from sys import argv
import re

try:
    script, filename = argv
except ValueError:
    print "You have to input a file name:"
    filename = raw_input()

f = open(filename, 'rU')
lines = [line.rstrip('\n') for line in f]


def palindrome(text):
    text = re.sub(r"\W+", "", text)
    text = text.replace(" ", "")
    text = text.lower()
    if text[::-1] == text:
        return True
    return False


def main():
    for line in lines:
        if palindrome(line) is True:
            print line


if __name__ == '__main__':
    main()
