from tkinter import*
#classImport modification de la lib tkinter.dnd
from classImport import *
from PIL import Image, ImageTk
#from tkinter.dnd import * cliquer sur dnd puis F12
fen = Tk()
fen.withdraw()
main = Tester(fen)
tabImage = []
frame = Frame(fen)

#Trouver comment afficher au bonne endroit le Entry


def ConfirmText(label, button, entry):
    label.text = entry.get()
    button.destroy()
    entry.destroy()


def ConfirmImage(label, button, entry):
    label.image = ImageTk.PhotoImage(Image.open(entry.get()))
    button.destroy()
    entry.destroy()


def rename(label):
    ent = Entry(frame)
    showButton = Button(main.top, text='Entrez')
    showButton.config(command=lambda label=label,button=showButton,entry=ent: ConfirmText(label, button, entry))
    showButton.pack(side = LEFT)

def changeImage(label):
    ent = Entry(frame)
    showButton = Button(main.top, text='Entrez')
    showButton.config(command=lambda label=label,button=showButton,entry=ent: ConfirmImage(label, button, entry))
    showButton.pack(side = LEFT)

m = Menu(fen, tearoff=0)



def Edit(event, label):
    try:
        m.add_command(label="Image", command=lambda label=label: changeImage(label))
        m.add_separator()
        m.add_command(label="Rename", command=lambda label=label: rename(label))
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

def Router():
    #Creation d'un objet dragable
    d=Icon("router", ImageTk.PhotoImage(Image.open("router1.png")))
    #attachement au canvas
    d.attach(main.canvas)
    #Implémentation du titre sur l'image
    #bind pour le click droit
    d.label.bind("<Button-3>", lambda event, label=d.label: Edit(event,label))
    #Ajout de l'objet dans un tableau
    tabImage.append(d)

def Switch():
    d=Icon("switch",ImageTk.PhotoImage(Image.open("switch1.png")))
    d.attach(main.canvas)
    d.label.bind("<Button-3>", lambda event, label=d.label: Edit(event,label))
    tabImage.append(d)

def Client():
    d=Icon("client",ImageTk.PhotoImage(Image.open("client1.png")))
    d.attach(main.canvas)
    d.label.bind("<Button-3>", lambda event, label=d.label: Edit(event,label))
    tabImage.append(d)

def Clear():
    for i in tabImage: i.detach()

button = Button(main.top, text = "Router",command=Router)
button.pack(side = LEFT)
button = Button(main.top, text = "Switch", command=Switch)
button.pack(side = LEFT)
button = Button(main.top, text = "Client", command=Client)
button.pack(side = LEFT)
button = Button(main.top, text = "Clear", command=Clear)
button.pack(side = LEFT)

fen.mainloop()


