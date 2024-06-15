
def celcius_fah(celcious):
    return (celcious*(9/5))+32

def temperature_table():
    for c in range(0,100,1):
        f = celcius_fah(c)
        print("Faranheit = {} Celecious = {}".format(f,c))

def menu():
    print("1 Convert celcious to farenheit")
    print("2 Display temperature table")
    n = input("Your Choice?")
    if n == "1":
        celcious = float(input("Input temperature in celcious"))
        print(celcius_fah(celcious))
    elif n == "2":
        temperature_table()
if __name__ == '__main__':

    menu()