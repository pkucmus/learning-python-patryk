#-*- coding: utf-8 -*-

TRANSLATION_DICT = {
    'and': 'och',
    'christmas': 'jul',
    'happy': 'gott',
    'merry': 'god',
    'new': 'nytt',
    'year': 'ĺr'
}




def translate(text):
    return [TRANSLATION_DICT.get(word, word) for word in text]


    # eng = lambda word: d[word]
    # translated = map(eng, text)

    # return translated

print translate("merry christmas and happy new year".split(' '))
# print translate("god jul och gott nytt ĺr".split(' '))
