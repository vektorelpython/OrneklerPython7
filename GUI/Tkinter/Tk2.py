from tkinter import *
import tkinter.messagebox as bx
anaPencere = Tk()
def ekranaYaz():
    if secim1.get()==1:
        bx.showinfo( "Mesaj Baslik", "onay1 Isaretli")
    if secim2.get()==1:
        bx.showinfo( "Mesaj Baslik", "onay2 Isaretli")
    if  secim3.get()==1:
        bx.showinfo( "Mesaj Baslik", "onay3 Isaretli")
    if  secim4.get()==1:
        bx.showinfo( "Mesaj Baslik", "onay4 Isaretli")
secim1=IntVar()
secim1.set(0)
secim2=IntVar()
secim2.set(0)
secim3=IntVar()
secim3.set(0)
secim4=IntVar()
secim4.set(0)

dugme = Button(text="sonuc",command=ekranaYaz)
dugme.pack()

anaPencere.geometry("300x100+150+150")
onay1 = Checkbutton(text="Windows 8",variable=secim1)
onay1.place(relx=0.0,rely=0.1)
onay2 = Checkbutton(text="Windows 7",variable=secim2)
onay2.place(relx=0.0,rely=0.3)
onay3 = Checkbutton(text="Windows Vista",variable=secim3)
onay3.place(relx=0.0,rely=0.5)
onay4 = Checkbutton(text="Windows XP",variable=secim4)
onay4.place(relx=0.0,rely=0.7)
mainloop()
