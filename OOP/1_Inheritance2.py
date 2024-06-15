#ที่นี้มาลองเพิ่มความสามารถของ class student
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
    def __init__(self, s_id, fname, lname):
        self.s_id = s_id
        self.lname = lname
        self.fname = fname
    def __str__(self):
        return "{} {}".format(self.s_id, super().__str__()) #คำสั่ง super ไปเอา __str__ ของ class แม่มาด้วย

class ExchangeStudent(Student):
    def __init__(self, partner_University, s_id, fname, lname)
        super().__init__(s_id, fname, lname) #เมื่อเทียบกับ ที่ของ student จะมีความซ้ำซ้อนมากกว่า
        self.partner_University = partner_University


if __name__ == '__main__':
    s1 =Student("1234","Ronnie","O' sullivan")
    print(s1)
