class Person:
    def __init__(self):
        self.fname = ""
        self.lanme = ""
        self.country = "Thailand" #กำหนดให้ defult เป็นประเทศไทย

if __name__ == '__main__':
    p1 = Person()   # Create new instance
    print(p1.country)
