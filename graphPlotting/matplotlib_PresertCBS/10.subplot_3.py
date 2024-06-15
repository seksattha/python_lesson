#suplot to grid

import matplotlib.pyplot as plt
import numpy as np

def demo1():
    fig = plt.figure()
    # 2 rows  5 columns
    ax1 = plt.subplot2grid((2,5), (0,0),
                           rowspan= 1, colspan=3)
    ax2= plt.subplot2grid((2, 5), (0, 3),
                           rowspan=1, colspan=2)

    ax3 = plt.subplot2grid((2, 5), (1, 0),
                           rowspan=1, colspan=5)

    plt.show()
def demo2():
    fig = plt.figure()
    # 2 rows  5 columns
    ax1 = plt.subplot2grid((2,6), (0,0),
                           rowspan= 2, colspan=4)
    ax2 = plt.subplot2grid((2, 6), (0, 4),
                           rowspan=1, colspan=2)
    ax3 = plt.subplot2grid((2, 6), (1, 4),
                           rowspan=1, colspan=2)

    plt.show()
if __name__ == '__main__':
    # demo1()
    demo2()