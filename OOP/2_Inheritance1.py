#มาลองดูในตัวอย่างที่มีการแก้ไข ข้อมูลที่อยู่ใน Class แม่
# class ลูกทั้งหมดก็จะได้อานิสงค์ไปด้วย นี่แหละคือข้อดีข้อคุณสมบัติในการสืบทอดไปด้วย
class Person:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname.strip().title() #แก้ไขตรงนี้

    def __str__(self):
        return "ชื่อ:{!r} นามสกุล:{!r} ".format(self.fname,self.lname)

" Person Class"
#จะเป็น super class หรือที่เรียกว่า "คลาสแม่"


" Student Class"
#จะเป็น sub class หรือที่เรียกว่า "คลาสลูก"
class Student(Person):
    def __init__(self, s_id, fname, lname):
        super().__init__(fname, lname)
        self.s_id = s_id

    def __str__(self):
        return "รหัส:{} {}".format(self.s_id, super().__str__()) #คำสั่ง super ไปเอา __str__ ของ class แม่มาด้วย

class ExchangeStudent(Student):
    def __init__(self,  s_id, fname, lname, partner_University):
        super().__init__(s_id, fname, lname) #เมื่อเทียบกับ ที่ของ student จะมีความซ้ำซ้อนมากกว่า
        self.partner_University = partner_University
    def __str__(self):
        return "{} มหาลัย{} ".format(super().__str__(),self.partner_University)


if __name__ == '__main__':
    s1 =Student("1234","Ronnie","O' sullivan")
    print(s1)
    s2 = ExchangeStudent("1234","John  ", "Doe","Harvard")
    print(s2)
    p1 = Person(" John","Higgins")
    print(p1)
