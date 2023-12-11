from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class splash:
    def __init__(self):
        self.splashmainw = tk()
        self.splashmainw.title("Sistema de gerenciamento de vendas")
        width = 900
        height = 600
        self.splashmainw.config(bg="green")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenheight()
        x = (tela_largura/2) - (width/2)
        y = (tela_altura/2) - (height/2)
        self.splashmainw.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.splashmainw.resizable(0,0)
        path = "images/BacenImagem.jpeg"
        self.img = ImageTk.PhotoImage(Image.open(path)) #img = ImageTk.PhotoImage(Image.open(path))
        main = LabelFrame(self.splashmainw,width=890,heigth=560,bg="snow",relief="sunken")
        main.place(x=55,y=70)
        fotoframe = LabelFrame(main,width=420,heigth=440,bg="snow",relief="raised")
        foto = Label(fotoframe, image=img)
        foto.place(x=6,y=6)
        fotoframe.place(x=10,y=100)


        self.splashmainw.mainloop()