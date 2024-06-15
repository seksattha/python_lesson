
def celcius_fah(celcious):
    return (celcious*(9/5))+32

def temperature_table():
    for c in range(0,100,1):
        f = celcius_fah(c)
        print("Faranheit = {} Celecious = {}".format(f,c))


if __name__ == '__main__':
    temperature_table()