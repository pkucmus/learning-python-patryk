# You shouldn't use the python built'in sum() function

def sum(l):
    result = 0
    for i in l:
        result += i
    return result


def multipling(l):
    multipled = reduce(lambda x, y: x*y, l)
    return multipled


lista = [1, 2, 3, 4]
print sum(lista)
print multipling(lista)
