
def generate_n_chars(n):

    n = n*"x"
    return n


print generate_n_chars(5) == ("xxxxx")
print generate_n_chars(10) == ("xxxxxxxxxx")
print generate_n_chars(15) == ("xxxxxxxxxxxxxxx")
