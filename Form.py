from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Tkinter GUI --> Shlok ")
root.config(bg = "cyan")
def validateName() :
    name = namevalue.get()
    msg = ''
    if len(name) == 0:
        msg = 'Name can\'t be empty'
    else:
        try:
            # if any(ch.isdigit() for ch in name):
            if not name.isalpha() :
                msg = 'Name can\'t have numbers , special characters and spaces'
            elif len(name) <= 2:
                msg = 'Name is too short.'
            elif len(name) > 100:
                msg = 'name is too long.'
            else:
                msg = 'Success!'
        except Exception as ep:
            tmsg.showerror('error', ep)

    tmsg.showinfo('Message', msg)

Label(text ="!!! Welcome !!!",background = "cyan" ,font = 'SansSerief 10 bold', pady = 20).grid(row = 0, column = 2)
root.geometry("430x300")

gendervalue = StringVar()
gendervalue.set("Male ")
name = Label(root, text= "Name ",bg = "cyan").grid(row= 2, column = 1)
phone = Label(root, text= "Phone",bg = "cyan").grid(row= 3, column = 1)
gender = Label(root,text= "Gender",bg = "cyan").grid(row= 4, column = 1)
radio = Radiobutton(root , text  = "Male", variable = gendervalue, value = "Male",bg= "cyan").grid(row = 4,column= 3)
radio = Radiobutton(root , text  = "Female", variable = gendervalue, value = "Female",bg= "cyan").grid(row = 5,column= 3)
radio = Radiobutton(root , text  = "Others", variable = gendervalue, value = "Others",bg= "cyan").grid(row = 6,column= 3)
emailmode = Label(root,text= "Email",bg = "cyan").grid(row= 7, column = 1)

namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
emailservicevalue = IntVar()

nameEntry = Entry(root, textvariable = namevalue, width = 30).grid(row= 2, column = 3,padx = 10, pady = 5)
phoneEntry = Entry(root, textvariable = phonevalue, width = 30).grid(row= 3, column = 3,padx = 10, pady = 5)
emailEntry = Entry(root, textvariable = emailvalue , width = 30).grid(row= 7, column = 3,padx = 10, pady = 5)
emailservice = Checkbutton(text= "Do you want to receive emails from us ?", variable = emailservicevalue).grid (row= 8, column = 3,padx = 10, pady = 5)

Button(text = "Submit" , command = validateName,background = "lightgreen", activebackground = "Green", font = "Arial 10 bold ").grid(column = 2, row = 9)
root.mainloop()