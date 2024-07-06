class Person:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname.strip().title()
    @property
    def blood(self):
        return self.__blood # ต้องเขียนแบบนี้เป็น syntax จะเป้นการ mangled name ทำให้มันเป็น private

    @blood.setter
    def blood(self, blood):
        if blood.upper() in ['A', 'B', 'AB', 'O']:
            self.__blood = blood.upper()
        else:
            raise ValueError("invalid blood group")

    def __str__(self):
        return f'{self.blood} {self.fname} {self.lname}'

if __name__ == '__main__':
    p1 = Person("John", "Doe", 'A')
    print(p1)
    p1.blood = 'o'
    print(p1)
    p1.fname = 'smith'
    print(p1)

