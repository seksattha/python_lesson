class Medel:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.silver = silver
        self.gold = gold
        self.bronze = bronze

    def total(self): # instance method
        return self.gold + self.silver + self.bronze

    def __str__(self):
        return f'country => {self.country:>3} gold: {self.gold} silver: {self.silver} bronze: {self.bronze}'
if __name__ == '__main__':
    th = Medel("Thailand", 5, 6, 10 )
    print(th)
    #เขียนแบบนี้ จะไม่สดวกเวลาใช้งานจริง
    print(th.country, th.gold, th.silver ,th.bronze)
    print(th.total())


    print(th)



