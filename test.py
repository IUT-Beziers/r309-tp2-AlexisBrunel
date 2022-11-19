from tkinter import*
from PIL import Image, ImageTk
fen = Tk()
taille= Frame(fen, width=900, height=600)
taille.pack()

c = Canvas(fen, bg='white', width=1000, height=600)
c.pack()


def show_imageRouter():
    c.create_image(0,30, image=image1)

def show_imageSwitch():
    c.create_image(30,60, image=image2)

def show_imageServer():
        c.create_image(30,100, image=image3)



button = Button(taille, text = "Router",command=show_imageRouter)
button.pack(side = LEFT)
button = Button(taille, text = "Switch", command=show_imageSwitch)
button.pack(side = LEFT)

button = Button(taille, text = "Server", command=show_imageServer)
button.pack(side = LEFT)

    
imageFile = "client.png"

image1 = ImageTk.PhotoImage(Image.open(imageFile))

imageFile = "switch.png"
image2 = ImageTk.PhotoImage(Image.open(imageFile))

imageFile = "router.png"
image3 = ImageTk.PhotoImage(Image.open(imageFile))



# Creation of a menu File > Exit
menu = Menu(fen)
fen.config(menu=menu)



fen.mainloop()