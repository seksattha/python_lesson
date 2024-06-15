from itertools import cycle


def demo1():
    #ทีนี้ปัญหาจะเกิดขึ้นทันทีถ้าข้อมูลมัน มันไม่เท่ากัน
    weight = [70, 60, 40,50] #
    height = [170, 175, 161]

    return [w/((h/100)**2) for w,h in zip(weight,height)]
    #มันจะส่งค่ากลับมาแค่ 3 ตัว
def demo2():
    #วิธีการแก้คือการใช้ recycle ที่ตัวแปร height
    weight = [70, 60, 40,50,55] #
    height = [170, 175, 161]

    # return [w/((h/100)**2) for w,h in zip(weight,cycle(height))]
    #มันจะส่งค่ากลับมาแค่ 3 ตัว

    #ทีนี้มาลองดูกันว่า w, h ข้างในเป็นอย่างไร
    [print(w,h) for w,h in zip(weight, height)]
    print("*"*40)
    #จะเห็นได้ว่ามันเอามาแค่ 3 ตัว
    [print(w,h) for w,h in zip(weight, cycle(height))]
    # มันจะไปวนตัวแรกมาใหม่เหมือนชื่อของมัน cycle

def demo3():
    weight = [70, 60, 40, 50]  #
    height = [170, 175, 161]

    z = zip(weight, height) # Generator
    print(z)
    print(next(z))
    print(next(z))
    print(next(z))
    print(next(z))
    #จะแสดงผลลัพธ์ออกมาเป็นคู่ๆ





if __name__ == '__main__':
    print(demo1())
    print(demo2())
    demo3()
