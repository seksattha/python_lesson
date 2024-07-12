from tkinter import *

# fill , padx, pady

# ipadx จะเป็นการกำหนดขนาดในแกน y
# ipadx จะเป็นการกำหนดขนาดในแกน x
root = Tk()
Label(root, text="Mocha", bg = "red").pack(side= TOP, ipady = 20, ipadx  = 20)
Label(root, text="Espresso", bg = "green").pack(side= TOP)
Label(root, text="Latte", bg = "blue").pack(side= TOP)
root.mainloop()