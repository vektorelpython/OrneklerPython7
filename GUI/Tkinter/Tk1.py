from tkinter import *
import tkinter.messagebox as mb

def ekranaYaz():
    mb.showwarning("Sıradan Başlık","Tıklandı")

pencere = Tk()

pencere.title("Vektörel Bilişim")
pencere.geometry("300x100+250+500")
pencere.resizable(width=TRUE, height=FALSE)

dugme = Button(text="Tıkla",command=ekranaYaz)
dugme.pack(side=LEFT)

etiket = Label(text="www.vektorelbilisim.com",fg="red",bg="white",cursor="circle")
etiket["cursor"] = "man"
etiket.pack()

mainloop()
