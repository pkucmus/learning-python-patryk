def char_freq(text):

    return {char: text.count(char) for char in set(text)}


print char_freq("aaaaaaaaaassssssssssssbbbbbbbbbbffff")
