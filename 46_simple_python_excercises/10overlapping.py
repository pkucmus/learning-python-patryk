def overlapping(x, y):
    common = list(set(x) & set(y))
    com = len(common)

    if com > 0:
        return True
    else:
        return False

l = [1, 2, 3, 4, 5, 6]
m = [5, 6, 7, 8, 9]
print overlapping(l, m)
