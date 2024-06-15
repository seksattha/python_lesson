# class ปกติที่ชอบสร้้างกันที่มี self อยู่ด้านหลังจะเรียกว่า instance method
class Student:
    def __init__(self, fname, lname, w_kg, h_cm):
        self.fname = fname
        self.lname = lname
        self.w_kg = w_kg    
        self.h_cm = h_cm

    def __str__(self):
        return "{} {}Kg. {}cm".format(self.fname, self.w_kg, self.h_cm)
    def bmi(self):   #แบบนี้จะเรียกว่า instance method
        return self.w_kg / (self.h_cm/100) ** 2

    @staticmethod #แบบนี้จะเรียกว่าเป็น static method มันจะไม่ได้ไปยุ่งอะไรกับตัวแปรใน Class เลย
    def kg_pound(kg):
        return kg * 2.20462

    @staticmethod
    def cm_inch(cm):
        return cm * .393701


if __name__ == '__main__':

    s = Student("Ronnie", "O'sullivan", 75,80)
    print(s.bmi())
    #เวลาที่จะเรียกใช้จะต้องเรียกใช้ผ่าน class เวลาที่จะใช้งาน static method
    print(Student.kg_pound(50))
    print(s)



