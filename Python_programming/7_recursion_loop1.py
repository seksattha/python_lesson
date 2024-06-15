# recusion is a technique where the fucntion calls it self

def print_number(s):
    if s > 0:
        print_number(s-1)
        print(s)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def permutation(n, r):
    if r == 0:
        return 1
    else:
        return n * permutation(n - 1, r - 1)

def combination(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)

if __name__ == '__main__':
    # print_number(5)
    print(factorial(4))
    print(permutation(5, 3))
    print(combination(5, 3))

