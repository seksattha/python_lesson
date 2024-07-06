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


if __name__ == '__main__':
    # p1 = Person()   # Create new instance
    # print(p1.country)
    #
    # p1 = Person2()
    # print(p1)

    th = Medal('Thailand', 5, 3, 2)
    print(th)