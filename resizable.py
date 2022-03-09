
from tkinter import *

root = Tk()
root.geometry("350x200")
root.title("Resizable Window")
def resize() :
    root.geometry(f"{widthEntry.get()}x{heightEntry.get()}")

title = Label(root, text = "This is a Resizable Window" , font = "comicsansms 12 bold", fg = "Hotpink")
title.grid(row = 0, column = 2, columnspan = 2, padx = 4, pady = 4)

widthLabel = Label(root, text = "Enter new width")
widthLabel.grid(row = 2, column = 0, padx = 5 , pady = 5)

widthEntry = Entry(root)
widthEntry.grid(row = 2 , column = 2 , padx = 20, pady = 5)

heightLabel = Label(root, text = "Enter new height")
heightLabel.grid(row = 3, column = 0, padx = 5 , pady = 5)

heightEntry = Entry(root)
heightEntry.grid(row = 3 , column = 2 , padx = 20, pady = 5)

Button(root, text = "Apply changes", command= resize, activebackground = "yellow").grid(row = 4, column = 2 , padx = 10 , pady = 10)

root.mainloop()


