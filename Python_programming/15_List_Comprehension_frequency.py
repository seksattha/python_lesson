import random


def mulidim_list():
    medals = [['th', 3, 5, 2],
              ['KR', 3, 5, 2],
              ['JP', 20, 30, 40]]




    a = [sum(m[1:]) for m in medals]
    print(a)
    b = [(m[0], sum(m[1:])) for m in medals]
    print(b)
    # การใช้ sum(m[1:]) หมายถึงเอาตั้งแต่ index ตัวที่ 1 เป็นต้นไปแต่ถ้าเราพิพม์เป็น sum(m[2:) จะนับตั้งแต่ index
    #ตัวที่ 2 เป็นต้นไป
    c = [(m[0], m[1], m[2], m[3]) for m in medals]
    print(c)
    # จะเห็นได้ว่าเขียนโปรแกรมแบบ list comprehension แล้วโค้ดจะสั้นมากๆ
    # ทีนี้มาลองเปรียบเทียบดูว่ากับ list ปกติจะเป็นอย่างไร
    d = []
    for m in medals:
        d.append((m[0],m[1],m[2],m[3]))
    print(d)

def freq():
    flowers = ['ivy','iris','rose','lilly','jasmine']
    choice = [random.choice(flowers) for i in range(10)]
    print(choice)

    f = [(i,choice.count(i)) for i in set(choice)]
    #set methode is the same as remove duplicate.
    print(f)
if __name__ == '__main__':
    freq()