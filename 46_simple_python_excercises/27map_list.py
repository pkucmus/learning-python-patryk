
def map_list_word_fl(text):
    l = []
    for word in text:
        word = len(word)
        l.append(word)
    return l


def map_list_word_ls(text):

    return [len(word) for word in text]


def map_list_word_hf(text):

    return map(len, text)


print map_list_word_fl(['aaaaaaaa', 'vvvv', 'bbbbbbb', 'ssssssss'])
print map_list_word_ls(['aaaaaaaa', 'vvvv', 'bbbbbbb', 'ssssssss'])
print map_list_word_hf(['aaaaaaaa', 'vvvv', 'bbbbbbb', 'ssssssss'])
