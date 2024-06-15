import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def demo1():
    # n = np.arange(10)
    # height = np.array(np.random.normal(170,10,n.size))
    # print('{}'.format(height))
    # weight = np.array(np.random.normal(70,5,height.size))
    x = [170, 165, 180, 155, 163, 160, 175]
    y = [80, 65, 75, 47, 50, 52, 74]

    plt.scatter(x,y)


    #linear regresssion
    slope, intercept, r, p, std_err = stats.linregress(x,y)
        #create a line
    # creat a tutple y1, y2
    l = slope * min(x) + intercept, slope * max(x) + intercept
    # l is tuple
    # plotting linear regression
    plt.plot([min(x), max(x)], l,
             color = 'orange', linestyle='--')
    print(slope, intercept, r, p, std_err)

    plt.xlabel("height (cm)")
    plt.ylabel("weight (kg)")

    #"String Formatting for Titles"
    # mytitle = "y = {:.2f}x + {:.2f}  r^2 = {:.4f}, p ={:.4}".format(slope, intercept, r**2, p)
    #using LaTex formatting
    mytitle = r"${} = {:.2f}x + {:.2f}  r^2 = {:.4f}, p ={:.4}$".format(r"\^{y}",slope, intercept, r ** 2, p)
    plt.title(mytitle)
    plt.show()

if __name__ == '__main__':
    demo1()