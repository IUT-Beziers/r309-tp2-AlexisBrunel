from tkinter import *
fen=Tk()

def outils():#fonction barre d'outils
    pass

def keytouch():#fonction qui va lorsque le la touche R,C ou S presser importer un item et le placer.

    pass 

def check (): #fonction qui vérifie si l'image peut être placer (si il n'y à pas d'autre image)
    pass

# Fonction pour modifier la taille de l'image 
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

def router ():
    img=PhotoImage(file='/home/alexis/Bureau/Cours/Prog_event/TP1/img/router.png')
    img=resizeImage(img,45,45)
    my_img =can.create_image(img)

def switch():
    img=PhotoImage(file='img/swtich.jpeg')
    img=resizeImage(img,45,45)

def client():
    img=PhotoImage(file='img/client.jpeg')
    img=resizeImage(img,45,45)

can=Canvas(fen,width=1000,heigh=600,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)

fen.mainloop() 


import tkinter
from tkinter import *

#Exercice 3 

def Commencer():
    pass

# Fonction pour modifier la taille de l'image 
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

def reine ():
   
    photo=PhotoImage(file='img/index.png')
    photo=resizeImage(photo,45,45)
    return photo
    
    




def drag(event):
    global photo
    photo = PhotoImage(file = "img/index.png") 
    photo=resizeImage(photo,45,45)
    x=event.x
    y=event.y
    #Impossible de sortir 
    if x <=0 or x>=400 or y <=0 or y>=400 : #Empeche la photo de sortir 
        if x<0 :
            x=0
        elif x>400 :
            x=400
        if y<0:
            y=0
        elif y>400:
            y=400
    my_img = can.create_image(x, y,  image=photo)
    
    

can=Canvas(fen,width=1000,heigh=600,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)
fen.mainloop() 
photo=reine()
Commencer()
can.bind('<B1-Motion>',drag)
fen.mainloop()