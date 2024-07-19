import re



class Box:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w):
        if(w > 0):
            self.__w = w
        else:
            raise ValueError("ค่าต้องมากกว่า 0 เท่านั้น")

    def volume(self):
        return self.w * self.h * self.d
class ContactV1:
    def __init__(self, fname, lname, phoneNum):
        self.fname = fname
        self.lname = lname
        self.phoneNum = phoneNum

    def __str__(self):
        return f'ชื่อ: {self.fname} นามสกุล: {self.lname} เบอร์มือถือ: {self.phoneNum}'

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname):
        self.__fname = fname.title().strip()

    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname):
        self.__lname = lname.strip().title()

    @property
    def phoneNum(self):
        return self.__phoneNum
    @phoneNum.setter
    def phoneNum(self, phoneNum):
        self.__phoneNum = re.sub(r'\D', "", phoneNum)

class CreditCard:
    def __init__(self, customer, bank, account, limit):
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        # setting initial value of balance equal to 0
        self.balance = 0

    def charge(self, price):
        if (price + self.balance > self.limit):
            print("วงเกินของคุณไม่เพียงพอ")
            return False
        else:
            self.balance = self.balance + price
            print(f'{self.balance}')
            return True
    def make_payment(self, amount):
        if (amount < (self.balance * 10)/100):
            print("ชำระไม่ถึงยอดขั้นต่ำ")
        else:
            self.balance = self.balance - amount
            print(f'วงเงินคงเหลือ :{self.limit - self.balance}' )


if __name__ == '__main__':
    def demo1():
        aBox = Box(40, 10, 6)
        try:
            print(aBox.w)
        except:
            raise ValueError("Error")
        print(aBox.volume())
    def demo2():
        c1 = ContactV1('JoHn','DOE', '091-123-4567')
        print(c1)
    def demo3():
        c1 = CreditCard("John Doe", 'Kbank', "123 456", 10000)
        c1.charge(5000)
        c1.charge(3000)
        print(c1.balance)
        c1.make_payment(7000)



    # demo1()
    demo3()


