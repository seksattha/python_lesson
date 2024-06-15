#จะต้องสร้าง methode discount ใน class ที่ได้ทำการสืบทอดด้วย

#เป็นตัวช่วยของ Editor โดยการใช้ Ctrl + O (Oscar) เพื่อที่ทำให้การเลือก method ที่จะมาใช้ในการ override

#เพราะว่าถ้าไม่มีการ Override จะไม่สามมารถที่จะสร้าง instance จาก class นั้นได้
from abc import ABC ,abstractmethod #ทำการ import Abstract base class และเพิ่ม static method
class Member(ABC): #กำหนด Member ให้เป็น abstact class
    def __init__(self,m_id, fname, lname):
        self.lname = lname
        self.fname = fname
        self.m_id = m_id

    def __str__(self):
        # return f"{self.fname} {self.lname} {self.m_id}"
        return "Member:{} {} {}".format(self.m_id, self.fname, self.lname)
        "กด ALT ค้างไว้แล้วไปคลิกที่ข้างหน้า จะเติม text ได้พร้อมกันทีเดียว  อันเลย"

    def fullname(self):  # ไม่จำเป็นว่าจะต้องเป็น metode ที่เป็น abstract ทั้งหมดก็ได้
        return f"{self.fname} {self.lname}"

    @abstractmethod
    def discount(self):
        pass
class Gold(Member):
    def discount(self):
        return 0.1

class Silver(Member):

    def discount(self):
        return  0.05


if __name__ == '__main__':
    # m = Member("007", "James", "Bond")
    # print(m)

    g = Gold("123", "John", "Doe")
    print(g)
    print(g.discount())
    print(g.fullname())

    s = Silver("777","Jane", "Smith")
    print(s.m_id)
    print(s.fullname())
    print(s.discount())