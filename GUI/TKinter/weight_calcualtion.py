from tkinter import  *

root = Tk()
#สร้าง textvariable
tv_kg = DoubleVar() #tv ย่อมาจาก Text variable
tv_lbs = DoubleVar()


ent_kg = Entry(root, textvariable=tv_kg).pack(side=LEFT)
Label(root, text= "kg." ).pack(side= LEFT)

Button(root, text= " Calculate").pack(side = LEFT)
lbl_lbs = Label(root, textvariable=tv_lbs).pack(side= LEFT)
root.mainloop()