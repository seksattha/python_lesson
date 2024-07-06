class Student:
    def __init__(self, id, fname, lname):
        self.id = id
        self.fname = fname
        self.lname = lname
        # self.full_name = f'{self.fname} {self.lname}'

    def full_name(self):
        return f'{self.fname} {self.lname} '
    @property
    def full_name2(self):
        return f'{self.fname} {self.lname} '

if __name__ == '__main__':
    s = Student("123456789","John", "Doe")
    print(s.full_name())
    print(s.full_name2)