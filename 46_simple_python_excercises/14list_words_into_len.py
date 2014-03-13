def list_words_into_len(lista):

    # you should use a comprehantion list to make it more pythonic

    return {i: len(i) for i in lista}

    # lista_len = []

    # for i in lista:
    #     i = len(i)
    #     lista_len.append(i)

    # return lista_len

lista = ['abs', 'sgasdsad', 'sdfag', "dfgd"]
print list_words_into_len(lista)
