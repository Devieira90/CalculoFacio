
import customtkinter as ctk


class Toplevel :
    def __init__(self,tela):
        self.tela = tela
        self.janela =  ctk.CTkToplevel(self.tela)
        self.janela.geometry('1000x500')
        self.janela.title('Perfis')