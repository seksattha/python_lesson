# Returning multiple value from function, It will be store as tuple variable.
def price_with_vat(amount):
    vat = amount * 7/107
    price = amount - vat
    t = vat,price
    return t,type(t)
if __name__ == '__main__':
    print(price_with_vat(100))
    #It's obvious that t is tuple variable


