def is_member(x, a):
    for b in a:
        if x == b:
            return True
    return False


print is_member(5, [1, 2, 3, 4, 5, 6, 7, 8])
