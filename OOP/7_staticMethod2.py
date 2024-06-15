# แล้วที่นี่เวลาที่จะใช้งาน static method ก็สามารถที่จะเอามาใช้งานโดยการเียกใช้ผ่าน class ได้
# หรือ่ว่าจะเอามาใช้ methode อันอื่นๆ ก็ได้ลองดูใน __str__(self)


#สิ่งที่จะสำคัญก็คือ staticmethode จะไม่สามารถเข้าถึง attribute ของ class ได้
class Student:
    def __init__(self, fname, lname, w_kg, h_cm):
        self.fname = fname
        self.lname = lname
        self.w_kg = w_kg    
        self.h_cm = h_cm

    def __str__(self):
        return "{} {}Kg({:.1f}) pound. {}cm({:.1f}) inches".format(self.fname, self.w_kg,self.kg_pound(self.w_kg), self.h_cm,self.cm_inch(self.h_cm)) #เอาstatic method มาเรียกใช้งานในนี้ก็ได้
    def bmi(self):   #แบบนี้จะเรียกว่า instance method
        return self.w_kg / (self.h_cm/100) ** 2

    @staticmethod #แบบนี้จะเรียกว่าเป็น static method มันจะไม่ได้ไปยุ่งอะไรกับตัวแปรใน Class เลย
    def kg_pound(kg):
        return kg * 2.20462

    @staticmethod
    def cm_inch(cm):
        return cm * .393701


if __name__ == '__main__':

    s = Student("Ronnie", "O'sullivan", 75,180)
    print(s.bmi())
    #เวลาที่จะเรียกใช้จะต้องเรียกใช้ผ่าน class เวลาที่จะใช้งาน static method
    print(Student.kg_pound(50))
    print(s)



