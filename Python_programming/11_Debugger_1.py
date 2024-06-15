import random


def sum_digit(n):
    s = str(n)
    total = 0
    for i in s:
        total = total + int(i)

    return total
#step out is ised for getting out of loop


def dice():
    for i in range(10):
        n = random.randint(1,6)
        print(n)


# Apperantly, step mycode is only your code, not any module we are calling.
#Step into mycode will not go though imported function called "random"

# print(sum_digit(12345))
# dice()

a=sum_digit(12345)
b=sum_digit(5678)
print(a+b)