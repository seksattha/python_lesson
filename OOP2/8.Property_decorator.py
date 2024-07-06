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
    @property
    def join_yy(self):
        return self.id[:2]

    @property
    def get_major(self):
        major_code = {
            '1': 'Engineer',
            '2': 'Scientist',
            '3': 'Architecture',
            '4': 'Accountance'
        }
        return major_code.get(self.id[2], 'Unknown Major')


if __name__ == '__main__':
    s = Student("5841234526","John", "Doe")
    print(s.full_name())
    print(s.full_name2)
    print(s.join_yy)
    print(s.get_major)