import matplotlib.pyplot as plt
import numpy as np

# คิดว่าเขียนแบบนี้เหมาะเขียนแบบในตัวอย่างแรก subplot_1

def demo2():
    fig, axes = plt.subplots(2,1)
    # this function will return array
    print('type of ax = {} size = {}'.format(type(axes) ,axes.shape))

    axes[0].plot([3,5,7,1])
    axes[1].bar(np.arange(4), [3,5,7,1] )
    plt.show()

def demo3():
    fig, axes = plt.subplots(2,3, sharex=True)
    # this function will return array
    print('type of ax = {} size = {}'.format(type(axes) ,axes.shape))

    for row in range(axes.shape[0]):
        for column in range(axes.shape[1]):
            axes[row, column].plot(np.random.randint(1,11,5))
            axes[row,column].set_title('ax[{},{}]'.format(row, column))

    plt.show()

if __name__ == '__main__':
    # demo2()
    demo3()