#-*- coding: utf-8 -*-


def translate(text):

    d = {
        "merry": "god",
        "christmas": "jul",
        "and": "och",
        "happy": "gott",
        "new": "nytt",
        "year": "ĺr",
    }

    swed = lambda word: d[word]
    translated = map(swed, text)

    return translated

print translate(["merry"])
