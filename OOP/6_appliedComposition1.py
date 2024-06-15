class Printer:
    def print_Page(self,data):
        print ("Printing....".format(data)) #ตรงนี้อีกตัวนึงที่ชอบพิมพ์ผิด ชอบไปใส่ self.data

class Scanner:
    def scan_Page(self):
        print("Scanning")

class Fax:
    def fax_Page(self,number):
        print(f"faxing to {number}")
class Aio:
    def __init__(self, p , s, f):
        self.f = f
        self.p = p
        self.s = s

if __name__ == '__main__':
    a = Aio(Printer(), Scanner(), Fax()) #ผ่าน Class printer และ Class scanner ผ่านตัวแปร p และ ตัวแปร s
    a.p.print_Page("hello World")
    a.s.scan_Page()
    a.f.fax_Page("09999999")

