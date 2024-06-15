class Person:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname
    def __str__(self):
        return "First Name:{} Surname:{} ".format(self.fname,self.lname)

" Person Class"
#จะเป็น super class หรือที่เรียกว่า "คลาสแม่"


" Student Class"
#จะเป็น sub class หรือที่เรียกว่า "คลาสลูก"
class Student(Person):
    pass #คือเอาไปคุณสมบัติ หรือว่า ความสามารถทั้งหมดของ class แม่มาหมดเลย



if __name__ == '__main__':
    s1 =Student("Ronnie","O' sullivan")
    print(s1)
