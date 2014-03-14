from sys import argv
import re


def main(filename):
    try:
        script, filename = argv
    except ValueError:
        print "You have to input a file name:"
        filename = raw_input()
    in_file = open(filename, 'rU')

    hapax = []
    frequency = {}
    for line in in_file:
        words = line.split()
        for word in words:
            word = word.lower()
            word = re.sub(r"\W+", "", word)
            if word not in frequency:
                frequency[word] = frequency.get(word, 1)
    for row in frequency:
        hapax.append(row)

    return "List of hapax legomenon words from file {0}:\n{1}".format(filename, hapax)


print main(argv)


if __name__ == '__main__':
    main(argv)
