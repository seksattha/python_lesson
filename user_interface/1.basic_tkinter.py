
from tkinter import messagebox
import  tkinter as tk

def show_message():
    messagebox.showinfo("message", 'Hello world')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('tkinter demo')

    button = tk.Button(root, text = "click me!", command=show_message)
    button.pack(padx=20, pady=20)


    root.mainloop()