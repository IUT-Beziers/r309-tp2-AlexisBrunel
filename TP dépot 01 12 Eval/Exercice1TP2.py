from tkinter import*
#classImport modification de la lib tkinter.dnd
from classImport import *
from PIL import Image, ImageTk
#from tkinter.dnd import * cliquer sur dnd puis F12
fen = Tk()
fen.withdraw()
main = Tester(fen)
tabImage = []
lines = []
frame = Frame(fen)

#Creation de la liste des images à proposé pour le changement
OptionList = [
"router1.png",
"switch1.png",
"client1.png"
] 

#Varaible permettant d'identifier les objets
routeur = 1
switch = 1
client = 1
ConnectCount = 1


def ConfirmText(obj, button, entry):
    #recupere la valeur en entry et la met dans les textes
    obj.label.config(text = entry.get()) 
    obj.text.config(text = entry.get()) 
    #detruit les bouttons en surplus
    button.destroy()
    entry.destroy()

def ConfirmImage(obj, button, entry,menu):
    #change la photo de notre objet 
    img2 = ImageTk.PhotoImage(Image.open(entry.get()))
    obj.label.configure(image=img2)
    obj.label.image = img2
    #replacement du label après modification de l'image
    obj.text.place(x=obj.label.winfo_x()+(img2.width()/2)-10,y=obj.label.winfo_y()+10+img2.height())
    button.destroy()
    menu.destroy()

def rename(obj):
    #crée des instances pour récuperer le choix utilisateur
    ent = Entry(main.top, bd=2)
    ent.pack(side = LEFT)
    showButton = Button(main.top, text='Entrez')
    showButton.config(command=lambda obj=obj,button=showButton,entry=ent: ConfirmText(obj, button, entry))
    showButton.pack(side = LEFT)

def changeImage(obj):
    #crée des instances pour récuperer le choix utilisateur avec une liste de choix
    variable = StringVar(main.top)
    variable.set(OptionList[0])
    ent = OptionMenu(main.top, variable, *OptionList)
    ent.config(width=90, font=('Helvetica', 12))
    ent.pack(side= LEFT)
    showButton = Button(main.top, text='Entrez')
    showButton.config(command=lambda obj=obj,button=showButton,var=variable, menu=ent: ConfirmImage(obj, button, var,menu))
    showButton.pack(side = LEFT)

m = Menu(fen, tearoff=0)

#variable de gestion des lignes
IsOnLine = False
line = None
obj1 = None

#function du menu d'action sur l'objet
def Edit(event, label):
    global line
    #test si l'on doit detruire ou crée nos commandes du menu
    try:
        try:
            m.index("Image")
            m.delete("Image")
            m.index("Rename")
            m.delete("Rename")
            m.index("NewLine")
            m.delete("NewLine")
            try:
                m.index("PlaceLine")
                m.delete("PlaceLine")
            except TclError:
                m.grab_release()
        except TclError:
            m.grab_release()
        #Ajoute les commandes necessaire au bon fonctionnement de l'app
        m.add_command(label="Image", command=lambda label=label: changeImage(label))
        m.add_command(label="Rename", command=lambda label=label: rename(label))
        #verifie si l'on doit ajouter ou placer une ligne à notre objet
        m.add_command(label="NewLine", command= lambda obj=label: AddLigne(obj)) if not IsOnLine else m.add_command(label="PlaceLine", command=lambda label=label: PlaceLigne(line,label)) 
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

def Router():
    #Creation d'un objet dragable
    global routeur
    d=Icon("router"+str(routeur), ImageTk.PhotoImage(Image.open("router1.png")))
    routeur+=1
    #attachement au canvas
    d.attach(main.canvas)
    #Implémentation du titre sur l'image
    #bind pour le click droit
    d.label.bind("<Button-3>", lambda event, obj=d: Edit(event,obj))
    #Ajout de l'objet dans un tableau
    tabImage.append(d)

def Switch():
    global switch
    d=Icon("switch"+str(switch),ImageTk.PhotoImage(Image.open("switch1.png")))
    switch+=1
    d.attach(main.canvas)
    d.label.bind("<Button-3>", lambda event, obj=d: Edit(event,obj))
    tabImage.append(d)

def Client():
    global client
    d=Icon("client"+str(client),ImageTk.PhotoImage(Image.open("client1.png")))
    client+=1
    d.attach(main.canvas)
    d.label.bind("<Button-3>", lambda event, obj=d: Edit(event,obj))
    tabImage.append(d)

def Clear():
    #Vide toute la page 
    for i in tabImage: i.detach()
    for i in lines: main.canvas.delete(i)

#Ajout d'une ligne
def AddLigne(obj):
    #Set global value 
    global ConnectCount
    global line
    global IsOnLine
    global obj1
    obj1 = obj
    #création de la base de notre ligne
    idLine = main.canvas.create_line(obj1.label.winfo_x(),obj1.label.winfo_y(),obj1.label.winfo_x()+1,obj1.label.winfo_y()+1, fill="black", tags = ("Line", ConnectCount), width = 5, smooth = 1)
    line = idLine
    lines.append(line)
    #ajout du suivi au curseur de notre ligne
    main.canvas.bind("<Motion>", lambda event, line=idLine, obj=obj: OnMotion(event,line, obj))
    ConnectCount +=1
    IsOnLine = True

#placement de notre ligne à ses points finaux
def PlaceLigne(lined, obj):
    global IsOnLine
    global obj1
    global line
    #mouvement vers la ou l'on veux la placer au final
    main.canvas.coords(lined, obj1.label.winfo_rootx(), obj1.label.winfo_rooty(), obj.label.winfo_rootx(), obj.label.winfo_rooty())
    #fin du bin pour suivre le mouvement de la souris
    main.canvas.unbind("<Motion>")
    IsOnLine = False
    line = None
    obj1 = None

#Follow du curseur avec la ligne
def OnMotion(event, line, obj):
    #récupere le cuseur de notre souris
    x, y = event.x_root, event.y_root
    #modifie les coordonées de notre ligne afin qu'elle suive notre curseur
    main.canvas.coords(line, obj.label.winfo_x(),obj.label.winfo_y(), x, y)

button = Button(main.top, text = "Router",command=Router)
button.pack(side = LEFT)
button = Button(main.top, text = "Switch", command=Switch)
button.pack(side = LEFT)
button = Button(main.top, text = "Client", command=Client)
button.pack(side = LEFT)
button = Button(main.top, text = "Clear", command=Clear)
button.pack(side = LEFT)

fen.mainloop()
#fin x)

