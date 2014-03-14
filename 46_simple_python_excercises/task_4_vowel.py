# This is task 4 - name changed to be importable

# You should define a constant so that evantualy other functiona would know
# whay vowels are.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y',)


def vowel(i):
    i = i.lower()
    if i in VOWELS:
        return True
    else:
        return False

print vowel("A")
print vowel("Z")
