import re
def correct(text):

	text = re.sub(r"\s+"," ", text)
	text = re.sub(r"(?<=\.)(?=[a-zA-Z])", " ", text)
	return text


print correct("This   is  very funny  and    cool.Indeed!")

# ok if not the tabs and PEP8
