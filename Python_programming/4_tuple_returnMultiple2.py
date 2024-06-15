# Returning multiple value from function, It will be store as tuple variable.
def price_with_vat(amount):
    vat = amount * 7/107
    price = amount - vat
    t = vat,price
    return t

if __name__ == '__main__':
    print(price_with_vat(100))
    a = price_with_vat(200)
    print(a)
    print(type(a))
    print("price = ",a[0])
    print("Vat = ",a[1])

    p,v = price_with_vat(200)
    print(p)
    print(v)

# สามารถที่เรียกค่าใน Tuple มาใช้งานได้หลายๆ แบบ