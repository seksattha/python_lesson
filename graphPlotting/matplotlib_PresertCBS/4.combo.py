import matplotlib.pyplot as plt
import numpy as np

def combo1():
    monthLabels  = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
    x = np.arange(monthLabels.size)
    y = np.random.normal(80, 10, x.size)
    y2 = np.random.normal(95,10,x.size)

    plt.xticks(x,labels=monthLabels)
    # plotting bar graph
    plt.bar(x,y,
            color = 'Orange', alpha = 0.7,
            label ='we')
    #plotting line graph
    plt.plot(x,y2,
             color='blue', marker = 'o',
             label = 'industry')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    combo1()
