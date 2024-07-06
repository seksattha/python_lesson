def immutable_demo():
    n= 5
    print(f' memory address = {id(n):10}  value = {n} ')
    n = n + 4
    print(f' memory address = {id(n):10}  value = {n} ')

    s = "Dream"
    print(f' memory address = {id(s):10}  value = {s} ')

    s = s + "Theater"
    print(f' memory address = {id(s):10}  value = {s} ')

    # int และ string จะเป็น immutable

def mutable_demo():
    # object ที่สร้างมาจาก class ต่างๆ จะเป็น mutable
    #string ที่เก็บอยู่ใน list
    p = ["peter"]
    print(f'{id(p)} {p}')
    p[0] = "Spiderman"
    print(f'{id(p)} {p}')

class Contact:
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return f'id_self{id(self)} {self.name} {self.phone}'


if __name__ == '__main__':
    # immutable_demo()
    # mutable_demo()
    a = Contact("John", "1234567")
    print(a)
    a.phone = 999999999
    print(a)
    #ถึงจะมีการเปลี่ยนแปลงอย่างไร pointer ก็ยังเก็บอยู่ในหน่วยความจำที่เดิม
    b =a
    print(b)
    b.phone = "7777777777"
    print(a,b)