class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi_calc(self): #instance method
        return self.weight / (self.height/100) ** 2

    def bmi_cat(self):
        if self.bmi_calc() < 18.5:
            text  = "ต่ำกว่าเกณฑ์"
        elif 18.5 <= self.bmi_calc() <= 25:
            text = "ตามเกณฑ์"
        elif 25 <= self.bmi_calc() <= 30:
            text = "เกินเกณฑ์"
        elif self.bmi_calc() > 30:
            text = "อ้วน"
        return text

    def __str__(self):
        return f'{self.bmi_calc():.2f} {self.bmi_cat()}'

#ลองทำเล่นๆ ดูว่าถ้าเราสร้าง class person ขึ้นมา โดยให้มี BMI ด้วย


class Person:
    def __init__(self, fname, lname, weight, height):
        self.fname = fname
        self.lname = lname
        self.weight = weight
        self.height = height
        self.bmi = Bmi(weight,height) #การทำแบบนี้เรียกว่า composition

    def get_bmi(self):
        return self.bmi.bmi_cat()

    def __str__(self):
        return f'Name : {self.fname:} {self.lname} bmi_status = {self.bmi.bmi_cat()}'


if __name__ == '__main__':
    a = Bmi(70, 174)
    print(a.bmi_calc())
    print(a.bmi_cat())
    print(a)

    p1 = Person('John', 'Doe', 120, 170)
    print(p1)