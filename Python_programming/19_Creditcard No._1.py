
def remove_nondigit(s):
    d = []
    d =[i for i in s if i.isdigit()]
    return d
def multiplybyTwoandOne(d):
    s = []
    for i in range(len(d)):
        if i % 2 == 0:
            s.append(int(d[i])*2)
        else:
            s.append(int(d[i]) * 1)

    return s

def printdigit(s):
    [print("{:^3}|".format(i), end ="") for i in s]
    print()

def moddigit(s):
    d = []
    for n in s:
        if n<10:
            d.append(n)
        else:
            d.append(((n//10) + (n % 10)))

    return dpy
def moddigitComp(s):
    return [n if n<10 else ((n//10) + (n%10)) for n in s]


if __name__ == '__main__':
    card = "4597 7692 1332 987"
    d = remove_nondigit(card)
    printdigit(d)
    s = multiplybyTwoandOne(d)
    printdigit(s)
    d = moddigitComp(s)
    printdigit(d)

    sum = sum(d)
    r = sum % 10
    check_digit = 0 if r==10 else 10-r
    print(f"sum:{sum} check digit = {check_digit}")