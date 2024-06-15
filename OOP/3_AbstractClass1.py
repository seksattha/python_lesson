#ลองสร้าง class แบบปกติขึ้นมาก่อน
class Member:
    def __init__(self,m_id, fname, lname):
        self.lname = lname
        self.fname = fname
        self.m_id = m_id

    def __str__(self):
        # return f"{self.fname} {self.lname} {self.m_id}"
        return "Member:{} {} {}".format(self.m_id, self.fname, self.lname)
        "กด ALT ค้างไว้แล้วไปคลิกที่ข้างหน้า จะเติม text ได้พร้อมกันทีเดียว 3 อันเลย"

class Gold(Member):
    pass
class Silver(Member):
    pass

if __name__ == '__main__':
    m = Member("007", "James", "Bond")
    print(m)

    g = Gold("123", "John", "Doe")
    print(g)