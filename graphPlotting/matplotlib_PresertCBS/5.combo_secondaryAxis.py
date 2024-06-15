import matplotlib.pyplot as plt
import numpy as np

def combo1():
    monthLabels  = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
    x = np.arange(monthLabels.size)
    y = np.random.normal(80, 10, x.size)
    y2 = np.random.normal(95,10,x.size)

    fig, ax1 = plt.subplots()
    #setting secondary axis
    ax2 = ax1.twinx()

    #setting ticks
    plt.xticks(x,labels = monthLabels)
    #plotting bar graph
    ax1.bar(x, y,
            color = 'blueviolet', alpha = 0.7)
    ax1.set_ylabel("our company sales")
    ax1.tick_params('y', colors= 'blueviolet')
    ax1.set_ylabel("our companry", color = 'blueviolet')
    # plotting line graph
    ax2.plot(x, y2,
             marker = 'o', linestyle = '--',
             color = 'dodgerblue')

    #decoration
    ax2.tick_params('y', colors = 'dodgerblue')
    ax2.set_ylabel("industrail figure", color = 'dodgerblue')
    ax2.set_ylim(0)
    plt.show()

if __name__ == '__main__':
    combo1()