
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from controllers.controller import Controller

import config
from Calculo import *
from config import *

class Tela:

    def __init__(self):
        self.calculo = Controller(self)
        self.funcao_calculo = None

        self.produtos = [
            ('janela 2 folhas', "img_produtos/janela01.jpg", (calcular_janela,2,False)),
            ('janela 4 folhas', 'img_produtos/janela02.jpg', (calcular_janela,4,False)),
            ('janela 2 folhas C/ bandeira', 'img_produtos/janela03.jpg', (calcular_janela,2,True)),
            ('janela 4 folhas C/ bandeira', 'img_produtos/janela04.jpg', (calcular_janela,4,True)),
            ('porta Lambri', 'img_produtos/porta01.jpg', (calcular_porta,1,False))
        ]
        self.nomes = [nome[0] for nome in self.produtos]

        ctk.set_appearance_mode("light")  # ou "dark"
        ctk.set_default_color_theme("blue")  # você pode mudar o tema aqui

        self.janela = ctk.CTk()
        self.janela.title("CALCULO FACIL")
        self.janela.geometry("1000x1000")

        # BARRA EM CIMA
        barra_topo = ctk.CTkFrame(self.janela, height=25)
        barra_topo.pack(side='top', fill='x')

        rotulo_produto = ctk.CTkLabel(self.janela, text="PRODUTO",font=config.fonte)
        rotulo_produto.place(x=10, y=27)

        # COMBOBOX
        self.combo = ctk.CTkComboBox(self.janela, values=self.nomes,font=config.fonte, width=config.cbox_larg, command=self.ao_clicar())
        self.combo.place(x=70, y=30)

        self.rotulo = ctk.CTkLabel(self.janela, text="foto", width=200, height=200, fg_color=cor_frames)
        self.rotulo.place(x=10, y=60)

        # FRAME 01
        self.frame01 = ctk.CTkFrame(self.janela, fg_color=cor_frames)
        self.frame01.place(x=225, y=60)

        label01 = ctk.CTkLabel(self.frame01, text="Qnt:", text_color="black", font=("Arial", 11, "bold"))
        label02 = ctk.CTkLabel(self.frame01, text="Altura:", text_color="black", font=("Arial", 11, "bold"))
        label03 = ctk.CTkLabel(self.frame01, text="Largura:", text_color="black", font=("Arial", 11, "bold"))

        label01.grid(column=1, row=1)
        label02.grid(column=2, row=3)
        label03.grid(column=2, row=4)

        self.entre_quantidade = ctk.CTkEntry(self.frame01, width=50, font=("Arial", 11, "bold"),height=4)
        self.entre_largura = ctk.CTkEntry(self.frame01, width=80, font=("Arial", 11, "bold"),height=4)
        self.entre_altura = ctk.CTkEntry(self.frame01, width=80, font=("Arial", 11, "bold"),height=4)

        self.entre_quantidade.grid(column=2, row=1)
        self.entre_altura.grid(column=3, row=3, padx=10)
        self.entre_largura.grid(column=3, row=4, padx=10)

        self.btn_calcular = ctk.CTkButton(self.janela, text="CALCULAR", fg_color="lightblue", font=("Arial", 11, "bold"), command=self.click_frame01)
        self.btn_calcular.place(x=450, y=65)

        # FRAME 02
        self.frame02 = ctk.CTkFrame(self.janela, width=500, height=500, fg_color=cor_frames)
        self.frame02.pack_propagate(False)
        self.frame02.place(x=10, y=300)

        label04 = ctk.CTkLabel(self.frame02, font=("Arial", 12, "bold"), height=25, width=500, text_color="black",
                               fg_color='gray', text="Codigo\tQnt/Perfil\tPESO/barra\tPESO/Total", anchor="w")
        label04.pack()

        self.lbl_print = ctk.CTkLabel(self.frame02, text="Peso/Total: \nCor Selecionada: \nValor Aproximado:",font=("Arial",20,'bold'),anchor='w')
        self.lbl_print.place(x=1,y=300)



        #FRAME 3
        self.frame03 = ctk.CTkFrame(self.janela,  fg_color=cor_frames,width=150,height=120)

        self.btn_cor_branco = ctk.CTkButton(self.frame03,fg_color="white",width=20,text="",command=lambda:self.add_cor(2))
        self.btn_cor_bronze = ctk.CTkButton(self.frame03,fg_color="#4d3339",width=20,text="",command=lambda:self.add_cor(4))
        self.btn_cor_preto = ctk.CTkButton(self.frame03,fg_color="black",width=20,text="",command=lambda:self.add_cor(3))
        self.btn_cor_brilho = ctk.CTkButton(self.frame03,fg_color="#45484b",width=20,text="",command=lambda:self.add_cor(1))
        label05 = ctk.CTkLabel(self.frame03, text="COR : ", font=("Arial", 11, "bold"))
        label05.grid(column=1,row=1)
        self.lbl_cor = ctk.CTkLabel(self.frame03,font=config.fonte,text="brilho")

        self.btn_cor_brilho.grid(column=2,row=1,padx=4)
        self.btn_cor_branco.grid(column=3,row=1,padx=4)
        self.btn_cor_preto.grid(column=4,row=1,padx=4)
        self.btn_cor_bronze.grid(column=5,row=1,padx=4)
        self.lbl_cor.grid(columnspan=4,row=5,column=2)
        self.frame03.pack_propagate(False)

        self.lblresultado = ctk.CTkLabel(self.frame02, text="", font=("Arial", 17, "bold"), width=500, anchor='w')
        self.lblTotal = ctk.CTkLabel(self.frame02, text="", font=("Arial", 17, "bold"))


        self.frame03.place(x=225,y=150)

    def add_cor(self,cor=1):
        cor_perfil = get_preco_cor(cor)
        self.lbl_cor.configure(text = cor_perfil)



    def click_frame01(self):

        self.lblresultado.configure(text = "")
        try:
            quantidade_produto = int(self.entre_quantidade.get())
            altura = int(self.entre_altura.get())
            largura = int(self.entre_largura.get())
        except ValueError:
            messagebox.showerror("Erro", "Insira apenas números válidos.")
            return

        dimensao = (altura, largura)
        funcao , quantidade_folhas, bandeira  = self.funcao_calculo
        resultado_calculos  = funcao(dimensao , quantidade_folhas , bandeira , quantidade_produto)
        texto =""
        soma_peso =0
        for perfil in resultado_calculos:
            texto += (f"{perfil['codigo']}\t"
                     f"{perfil['quant']}\t"
                     f"{perfil['kg/barra']}\t"
                     f"{perfil['kg/total']:.3f}\n")
            soma_peso+=perfil['kg/total']
            self.lblresultado.configure( text=texto )
            self.lblTotal.configure(text=f"{soma_peso:.3f}")

        self.lblresultado.pack()
        self.lblTotal.place(x=150,y=300)

        self.entre_altura.delete(0, "end")
        self.entre_largura.delete(0, "end")
        self.entre_quantidade.delete(0, "end")

    def imagemTk(self, caminho):
        imagem = Image.open(caminho)
        imagem = imagem.resize((200, 200))

        return ctk.CTkImage(light_image=imagem,size=(200,200))

    def ao_clicar(self, event=None):

        nome = self.combo.get()

        for item in self.produtos:
            if item[0] == nome:

                caminho = item[1]

                self.funcao_calculo = item[2]

                imagem = self.imagemTk(caminho=caminho)
                self.rotulo.configure(image=imagem, text="")
                self.rotulo.image = imagem  # Manter referência

if __name__ == "__main__":
    tela = Tela()
    tela.janela.mainloop()
