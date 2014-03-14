def find_longest_word(l):

    return max(len(w) for w in l)


lista = ['abc', 'aaaa', 'asdfasdfadf', 'asdfg', 'qwerty', 'ab']
print find_longest_word(lista)

# OK but my brain hurst from your coding style xD
# I appreciate :D
# Secound example, just for heal your brain :)
"""
def find_longest_word(text):

    longest = max(text, key=len)
    return len(longest)


print find_longest_word(['aaaaaaa', 'bbbbbbbbbbbbb', 'cc', 'd', 'dddd'])
"""
