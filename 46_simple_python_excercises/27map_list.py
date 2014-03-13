def map_list_word_ls(text):


    return [len(word) for word in text]


def map_list_word_hf(text):


    return map(len, text)


print map_list_word_ls(['aaaaaaaa','vvvv','bbbbbbb','ssssssss'])
print map_list_word_hf(['aaaaaaaa','vvvv','bbbbbbb','ssssssss'])


# This is not the whole task! "Write it in three different ways"
