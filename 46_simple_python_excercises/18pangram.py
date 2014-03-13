#-*- coding: utf-8 -*-

# Alphabet should be a constant
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

#     alphabet = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
#     string = string.lower()
#     for n in string:
#         alphabet[n] = 1

#     x = 0

#     for k, v in alphabet.iteritems():
# #       print k, v # testowo

#         if v == 1:
# #           print x # testowo
#             x += 1
#         else:
#             pass
#     print x
#     if x > 25:
#         print True
#     else:
#         print False

print panagram("The quick brown fox jumps over the lazy dog")
