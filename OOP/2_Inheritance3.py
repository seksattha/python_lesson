#มาลองดูในตัวอย่างที่มีการแก้ไข ข้อมูลที่อยู่ใน Class แม่
# class ลูกทั้งหมดก็จะได้อานิสงค์ไปด้วย นี่แหละคือข้อดีข้อคุณสมบัติในการสืบทอดไปด้วย
import re


#และเพิ่ม attribute สำหรับเก็บข้อมูลเรื่องเพศไปด้วย แต่ก็ต้องไปเติมที่ class ลูกที่เอาไปใช้งานด้วย

#มีการเพิ่ม Method สำหรับเอาที่ไม่ใช่ตัวเลขในรหัศนักศึกษาออก โดยการสร้างใน class student
#เป็น staticmethod แล้วเอามาใช้ที่ class student

class Person:
    def __init__(self, fname, lname, sex): 
        self.lname = lname
        self.fname = fname.strip().title() #แก้ไขตรงนี้
        self.sex = sex

    def __str__(self):
        return "ชื่อ:{!r} นามสกุล:{!r} เพศ{}".format(self.fname,self.lname,self.sex)

" Person Class"
#จะเป็น super class หรือที่เรียกว่า "คลาสแม่"


" Student Class"
#จะเป็น sub class หรือที่เรียกว่า "คลาสลูก"
class Student(Person):
    def __init__(self, s_id, fname, lname, sex):
        super().__init__(fname, lname, sex)
        self.s_id = self.remove_non_digit(s_id)

    def __str__(self):
        return "รหัส:{} {}".format(self.s_id, super().__str__()) #คำสั่ง super ไปเอา __str__ ของ class แม่มาด้วย

    @staticmethod
    def remove_non_digit(s):
        return re.sub(r"[\D]", "", s.strip())

class ExchangeStudent(Student):
    def __init__(self,  s_id, fname, lname,sex, partner_University):
        super().__init__(s_id, fname, lname,sex) #เมื่อเทียบกับ ที่ของ student จะมีความซ้ำซ้อนมากกว่า
        self.partner_University = partner_University
    def __str__(self):
        return "{} มหาลัย{} ".format(super().__str__(),self.partner_University)


if __name__ == '__main__':
    s1 =Student("12 34","Ronnie","O' sullivan","Female")
    print(s1)
    s2 = ExchangeStudent("123-(4)","John  ", "Doe","Female","Harvard")
    print(s2)
    p1 = Person(" John","Higgins","Female")
    print(p1)
