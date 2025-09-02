
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from controllers.controller import Controller

import config
from Calculo import *
from config import *

class Tela:

    def __init__(self):
        #ctk.set_appearance_mode("dark")  # ou "dark"
        ctk.set_default_color_theme("blue")  # você pode mudar o tema aqui

        self.calculo = Controller(self)
        self.funcao_calculo = None
        self.produtos = self.calculo.get_produtos()
        self.nomes = [nome[0] for nome in self.produtos]
        self.janela = ctk.CTk()
        self.janela.title("CALCULO FACIL")
        self.janela.geometry("1000x1000")
        self.combo = ctk.CTkComboBox(self.janela, values=self.nomes, font=config.fonte, width=config.cbox_larg,
                                     command=self.calculo.ao_clicar)
        self.rotulo = ctk.CTkLabel(self.janela, text="foto", width=200, height=200, fg_color=cor_frames)
        self.frame01 = ctk.CTkFrame(self.janela, fg_color=cor_frames)
        label01 = ctk.CTkLabel(self.frame01, text="Qnt:", text_color="black", font=("Arial", 11, "bold"))
        label02 = ctk.CTkLabel(self.frame01, text="Altura:", text_color="black", font=("Arial", 11, "bold"))
        label03 = ctk.CTkLabel(self.frame01, text="Largura:", text_color="black", font=("Arial", 11, "bold"))


        self.frame02 = ctk.CTkFrame(self.janela, width=500, height=500, fg_color=cor_frames)
        label04 = ctk.CTkLabel(self.frame02, font=("Arial", 12, "bold"), height=25, width=500, text_color="black",
                               fg_color='gray', text="Codigo\tQnt/Perfil\tPESO/barra\tPESO/Total", anchor="w")
        self.lbl_print = ctk.CTkLabel(self.frame02, text="Peso/Total:\nCor Selecionada:\nValor Aproximado:",justify='left',
                                      font=("Arial", 20, 'bold'), anchor='w')
        self.frame03 = ctk.CTkFrame(self.janela, fg_color=cor_frames, width=150, height=120)
        self.barra_topo = ctk.CTkFrame(self.janela, height=25)


        self.lblresultado = ctk.CTkLabel(self.frame02, text="", font=("Arial", 17, "bold"), width=500, anchor='w')
        self.resutado_calculos()
        self.conponentes_comando()
        self.frame_informativo()



        self.barra_topo.pack(side='top', fill='x')
        rotulo_produto = ctk.CTkLabel(self.janela, text="PRODUTO",font=config.fonte)
        rotulo_produto.place(x=10, y=27)
        self.combo.place(x=70, y=30)
        self.rotulo.place(x=10, y=60)
        self.frame01.place(x=225, y=60)
        label01.grid(column=1, row=1)
        label02.grid(column=2, row=3)
        label03.grid(column=2, row=4)

        self.frame02.pack_propagate(False)
        self.frame02.place(x=10, y=300)
        label04.pack()
        self.lbl_print.place(x=1,y=300)


        self.frame03.pack_propagate(False)


        img = Image.open("img_produtos/janela01.jpg")
        img = img.resize((200,200))
        self.img = ctk.CTkImage(light_image=img,size=(200,200))

        self.frame03.place(x=225,y=150)


    def frame_informativo(self):
        self.info = ctk.CTkFrame(self.janela,width=500,height=500,bg_color=cor_frames)
        self.lbl_info = ctk.CTkLabel(self.info,text="",justify='left')
        self.lbl_info.pack()
        self.info.place(x=530,y=300)

    def resutado_calculos(self):
        self.lblTotal = ctk.CTkLabel(self.frame02, text="", font=("Arial", 17, "bold"),text_color="green")
        self.lblCor_selecionada = ctk.CTkLabel(self.frame02,font=("Aria",20,'bold'),text_color='green',text="")
        self.lblValorAproximado = ctk.CTkLabel(self.frame02,font=('Arial',20,'bold'),text_color="green",text="")

        self.lblCor_selecionada.place(x=200, y=320)
        self.lblValorAproximado.place(x=200, y=350)
        self.lblTotal.place(x=150, y=300)

    def conponentes_comando(self):
        self.entre_quantidade = ctk.CTkEntry(self.frame01, width=50, font=("Arial", 11, "bold"), height=4)
        self.entre_largura = ctk.CTkEntry(self.frame01, width=80, font=("Arial", 11, "bold"), height=4)
        self.entre_altura = ctk.CTkEntry(self.frame01, width=80, font=("Arial", 11, "bold"), height=4)
        self.btn_calcular = ctk.CTkButton(self.janela, text="CALCULAR", fg_color="lightblue",font=("Arial", 11, "bold"), command=self.calculo.click_frame01)

        self.btn_cor_branco = ctk.CTkButton(self.frame03, fg_color="white", width=20, text="",command=lambda: self.calculo.add_cor(2))
        self.btn_cor_bronze = ctk.CTkButton(self.frame03, fg_color="#4d3339", width=20, text="",command=lambda: self.calculo.add_cor(4))
        self.btn_cor_preto = ctk.CTkButton(self.frame03, fg_color="black", width=20, text="", command=lambda: self.calculo.add_cor(3))
        self.btn_cor_brilho = ctk.CTkButton(self.frame03, fg_color="#45484b", width=20, text="", command=lambda: self.calculo.add_cor(1))
        self.label05 = ctk.CTkLabel(self.frame03, text="COR : ", font=("Arial", 11, "bold"))
        self.lbl_cor = ctk.CTkLabel(self.frame03, font=config.fonte, text="brilho")
        self.btn_cadastrar = ctk.CTkButton(self.janela,text="cadastrar",command= self.calculo.set_cadastro)

        self.entre_quantidade.grid(column=2, row=1)
        self.entre_altura.grid(column=3, row=3, padx=10)
        self.entre_largura.grid(column=3, row=4, padx=10)
        self.btn_calcular.place(x=410, y=30)
        self.label05.grid(column=1, row=1)
        self.btn_cor_brilho.grid(column=2, row=1, padx=4)
        self.btn_cor_branco.grid(column=3, row=1, padx=4)
        self.btn_cor_preto.grid(column=4, row=1, padx=4)
        self.btn_cor_bronze.grid(column=5, row=1, padx=4)
        self.lbl_cor.grid(columnspan=4, row=5, column=2)
        self.btn_cadastrar.place(x=555,y=30)

    def janela_cadastrar(self):
        tela_cadastro=ctk.CTkToplevel(self.janela)
        tela_cadastro.geometry('500x800')
        tela_cadastro.title('Cadastrar perfil e peso')




if __name__ == "__main__":
    tela = Tela()
    tela.lblresultado.pack()
    tela.janela.mainloop()
