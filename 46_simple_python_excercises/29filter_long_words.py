def filter_long_words(l, n):

	for w in l:
		len_words = len(w)
		if len_words > n:
			print w

lista = ['abc','aaaa','asdfasdfadf','asdfg','qwerty','ab']
print filter_long_words(lista, 3)


# Return those words to an output list. Dont print a function that return
# nothing, and first of all don't make such functions.
