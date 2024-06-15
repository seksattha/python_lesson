# เรื่องนี้ไม่ได้เป็นเรื่องพิเศษอะไร ปกติเราเวลาที่จะรับค่า argument เข้ามาใน function จะต้องกำหนด
# แต่ถ้าจะรับค่าได้หลายๆ ค่าโดยที่ไม่ต้องกำหนด จะต้องใช้ *args args ก็คือหลายๆ argugment (เติมS)
# ซึ่งมันก็ไม่จำเป็นที่ต้องเป็นคำว่า args อาจจะเป็นชื่ออะไรก็ได้ตามที่เราต้องการเช่น data
# แต่สิ่งที่สำคัญที่สุดคือจะต้องมี *

def demo(*args):
    print(type(args))
    print(args)
    #ค่าที่เอามาเก็บก็จะเป็น tuple

def find_average(*values):
    # ไม่จำเป็นจะต้องเป็น args ก็ได้ เป็นอะไรก็ได้ตามที่เราต้องการ
    count = 0
    total = 0
    for i in values:
        total += i
        count = count + 1
    return total/count




if __name__ == '__main__':
    demo(1,3,5,7)
    average = find_average(1,3,5,7.56,78)
    print(average)

