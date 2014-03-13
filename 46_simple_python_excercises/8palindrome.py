def reverse(text):
    reverse_text = text[::-1]
    return reverse_text


def palindrome(text):
    if reverse(text) == text:
    # if text[::-1] == text:
        return True
    else:
        return False

print palindrome("radar")
