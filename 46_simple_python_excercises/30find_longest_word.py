def find_longest_word(text):

    longest = max(text, key = len)
    return len(longest)


print find_longest_word(['aaaaaaa','bbbbbbbbbbbbb','cc','d','dddd'])