# %config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import numpy as np


def demo1():
    labels = ["China", "USA", "Germany", "Japan"]
    value = (3.5, 2, .5, 1.2)
    plt.pie(value, labels= labels,
            startangle = 90,
            autopct= "%1.2f%%",
            explode = (0,0,0.1,0))
    plt.show()

def demo2():
    labels = np.array(["China", "USA", "Germany", "Japan"])
    value = (3.5, 2, .5, 1.2)
    explode_setting = np.zeros(labels.size)
    explode_setting[np.where(labels == "Japan")] = 0.1
    plt.pie(np.sort(value), labels = labels, explode = explode_setting,
            startangle = 90,
            autopct= "%1.2f%%")

    plt.show()


def demo3():
    brandLabels = np.array(['Daikin', 'Mitsubishi', 'Haier', 'Carrier'])
    #value = np.random.uniform
    value = np.random.uniform(3,7, brandLabels.size)
    explode_setting = np.zeros(brandLabels.size)
    #explode_setting[np.where(brandLabels == 'Daikin')] = 0.1

    # exploding only second largest
    sortIndicies = np.argsort(value)
    second_largest_index = sortIndicies[-2]
    explode_setting[second_largest_index] = 0.1
    #Just checking the values
    print(sortIndicies)
    print(f'The second largest = {second_largest_index}')

    #ploting the pie graph
    plt.pie(value, labels = brandLabels, autopct = "%1.2f%%",
            explode = explode_setting,
            startangle = 90)
    plt.axis = "equal"
    plt.title(f'The second best selling brand = {brandLabels[second_largest_index]}',
              fontsize= 17,
              color = "Red")
    plt.show()



if __name__ == '__main__':
    # demo1()
    # demo2()

    demo3()