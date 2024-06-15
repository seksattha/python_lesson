def demo():
   # แบบปกติ
    weight = [70,60,40]
    height = [170,175,161]

    bmi = []
    for i in range(len(weight)):
        bmi.append((weight[i]/(height[i]/100)**2))

    return bmi
def demo2():
    weight = [70, 60, 40]
    height = [170, 175, 161]

    bmi = []
    for w,h in zip(weight,height):
        bmi.append(w/((h/100)**2))
    return bmi

def demo3():
    #ลองเขียนแบบ list comprehension ดู
    weight = [70, 60, 40]
    height = [170, 175, 161]

    bmi = []
    bmi = [w/((h/100)**2) for w,h in zip(weight,height)]


    # หรือว่าเอาให้ย่อไปกว่า่นี้อีกด้วยการ return ค่าออกไปเลย
    return [w/(h/100)**2 for w,h in zip(weight,height)]

def demo4():
    #return ค่าแบบที่เป็น dictionary
    weight = [70, 60, 40]
    height = [170, 175, 161]
    name = ["John","Micheal","Peter"]
    return [{name:w/(h/100)**2} for w,h,name in zip(weight,height,name)]

def demo5():
    weight = [70, 60, 40]
    height = [170, 175, 161]
    name = ["John", "Micheal", "Peter"]
    gender = ["Male","Female","Male"]
    # ให้แสดงผลออกมาเฉพาะที่เป็นผู้ชาย
    return [{name: w / (h / 100) ** 2} for w, h, name,gender in zip(weight, height, name, gender) if gender =="Male"]


if __name__ == '__main__':
  a = demo()
  print(a)
  a = demo2()
  print(a)
  a = demo3()
  print(a)
  a = demo4()
  print(a)
  a = demo5()
  print(a)

