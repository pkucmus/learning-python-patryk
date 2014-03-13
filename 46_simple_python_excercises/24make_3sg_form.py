def make_3sg_form(text):

	a = len(text)
	b = a - 1
	c = a - 2
	if text[b:] == "e":
		text = text[:-1]#deleting last character
		text = text + "ies"
		return text


	elif text[b:] == ('o' or 's' or 'x' or'z'):
		text = text + "es"
		return text


	elif text[c:] == ('ch' or 'sh'):
		text = text + "es"
		return text


	else:
		text = text + "s"
		return text


print make_3sg_form("move")

# this is bad whyt you did'ny not use the `endswith()` string method as the
# task proposed?

# make more test like
print "fixes" == make_3sg_form("fix")

# hint
# if text.endswith('e'):
# elif text.endswith(('sh', 's', 'x')):
# get to know the functions you're about to use
# do it your self!
