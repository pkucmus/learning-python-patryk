def reverse(text):
    reverse_text = text[::-1]
    return reverse_text


def palindrome(text):
    if reverse(text) == text:
        return True
    else:
        return False

print palindrome("radar")
