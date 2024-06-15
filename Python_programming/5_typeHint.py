# Variable in python is dynamic
# but sometimes we need to specific type of variable, passing into function.
from datetime import date


def alpha(a,b):
    c = a + b
    return c
def beta(a: str, b:int, c): #type hint
    print(a,b,c)

def gamma(a: date,b):
    print(a.year)
    print(b.year)

if __name__ == '__main__':
    print(alpha(5, 3))
    print(alpha("Dream", "Theater"))
    t1 = date(2022,10,12)
    print(gamma(t1,t1))