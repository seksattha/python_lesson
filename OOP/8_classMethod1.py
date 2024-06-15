# Class method มันทำให้้เราสามารถที่จะสร้าง constructor ได้หลายแบบ
class Eyeglasses:
    def __init__(self,eye, bridge, temple):
        self.eye = eye
        self.bridge = bridge    
        self.temple = temple
    @classmethod
    def of(cls,frame_string): #constructor
        #ต้องการให้ผู้ใช้ผ่านค่าเข้ามาเป็น string
        s = frame_string.split("-")
        return cls(int(s[0]), int(s[1]), int(s[2])) #เปลี่ยนค่าตัวแปร s ให้เป็น integer

    @staticmethod
    def gram_oz(g):
        return g * .035274

    def __str__(self):
        return "{}-{}-{}".format(self.eye, self.bridge, self.temple)


if __name__ == '__main__':
    f1 = Eyeglasses(55,16,140)
    print(f1)
    f2 = Eyeglasses.of("55-16-140") #เรียกใช้
    print(f2)
    "สังเกตุได้ว่าทั้ง f1 และ f2 จะได้ผลลัพธ์เหมือนกัน"
    print("*" * 40)
    print(f2.eye, f2.bridge, f2.temple)
    print(Eyeglasses.gram_oz(20))



