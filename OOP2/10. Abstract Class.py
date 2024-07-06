from abc import ABC, abstractmethod
class Member(ABC):
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "ID:{} {} {}".format(self.id, self.fname, self.lname)

    #พอเขียนถึงตรงนี้จะสร้าง instance จาก class member ไม่ได้อีกแล้ว
    @abstractmethod
    def discount(self):
        pass

class Gold(Member):
    def discount(self):
        return .1

class Silver(Member):
    def discount(self):
        return .05

if __name__ == '__main__':
    # m = Member("007", "James", "bond")
    # print(m)
    g = Gold("123","John", "Doe")
    print(g)
    print(g.discount())
    s = Silver("456","Jane", "Smith")
    print(s.discount())



