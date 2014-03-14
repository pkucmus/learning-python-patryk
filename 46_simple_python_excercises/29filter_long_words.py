def filter_long_words(l, n):

    l2 = []
    for w in l:
        len_words = len(w)
        if len_words > n:
            l2.append(w)
    return l2

lista = ['abc', 'aaaa', 'asdfasdfadf', 'asdfg', 'qwerty', 'ab']
print filter_long_words(lista, 3)
