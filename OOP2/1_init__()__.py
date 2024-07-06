class Person:
    def __init__(self):
        self.fname = ""
        self.lanme = ""
        self.country = "Thailand" #กำหนดให้ defult เป็นประเทศไทย

class Person2:
    def __init__(self, fname, lname, country):
        self.fname = fname
        self.lname = lname
        self.country = country

class Medal:
    def __init__(self, country, gold, silver , bronze):
        self.country = country
        self.bronze = bronze
        self.silver = silver
        self.gold = gold

    def total(self): # instance method
        return self.gold + self.silver + self.bronze

    def dummy(self , a, b):
        return  a + b

class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi_calc(self): #instance method
        return self.weight / (self.height/100) ** 2

    def bmi_cat(self):
        if self.bmi_calc() < 18.5:
            text  = "ต่ำกว่าเกณฑ์"
        elif 18.5 <= self.bmi_calc() <= 25:
            text = "ตามเกณฑ์"
        elif 25 <= self.bmi_calc() <= 30:
            text = "เกินเกณฑ์"
        elif self.bmi_calc() > 30:
            text = "อ้วน"
        return text


    

if __name__ == '__main__':
    # p1 = Person()   # Create new instance
    # print(p1.country)
    #
    # p1 = Person2()
    # print(p1)

    th = Medal('Thailand', 5, 3, 2)
    print(th.country)
    print(th.gold)
    print(th.silver)
    print(th.bronze)
    print(th.total())
    # เครื่องจะทำการเปลี่ยน code ไปเป็นแบบนี้
    print(Medal.total(th))

    print(th.dummy(2,3))

    a = Bmi(70, 174)
    print(a.bmi_calc())
    print(a.bmi_cat())