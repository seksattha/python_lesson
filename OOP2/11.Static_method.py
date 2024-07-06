class Student:
    def __init__(self, id, fname, lname, w,h):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.w = w
        self.h = h
    def __str__(self):
        return f'{self.fname} {self.lname}'

    def bmi(self):
        return self.w /(self.h /100) ** 2
    @staticmethod
    def kg_pound(kg):
        return kg* 2.24


if __name__ == '__main__':
    s1 = Student(123,"Robert", "Angier", 75, 185)
    print(s1)
    print(f'{s1.bmi():.2f}')
    print(Student.kg_pound(45))

