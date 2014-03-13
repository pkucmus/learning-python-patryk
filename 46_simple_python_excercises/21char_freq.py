def char_freq( text ):
    return {
        char: text.count(char) for char in set(text)
    }
    # dictionary = {}


    # for a in text:
    #     keys = dictionary.keys()

    #     if a in keys:
    #         dictionary[a] += 1

    #     else:
    #         dictionary[a] = 1

    # return dictionary


print char_freq("aaaaaaaaaassssssssssssbbbbbbbbbbffff")
