from tkinter import * 
from tkinter import ttk 

class interface:
    def __init__(self):
        self.tela = Tk() 
        self.tela.geometry('1000x500') 
        self.tela.title('Limpador de dados') 


        self.tela.mainloop()


if __name__ == "__main__":
    app = interface() 
