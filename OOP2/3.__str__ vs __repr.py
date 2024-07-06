class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.silver = silver
        self.gold = gold
        self.bronze = bronze

    def total(self): # instance method
        return self.gold + self.silver + self.bronze

    def __str__(self):
        return f'country => {self.country:>3} gold: {self.gold:>3} silver: {self.silver:3} bronze: {self.bronze:3}'
if __name__ == '__main__':
    th = Medal("Thailand", 5, 6, 10 )
    print(th)
    #เขียนแบบนี้ จะไม่สดวกเวลาใช้งานจริง
    print(th.country, th.gold, th.silver ,th.bronze)
    print(th.total())

    m = [
        Medal("Japan", 1,2 ,3),
        Medal('USA', 3, 7, 5),
        
    ]

    for  c in m:
        print(c)


    print(th)



