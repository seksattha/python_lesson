from datetime import  date
class Person:
    def  __init__(self, fname, lname, dob):
        self.dob = dob
        self.lname = lname
        self.fname = fname

    def age(self): #instance methode
        today = date.today()
        return today.year - self.dob.year
    def __str__(self):
        # return f'name: {self.fname} surname {self.lname} age:{self.age()} years'
        a = vars(self)
        print(a)
        return ""

if __name__ == '__main__':
    p = Person('Ronnie', 'O Sullivan', date(1975, 12 ,5))
    print(p)
