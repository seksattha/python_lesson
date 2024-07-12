from tkinter import *

root = Tk()
# pack จะเป็น geometry management สำหรับในการกำหนดตำแหน่งของ widget ต่างๆ
Button(root, text="Click me").pack(side = LEFT)
# แบบนี้จะกำหนดให้อยู่ทางด้านซ้าย side = LEFT

root.mainloop()