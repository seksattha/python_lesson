from tkinter import *

root = Tk()


#กำหนดปุ่มมาสองอัน
Button(root, text='male').grid(row=0, column = 0)
Button(root, text='female').grid(row=0, column = 1)

#ทำการสร้าง textvariable
tv_male = IntVar()
tv_female = IntVar()




root.mainloop()