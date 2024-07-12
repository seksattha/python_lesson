from tkinter import  *


#ต่อมาจะต้องทำการสร้าง Function onclick สำหรับปุ่มกด
# โดยจะนำไปใช้งานที่ command = onclick ใน Button
def on_click():
    lbs = tv_kg.get() * 2.2 #สร้างตัวแปร lbs มารับค่าการคำณวณ
    tv_lbs.set(lbs) # ทำการกำหนดค่าให้ text variable tv_bls

root = Tk()
#สร้าง textvariable
tv_kg = DoubleVar() #tv ย่อมาจาก Text variable
tv_lbs = DoubleVar()


ent_kg = Entry(root, textvariable=tv_kg).pack(side=LEFT)
Label(root, text= "kg." ).pack(side= LEFT)

#จะเป็นการกำหนดว่าเมื่อกดปุ่มแล้วให้ทำอะไร โดยชื่อว่า on_click
Button(root, text= " Calculate", command=on_click).pack(side = LEFT)
lbl_lbs = Label(root, textvariable=tv_lbs).pack(side= LEFT)
root.mainloop()