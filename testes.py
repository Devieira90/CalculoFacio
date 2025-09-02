from telaCustom import Tela
from Calculo import *
from screem import Toplevel
if __name__ =="__main__":

 tela = Tela()


 pro=tela.combo.get()
 qnt = tela.entre_quantidade.insert(0,"1")
 altura = tela.entre_altura.insert(0,'1200')
 largura = tela.entre_largura.insert(0,'1200')
 tela.calculo.add_cor(1)
 tela.calculo.ao_clicar()

 tela.janela.mainloop()

 perfil_externo = 70
 perfil_grade = 25
 largura = 3000
 altura = 3000
 tamanho,quant = calcular_grade(perfil_externo,perfil_grade,altura,largura)

 print(f"Sera necessario {quant} travesão de {tamanho} cm ")






perfis = getLista(quant,tamanho)

nomePeso = ('tupo',1.3)
res = calcular_kg(perfis,nomePeso)

mostrar([res])



