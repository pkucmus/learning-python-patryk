# the task gives you a list of phrases to use/test you should have it heve in a
# constant

# FINISH THIS TASK!

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
    text = text.replace(' ','')
    text = text.lower()
    if text[::-1] == text:
        return True
    else:
        return False

print palindrome("Step on no pets")
