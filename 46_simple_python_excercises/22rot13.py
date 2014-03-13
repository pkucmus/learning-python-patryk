

def rot(string):

	string = string.encode('rot13')
	return string

print rot("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq")
print rot("Test dzialania w druga strone")


# write your own encoder and decoder

def encode_rot13(raw_string):
    # your code here :D

def decode_rot13(rot13_string):
    # your code here :D

test_text = "Lorem ipsum dolorum"
test_encoded_text = "Yberz vcfhz qbybehz"

# These should pass
print encode_rot13(test_text) == test_encoded_text
print decode_rot13(test_encoded_text) == test_text
print decode_rot13(encode_rot13(test_text)) == test_text
