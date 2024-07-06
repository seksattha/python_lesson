from abc import ABC
class Member(ABC):
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "ID:{} {} {}".format(self.id, self.fname, self.lname)

class Gold(Member):
    pass

class Silver(Member):
    pass

if __name__ == '__main__':
    m = Member("007", "James", "bond")
    print(m)
    g = Gold("123","John", "Doe")
    print(g)



