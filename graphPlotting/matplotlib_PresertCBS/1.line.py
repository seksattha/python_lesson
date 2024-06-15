import matplotlib.pyplot as plt
import numpy as np
def demo():
    x = range(2017,2022)
    y = [25,18,32,8,43]

    plt.plot(x,y)
    plt.show()

def demo1():
    x = np.array(range(2014,2021))
    y = np.random.normal(10,30,x.size)
    plt.plot(x[:4], y[:4], color = 'blue',
             label = 'actual')
    plt.plot(x[3:], y[3:], color='red', linestyle = "--",
             label = 'forcast')

    plt.ylabel("Sales")
    plt.title("Example Line Graph")
    plt.legend()
    plt.show()


demo1()