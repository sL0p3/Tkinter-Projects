
from tkinter import *

root = Tk()
root.title("Aaj ke Samachar")
root.geometry("1000x1000")
from PIL import ImageTk, Image

def every_110(text) :
    final_text = ""
    for i in range(0, len(text)) :
        final_text += text[i]
        if i %110==0 and i!= 0 :
            final_text += "\n"
    return final_text

texts = []
photos = []
for i in range(0,3) :
    with open(f"{i+1}.txt") as f :
        text = f.read()
        texts.append(every_110(text))

    image = Image.open(f"{i+1}.jpg")

    # TODO: resize these images
    image = image.resize((285,245), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width = 800, height = 70)
Label(f0, text = "Welcome to the Sports section", font = "lucida 33 bold").pack()
Label(f0, text = "February 27 2022", font = "lucida 12 bold").pack()
f0.pack()
side = [LEFT, RIGHT, LEFT]
for i in range(0,3):
    f = Frame(root, width = 900, height = 200, pady = 30, padx = 20)
    Label(f, text = texts[i], padx= 22, pady = 22).pack(side = side[i])
    Label(f, image = photos[i], anchor = "e").pack()
    f.pack(anchor = "w")


root.mainloop()

