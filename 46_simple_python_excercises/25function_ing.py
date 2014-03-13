# use what you coded earlier - DRY

from task_4_vowel import vowel

# def vowel(i):
#   i = i.lower()
#   if i == ("a" or "e" or "i" or "o" or "u" or "y"):
#       return True
#   else:
#       return False


# DO TASK 24 FIRST THAN WITH THE KNOWLEDGE EARNED FROM THERE WEREWRITE THIS
# CRAP :D

def function_ing(text):

    if text != ("be" or "see" or "flee" or "knee"):

        a = len(text)
        b = a - 1
        c = a - 2
        if text[b:] == "e":
            text = text[:-1]  # deleting last character
            text = text + "ing"
            return text
# ZMIENIC SLICE POKAZUJE WSZYSTKO BEZ OSTATNICH ZAMIAST TYLKO OSTATNIE

        elif text[c:] == "ie":
            text = text[:-2]  # deleting last characters
            text = text + "ying"
            return text

        elif not vowel(text[b:]):
            if vowel(text[c:]):
                if not vowel(text[b:]):
                    text = text + text[b:] + "ing"
                else:
                    pass
            else:
                pass

        else:
            text = text + "ing"
            return text

    else:
        return text


print function_ing("movie")
