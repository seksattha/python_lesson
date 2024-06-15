import matplotlib.pyplot as plt
import numpy as np

def QC_plot(n):
    x = np.arange(n)
    data = np.random.randn(x.size)

    #Determination of mean and standard deviation
    m, sd = np.mean(data), np.std(data)

    #plotting scatter
    plt.plot(x,data,
             color = '0.7', alpha = 0.7,
             marker = 'o')
    # creating a filter
    filter = np.where((data > m + (2 * sd)) | (data < m - (2 * sd)) )
    plt.plot(x[filter], data[filter], color='pink', linestyle="", marker='o')

    #plotting average line.
    plt.axhline(m, linestyle = '--')




    #setting ucl (upper control line)
    ucl = 2 * sd
    lcl = -ucl
    plt.axhline(m+ucl, color = 'red', linestyle = '--')
    plt.axhline(m + lcl, color='red', linestyle='--')

    # Fill the banner
    plt.fill_between(x, m + ucl, m + 5 * sd, alpha= .3, color = 'red')
    plt.fill_between(x, m + lcl, m - 5 * sd, alpha=.3, color='red')
    #decoration
    plt.ylabel("weight (g) ")
    mytitle = "n = {}, {} = {:.2f}, sd ={:.2f}".format(n, r"$\bar{x}$", m, sd)
    plt.title(mytitle)


    plt.show()

if __name__ == '__main__':
    QC_plot(100)