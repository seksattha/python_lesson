import tkinter as tk # import tkinter แล้วทำการตั้งชื่อว่า tk

root = tk.Tk()             #คำว่า root จะเป้นอะไรก็ได้ main windows หรืออะไรก็ได้
root.option_add("*Font" ,"consolars 20 ") # เป็นการตั้งค่าทั้งหมด
root.title("Tkinter Example") # กำหนด title
tk.Label(root, text="Hello World").grid() #
root.mainloop()

# พื้นฐานก็เขียนเท่านี้ก็พอ
