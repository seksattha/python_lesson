#จะเห็นว่า PersonV2 Class ค่อนค้างที่จะซ้ำซอน
# วิธีการก็คือจะสร้าง class ที่ชื่อว่า PersonName แล้วสร้าง Class ที่ชื่อ PersonV3 มาเรียกเอาข้อมูลไป
from datetime import date

class Person:
    def __init__(self,title, fname, lname, dob):
        self.dob = dob
        self.lname = lname
        self.fname = fname
        self.title = title

    def __str__(self):
        return f"{self.title} {self.fname} {self.lname}, {self.dob}"
class PersonV2:
    def __init__(self,title, fname, lname, thtitle, thfname, thlname,dob):
        self.dob = dob
        self.lname = lname
        self.fname = fname
        self.title = title
        self.thlname = thlname
        self.thfname = thfname
        self.thtitle = thtitle

    def __str__(self):
        return f"{self.title} {self.fname} {self.lname}" \
               f"\n{self.thtitle} {self.thfname} {self.thlname}, " \
               f"{self.dob}"

class PersonName:
    def __init__(self,fname, lname, dob):
        self.dob = dob
        self.lname = lname
        self.fname = fname
    def __str__(self):
        return f"{self.fname}{self.lname}{self.dob}"


class PersonV3:
    def __init__(self,nameEN, nameTH, dob):
        self.dob = dob
        self.nameTH = nameTH
        self.nameEN = nameEN
    def __str__(self):
        return f"{self.nameEN}\n{self.nameTH}\n{self.dob}"

if __name__ == '__main__':
    p1 = Person("Mr", "Ronnie", "O'Sullivan", date(1975,12,5))
    print(p1)
    print("*" * 40)

    p2 = PersonV2("Mr", "Ronnie", "O'Sullivan",
                  "นาย","รอนนี่","โอซุลลิแวน", date(1975, 12, 5))
    print(p2)
    print("*" * 40)

    p3 = PersonV3(PersonName("Mr", "Ronnie", "O'Sullivan"),
                  PersonName("นาย","รอนนี่","โอซุลลิแวน"),date(1975,12,5))
    print(p3)