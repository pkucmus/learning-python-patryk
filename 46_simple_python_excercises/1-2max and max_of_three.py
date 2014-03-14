
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def max_of_three(num1, num2, num3):
    return max(num1, max(num2, num3))


num1 = 124357
num2 = 43253
num3 = 522646356

print max(num1, num2)
print max_of_three(num1, num2, num3)
