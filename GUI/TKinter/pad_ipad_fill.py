from tkinter import *

# fill , padx, pady
#ipad
    # ipadx จะเป็นการกำหนดขนาดในแกน y
    # ipadx จะเป็นการกำหนดขนาดในแกน x


#pad
    #padx จะเป็นกำหนดระยะห่างในแต่ละ widget ในแกน x
    #pady จะเป็นกำหนดระยะห่างในแต่ละ widget ในแกน y
root = Tk()
Label(root, text="Mocha", bg = "red").pack(side= TOP, ipady = 20, ipadx  = 20 , pady = 20)
Label(root, text="Espresso", bg = "green").pack(side= TOP)
Label(root, text="Latte", bg = "blue").pack(side= TOP)
root.mainloop()