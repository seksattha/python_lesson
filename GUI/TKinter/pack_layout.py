from tkinter import *

root = Tk()
# pack จะเป็น geometry management สำหรับในการกำหนดตำแหน่งของ widget ต่างๆ
Button(root, text="Click me").pack(side = LEFT)
# แบบนี้จะกำหนดให้อยู่ทางด้านซ้าย side = LEFT

#หรือจะเขียนในรูปแบบนี้ก็ได้เหมือนกัน
b1 = Button(root, text="Open")
b1.pack(side=LEFT)

#ลองเขียนให้มันอยู่ด้านขวาบ้าง
Button(root, text = "Browse").pack(side = RIGHT)
root.mainloop()