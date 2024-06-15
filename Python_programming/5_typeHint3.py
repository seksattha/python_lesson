# using this symbol -> , telling type of variable returning from function


def bar(a,b) -> str:
    c = a + b
    return c

if __name__ == '__main__':
    x = bar(1,3.2)
    print("{} {}".format(x,type(x)))