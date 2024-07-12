from tkinter import *

root = Tk()

male_count = 0
female_count = 0
totol_count = 0
def male_click():
    global male_count,totol_count
    male_count = male_count + 1
    totol_count = totol_count + 1
    tv_male.set(male_count)
    tv_total.set(totol_count)

#ทำการสร้าง textvariable
tv_male = IntVar()
tv_female = IntVar()
tv_total  = IntVar()

#กำหนดปุ่มมาสองอัน
Button(root, text='male', command=male_click).grid(row=0, column = 0)
Button(root, text='female').grid(row=0, column = 1)

Label(root, textvariable=tv_male).grid(row = 1, column = 0)
Label(root, textvariable=tv_female).grid(row = 1, column = 1)

Label(root, textvariable=tv_total).grid(row = 2, columnspan = 1)





root.mainloop()