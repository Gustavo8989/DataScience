from tkinter import *
from tkinter import ttk
import tkinter
class tela:
    def __init__(self):
        #self.dados = dados 
        self.janela = Tk()
        self.janela.geometry("500x500") 
        self.texto = tkinter.Label(self.janela,text='Limpador de dados',bg='blue',fg='orange') 
        self.texto.pack(fill = tkinter.X)
        self.texto_dados = tkinter.Label(self.janela,text="Coloca os dados aqui",bg="blue",fg='orange') 
         
        


        button_limpar = tkinter.Button(self.janela,text='Limpar',command=self.limpar_dados)
        button_limpar.pack() 
        self.janela.mainloop()

    def limpar_dados(self):
        pass

tela()
