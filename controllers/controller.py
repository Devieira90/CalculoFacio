
import Calculo as clc
from PIL import Image
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox

class Controller:
    def __init__(self,view):
        self.view = view
        self.cor_selecionada = None



    def click_comboox(self,event):
        produto = self.view.combo.get()
        self.view.lblresultado.configure(text= produto)

    def add_cor(self, cor=1):
        preco_perfil , cor_perfil = clc.get_preco_cor(cor)
        self.cor_selecionada = preco_perfil
        self.view.lbl_cor.configure(text=cor_perfil)

        self.view.lblCor_selecionada.configure(text=cor_perfil)



    def get_produtos(self):
        produtos = [
            ('janela 2 folhas', "img_produtos/janela01.jpg", (clc.calcular_janela, 2, False)),
            ('janela 4 folhas', 'img_produtos/janela02.jpg', (clc.calcular_janela, 4, False)),
            ('janela 2 folhas C/ bandeira', 'img_produtos/janela03.jpg', (clc.calcular_janela, 2, True)),
            ('janela 4 folhas C/ bandeira', 'img_produtos/janela04.jpg', (clc.calcular_janela, 4, True)),
            ('porta Lambri', 'img_produtos/porta01.jpg', ('calcular_porta', 1, False)),
            ('porta com grade', 'img_produtos/porta01.jpg', ('calcular_porta', 1, False))
        ]
        return produtos



    def imagemTk(self, caminho):
        imagem_pil = Image.open(caminho)
        imagem_pil = imagem_pil.resize((200, 200))
        imagem_ctk = CTkImage(dark_image=imagem_pil, light_image=imagem_pil, size=(200, 200))
        return imagem_ctk

    def ao_clicar(self, event=None):
        nome = self.view.combo.get()
        produtos = self.view.produtos

        for item in produtos:
            if item[0] == nome:
                caminho = item[1]
                self.view.funcao_calculo = item[2]
                imagem = self.imagemTk(caminho=caminho)
                self.view.rotulo.configure(image=imagem, text="")
                self.view.rotulo.image = imagem  # Manter referência

    def click_frame01(self):

        self.view.lblresultado.configure(text = "")
        try:
            quantidade_produto = int(self.view.entre_quantidade.get())
            altura = int(self.view.entre_altura.get())
            largura = int(self.view.entre_largura.get())
        except ValueError:
            messagebox.showerror("Erro", "Insira apenas números válidos.")
            return

        dimensao = (altura, largura)
        funcao , quantidade_folhas, bandeira  = self.view.funcao_calculo
        resultado_calculos  = funcao(dimensao , quantidade_folhas , bandeira , quantidade_produto)
        texto =""
        dados_frame_info=''
        soma_peso =0

        for perfil in resultado_calculos:
            texto += (f"{perfil['codigo']}\t"
                     f"{perfil['quant']}\t"
                     f"{perfil['kg/barra']}\t"
                     f"{perfil['kg/total']:.3f}\n")
            soma_peso+=perfil['kg/total']
            dados_frame_info +=f"{perfil['codigo'] }\t {len(perfil['perfis_cortados'][0])}\t{perfil['perfis_cortados'][0][0]}\n"
        self.view.lbl_info.configure(text=dados_frame_info)
        self.view.lblresultado.configure( text=texto )
        self.view.lblTotal.configure(text=f"{soma_peso:.3f}")
        valor_aproximado = float(self.cor_selecionada*soma_peso)
        self.view.lblValorAproximado.configure(text = f'{valor_aproximado:.2f}')

        self.view.lblresultado.pack()
        self.view.lblTotal.place(x=150,y=300)

        self.view.entre_altura.delete(0, "end")
        self.view.entre_largura.delete(0, "end")
        self.view.entre_quantidade.delete(0, "end")


    def set_cadastro(self):
       self.view.janela_cadastrar()