#-*- coding: utf-8 -*-

import string
ALPHABET = list(string.ascii_lowercase)


def panagram(string):
    occurent_chars = {}
    for i in string:
        if i in ALPHABET:
            if occurent_chars.get(i):
                occurent_chars[i] += 1
            else:
                occurent_chars[i] = 1
    return len(occurent_chars) == len(ALPHABET)


print panagram("The quick brown fox jumps over the lazy dog")
