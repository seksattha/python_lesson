from tkinter import *

root = Tk()


#ทำการสร้าง textvariable
tv_male = IntVar()
tv_female = IntVar()
tv_total  = IntVar()

#กำหนดปุ่มมาสองอัน
Button(root, text='male').grid(row=0, column = 0)
Button(root, text='female').grid(row=0, column = 1)









root.mainloop()