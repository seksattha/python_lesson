from tkinter import  *

root = Tk()
tv_kg = DoubleVar
ent_kg = Entry(root, textvariable=tv_kg).pack(side=LEFT)
Label(root, text= "kg." ).pack(side= LEFT)

Button(root, text= " Calculate").pack(side = LEFT)
lbl_lbs = Label(root).pack(side= LEFT)
root.mainloop()