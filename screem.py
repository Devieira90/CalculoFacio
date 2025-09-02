import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk
from Calculo import *



class Tela :






   def __init__(self):
        self.funcao_calculo=None
        self.produtos = [('janela 2 folhas', "img_produtos/janela01.jpg",calcular_porta),
                        ('janela 4 folhas', 'img_produtos/janela02.jpg',calcular_porta),
                        ('janela 2 folhas C/ bandeira', 'img_produtos/janela03.jpg',calcular_porta),
                        ('janela 4 folhas C/ bandeira', 'img_produtos/janela04.jpg',calcular_porta),
                        ('porta Lambri', 'img_produtos/porta01.jpg',calcular_porta)

                        ]
        self.nomes = []
        for nome in self.produtos:
           self.nomes.append(nome[0])

        # Criar a janela principal
        self.janela = tk.Tk()
        self.janela.title("CALCULO FACIL ")
        self.janela.geometry("1000x1000")  # Largura x Altura

    # BARRA EM CIMA
        barra_topo=tk.Frame(self.janela,height=25,bg='blue')
        barra_topo.pack(side='top',fill='x')

        rotulo_produto = tk.Label(self.janela,text="PRODUTO")
        rotulo_produto.place(x=10,y=27)

    # COMBO BOX ESCOLHE O PRDUTO
        self.combo = ttk.Combobox(self.janela, values=self.nomes, state='readonly', width=60)
        self.combo.place(x=70, y=30)
        self.rotulo = tk.Label(self.janela, text="foto", bg='lightgray', padx=95, pady=95)
        self.rotulo.place(x=10, y=60)




   # FRAME 01 (QUANTIDADE , ALTURA, LARGURA)
        self.frame01 = tk.Frame(self.janela,bg="lightgray",padx=5,pady=10)
        label01=tk.Label(self.frame01,text="qnt:",bg="lightgray",font=("Arial",11,"bold"))
        label02= tk.Label(self.frame01,text=" largura :  ",bg="lightgray",font=("Arial",11,"bold"))
        label03 = tk.Label(self.frame01,text="altura :  ",bg="lightgray",font=("Arial",11,"bold"))
        label01.grid(column=1,row=1)
        label02.grid(column=2,row=3)
        label03.grid(column=2,row=4)
        self.frame01.place(x=240,y=60)
        self.entre_quantidade =tk.Entry(self.frame01,width=4,font=("Arial",11,"bold"))
        self.entre_largura=tk.Entry(self.frame01,font=("Arial",11,"bold"),width=8)
        self.entre_altura=tk.Entry(self.frame01,font=("Arial",11,"bold"),width=8)
        self.entre_quantidade.grid(column=2,row=1)
        self.entre_altura.grid(column=3, row=3,padx=10)
        self.entre_largura.grid(column=3, row=4,padx=10)

        self.btn_calcular = tk.Button(self.janela,text="CALCULAR",bg="lightblue",font=("Arial",11,"bold"),command=self.click_frame01)
        self.btn_calcular.place(x=450,y=65)

   # FRAME 2 DESCRICAO
        self.frame02 = tk.Frame(self.janela,width=500,height=500,bg="white",)
        self.frame02.pack_propagate(False)
        label04 = tk.Label(self.frame02,font=("Arial",12,"bold"),height=1,width=500,bg='gray',text="Codigo         Qnt/Perfi         PESO/barra          PESO/Total",anchor="w" )

        self.lbl_print = tk.Label(self.frame02,bg="white")

        self.frame02.place(x=10,y=300)
        label04.pack()
        self.lbl_print.pack()





        self.combo.bind("<<ComboboxSelected>>", self.ao_clicar)



   def click_frame01(self):

       quantidade_produto = int(self.entre_quantidade.get())
       altura = int(self.entre_altura.get())
       largura = int(self.entre_largura.get())

       dimensao =(altura,largura)
       resultado_calculos = self.funcao_calculo(dimensao)

       for perfil in resultado_calculos:
           texto = (f"{perfil['codigo']}\t\t"
                    f"{perfil["quant"]}\t"
                    f"{perfil["kg/barra"]}\t\t"
                    f" {perfil['kg/total']:.3f}\n")
           tk.Label(self.frame02,text=texto,font=("Arial",13,"bold"),width=500,anchor='w').pack()




   def imagemTk(self,caminho):


        imagem = Image.open(caminho)
        imagem = imagem.resize((200, 200))

        img_tk = ImageTk.PhotoImage(imagem)

        return img_tk
# captura evento do combbox 01
   def ao_clicar(self,event):
       print(" funcionou ")
       nome  = self.combo.get()

       for item in self.produtos:
           if item[0] == nome:
               caminho = item[1]
               self.funcao_calculo = item[2]



       imagem = self.imagemTk(caminho= caminho)
       self.rotulo.config(image=imagem)
       self.rotulo.image = imagem
       self.rotulo.place(x=10,y=60)








if __name__ == "__main__":
    tela = Tela()


    tela.janela.mainloop()