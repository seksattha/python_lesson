class Wallet:
    def __init__(self):
        self.amount = 0

    def earn(self, a):
        self.amount = self.amount + a

    def spend(self, a):
        self.amount = self.amount - a

    def __str__(self):
        return f'balance = {self.amount}'

if __name__ == '__main__':
    dad = Wallet()
    dad.earn(100)
    dad.spend(23)
    print(dad)

    mom = dad # ใช้เงินจากกระเป๋าเดียวก
    print(mom is dad)

    print(f'moms wallet amont {mom}')
    mom.spend(200)
    print(dad)
    #พอทำหนดให้เท่ากันแล้ว จะอยุ่ใน memory ตำแหน่งเดียวกันเลย
    print(f'{id(mom)} {id(dad)}')
