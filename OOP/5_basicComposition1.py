#ในกรณีที่เราจะต้องการเพิ่ม ข้อมูลที่เป็นชื่อภาษาไทยด้วย

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
if __name__ == '__main__':
    p1 = Person("Mr", "Ronnie", "O'Sullivan", date(1975,12,5))
    print(p1)
    p2 = PersonV2("Mr", "Ronnie", "O'Sullivan",
                  "นาย","รอนนี่","โอซุลลิแวน", date(1975, 12, 5))
    print(p2)
        