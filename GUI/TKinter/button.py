from tkinter import *

root = Tk()
root.option_add("*Font", "consolars 20")
Button(root, text="Open").pack() # เป็นการสร้างปุ่ม
# การกำหนดให้เป็น pack ที่จะเป็นการกำหนดให้แสดงผลจาก บนลงล่าง
Button(root, text="Click me ", bg= "orange").pack()
# จะเป็นการสร้าง ปุ่ม ที่มี พื้นหลังเป็นสีส้ม โดยการตั้งค่าจาก bg

Button(root, text = "Click me", bg='Black', fg=  'yellow').pack()
root.mainloop()