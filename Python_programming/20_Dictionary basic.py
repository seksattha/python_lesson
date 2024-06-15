# จะมองว่าเป็นพจจนานุกรม ก็ได้
# หลักการสำคัญของมันจริงคือการใช้ key value pair
# {} จะใช้วงเล็บปีกกา

def demo():
        # key       value
    d = {"Hello": "สวัสดี","Thank":"ขอบคุณ","Toilet":"ห้องน้ำ"}
    print(d['Hello'])
    #จะอ้างด้วยตัว key ไม่เหมือนกับ tuple หรือว่า list
    #ที่จะอ้างอิงด้วย index

    #การเพิ่มข้อมูลเข้าไปใน dictionary
    d["one"] = "หนึ่ง"
    print(d)
    #การลบข้อมูล
    del d["Toilet"]
    print(d)

def demo2():
    #สามารถเอา list มาใช้งานใน dictionary ได้
    m = {"th":[5, 3, 7],
         "sg":[3, 2, 1]}
    print(m)
    print(m["th"])
    print(m["th"][0])
    print(m["th"][0] + m["th"][1] + m["th"][2])
if __name__ == '__main__':
    demo2()