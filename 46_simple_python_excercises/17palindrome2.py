
import re

PHRASES = [
    "Go hang a salami I'm a lasagna hog",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!"
]


def palindrome(text):
    text = re.sub(r"\W+", "", text)
    text = text.replace(' ', '')
    text = text.lower()
    if text[::-1] == text:
        return True
    else:
        return False

print palindrome("Go hang a salami I'm a lasagna hog")
print palindrome("Was it a rat I saw?")
print palindrome("Step on no pets")
print palindrome("Sit on a potato pan, Otis")
print palindrome("Lisa Bonet ate no basil")
print palindrome("Satan, oscillate my metallic sonatas")
print palindrome("I roamed under it as a tired nude Maori")
print palindrome("Rise to vote sir")
print palindrome("Dammit, I'm mad!")
