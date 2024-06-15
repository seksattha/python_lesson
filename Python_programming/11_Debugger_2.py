import random


def demo():
    for i in range(1000):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        total = d1 + d2
        print("{:>4} {} + {} = {:>2}".format(i+1,d1,d2,total))

demo()