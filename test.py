import tkinter
from tkinter import *

fen=tkinter.Tk()
my_menu=Menu(fen)
fen.config(menu=my_menu)
can=tkinter.Canvas(fen,width=1000,heigh=1000,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)


        


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

def client():
    print("test")
    photo=PhotoImage(file='img/index.png')
    photo=resizeImage(photo,45,45)
    can.create_image(200,200,  image=photo)
    return photo
    



def drag1(event):
    global photo
    photo = PhotoImage(file = "img/index.png") 
    photo=resizeImage(photo,45,45)
    x=event.x
    y=event.y
    #Impossible de sortir 
    if x <=0 or x>=1000 or y <=0 or y>=1000 : #Empeche la photo de sortir 
        if x<0 :
            x=0
        elif x>1000 :
            x=1000
        if y<0:
            y=0
        elif y>1000:
            y=1000
    can.create_image(x, y,  image=photo)



file_menu=Menu(my_menu)
my_menu.add_cascade(label="Outils",menu=file_menu)
file_menu.add_command(label="Client",command=lambda:client())
file_menu.add_command(label="Router")
file_menu.add_command(label="Switch") 

   
    
    
can=tkinter.Canvas(fen,width=1000,heigh=1000,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)


can.bind('<B1-Motion>',drag1)

fen.mainloop()