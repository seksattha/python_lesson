import matplotlib.pyplot as plt
import numpy as np

def demo():
    x = range(4)
    y = np.random.randint(20,40,len(x))

    avg = sum(y) / 4
    print(f'average = {avg}')

    labels = ("Mistubishi", "Daikin", "Samsung", "LG")

    plt.xticks(x, labels,)
    #plotting bar graph
    plt.bar(x,y)

    #plotting average line
    plt.axhline(avg, color="orange", linestyle= "--")

    #Decoration
    plt.title("Air conditioner sales", color='gray', fontsize= 17)
    plt.ylabel("sale qty")
    plt.show()


if __name__ == '__main__':
    demo()
