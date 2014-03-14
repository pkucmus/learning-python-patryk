from sys import argv
import re


def word_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def read_words(filename):
    try:
        script, filename = argv
    except ValueError:
        print "You have to input a file name:"
        filename = raw_input()
    f = open(filename).read().split()
    return f


def main(filename):
    words_sum = 0.0
    len_word_sum = []
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.iteritems():
        words_sum += count
        word = re.sub(r"\W+", "", word)
        len_word_sum += word
    len_word_sum = len(len_word_sum)
    result = len_word_sum/words_sum

    return "Avarage word length in file: {0} is {1}".format(filename, result)


print main(argv)

if __name__ == '__main__':
    main(argv)
