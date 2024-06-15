# สามารถเอามาใช้งานกับ Class ได้เหมือนกันจะช่วยให้ IDE ทำงานได้ง่ายขึ้น

class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def foo(self):
        print("Bar")



def epsilon(a: Person, b):
    return a.fname
            