
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def max_of_three(num1, num2, num3):
    return max(num1, max(num2, num3))
    # Consider a more pythonic way with less code:
    # if (num3 > num2 and num3 >num1):
    #     return num3
    # else:
    #     return max(num1, num2)


num1 = 124357
num2 = 43253
num3 = 522646356

print max(num1, num2)
print max_of_three(num1, num2, num3)
