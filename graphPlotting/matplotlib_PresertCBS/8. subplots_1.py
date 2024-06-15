import matplotlib.pyplot as plt

def demo1():
    plt.plot([1,2,3,4], [1,2,3,4])
    plt.show()

def demo2():
    fig = plt.figure()
    # 1 row 2 columns figure 1
    fig.add_subplot(121)
    plt.plot([3, 5, 7, 1])
    # 1 row 2 columns figure 2
    fig.add_subplot(122)
    plt.bar(range(4),[3, 5, 7, 1])

def demo3():
    fig = plt.figure()
    # 1 row 2 columns figure 1
    fig.add_subplot(211)
    plt.plot([3, 5, 7, 1])
    # 1 row 2 columns figure 2
    fig.add_subplot(212)
    plt.bar(range(4), [3, 5, 7, 1])
    plt.show()
def demo4():
    fig = plt.figure()
    # 1 row 2 columns figure 1
    fig.add_subplot(221)
    plt.plot([3, 5, 7, 1])
    # 1 row 2 columns figure 2
    fig.add_subplot(222)
    plt.bar(range(4), [3, 5, 7, 1])
    fig.add_subplot(223)
    plt.scatter(range(4), [3, 5, 7, 1])
    plt.show()
def demo5():
    fig = plt.figure()
    # 1 row 2 columns figure 1
    fig.add_subplot(221)
    plt.plot([3, 5, 7, 1])
    # 1 row 2 columns figure 2
    fig.add_subplot(222)
    plt.bar(range(4), [3, 5, 7, 1])
    fig.add_subplot(212)
    plt.scatter(range(4), [3, 5, 7, 1])
    plt.show()


if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    demo5()