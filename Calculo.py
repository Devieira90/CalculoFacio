
from classes import get_dados
import math





def calcular_perfis(cortes, tamanho_perfil=6000):
        # Cria uma cópia da lista de cortes para não modificar a original
        cortes_restantes = sorted(cortes, reverse=True)  # Ordena do maior para o menor
        perfis_utilizados = []  # Lista de perfis usados, cada perfil é uma lista de cortes
        sobras_por_perfil = []  # Lista das sobras de cada perfil

        while cortes_restantes:
            comprimento_restante = tamanho_perfil
            perfil_atual = []

            # Itera sobre os cortes restantes para tentar encaixá-los no perfil atual
            i = 0
            while i < len(cortes_restantes):
                corte = cortes_restantes[i]

                if corte <= comprimento_restante:
                    perfil_atual.append(corte)
                    comprimento_restante -= corte
                    cortes_restantes.pop(i) # Remove o corte que foi utilizado
                    i = 0  # Reinicia o índice para tentar encaixar os maiores cortes restantes novamente
                else:
                    i += 1

            # Adiciona o perfil completo (ou parcialmente preenchido) e sua sobra
            perfis_utilizados.append(perfil_atual)
            sobras_por_perfil.append(comprimento_restante)

        return len(perfis_utilizados), sobras_por_perfil, perfis_utilizados





def pegar_lista_de_corte(dimensao,folha=1,qnt=1):

        alt,larg = dimensao #Desenpacota a tupla do argumento

        larg = int(larg/folha)
        qnt_cortes = 4*folha
        lado = int(qnt_cortes/2)
        lista_de_cortes=[] # Lista de  cortes
        for vezes in range(qnt):
            for i in range(lado):# Adciona OS Tamanho de Corte Na Lista
                lista_de_cortes.append(alt)
                lista_de_cortes.append(larg)
        lista_de_cortes.sort(reverse=True)


        return lista_de_cortes # Retorna A LISTA DE CORTE DO MAIOR PARA O MENOR


def calcular_janela (dimensao , quantidade_folhas = 2 ,bandeira = False, quantidade_janela = 1, qnt_bandeira=2):

        altura , largura = dimensao
        larg_folha = int(largura/quantidade_folhas)
        alt_bandeira = 0
        larg_badeira =0
        altura_baguete_bandeira=0
        largura_baguete_bandeira =0
        alt_folha = altura - 30
        larg_folha = int(largura/quantidade_folhas)
        largura_baguete_folha = larg_folha-60
        altura_baguete_bandeira = 0
        largura_baguete_bandeira = 0



        if bandeira :
            alt_bandeira = int(altura/4)
            larg_badeira = int(largura/qnt_bandeira)

            alt_folha = 3*alt_bandeira

            altura_baguete_bandeira = alt_bandeira - 60
            largura_baguete_bandeira = larg_badeira - 40

        altura_baguete_folha = alt_folha - 80



        altura_montante = selecionar_cortes(altura,2*quantidade_janela)
        largura_montante = selecionar_cortes(largura,2*quantidade_janela)
        folhas_101 = selecionar_cortes(alt_folha,2*quantidade_janela)
        folhas_122 = selecionar_cortes(larg_folha,2*quantidade_folhas*quantidade_janela)

        folhas_102 = selecionar_cortes(alt_folha,int(quantidade_folhas/2)*quantidade_janela)
        folhas_103 = selecionar_cortes(alt_folha,int(quantidade_folhas/2)*quantidade_janela)

        folhas_104 = selecionar_cortes(alt_folha,(1*quantidade_janela))
        folhas_105 = selecionar_cortes(alt_folha , (1* quantidade_janela))
        folhas_135 = selecionar_cortes(larg_badeira, (2 * quantidade_janela))

        folhas_108 = selecionar_cortes(alt_bandeira, (4 * quantidade_janela))
        folhas_108.extend([larg_badeira] * (2*quantidade_janela))

        baguetes = 2*quantidade_folhas*quantidade_janela
        baguete_folhas = selecionar_cortes(alt_folha,baguetes)
        baguete_folhas.extend([largura_baguete_folha] * baguetes)
        baguete_folhas.extend([altura_baguete_bandeira] *(2*quantidade_janela*quantidade_folhas))
        baguete_folhas.extend([largura_baguete_bandeira] * (2*quantidade_janela*quantidade_folhas))

        dados = []

        dados.append(calcular_kg(altura_montante,get_dados('368')))

        if bandeira: # com bandeira
            for vezes in range(quantidade_janela):
                largura_montante.pop()

            if quantidade_folhas == 2:
                dados.append(calcular_kg(largura_montante, get_dados('362')))
            else:
                dados.append(calcular_kg(largura_montante, get_dados('363')))




            perfil_364 = selecionar_cortes(largura, quantidade_janela)
            dados.append(calcular_kg(perfil_364, get_dados('364')))

            perfil_365 = selecionar_cortes(largura, quantidade_janela)
            dados.append(calcular_kg(perfil_365, get_dados('365')))
            dados.append(calcular_kg(folhas_135, get_dados('135')))
            dados.append(calcular_kg(folhas_108, get_dados('108')))

        else: # sem badeira

            if quantidade_folhas == 2:
                dados.append(calcular_kg(largura_montante, get_dados('362')))
            else:
                dados.append(calcular_kg(largura_montante, get_dados('363')))


        dados.append(calcular_kg(folhas_122, get_dados('122')))
        dados.append(calcular_kg(folhas_101, get_dados('101')))
        dados.append(calcular_kg(folhas_102, get_dados('102')))
        dados.append(calcular_kg(folhas_103, get_dados('103')))
        if quantidade_folhas > 2:
            dados.append(calcular_kg(folhas_104, get_dados('104')))
            dados.append(calcular_kg(folhas_105, get_dados('105')))

        dados.append(calcular_kg(baguete_folhas,get_dados('176')))







        return dados












def selecionar_cortes(medida,quant):

        listasMedidas = []
        listasMedidas.extend([medida]*quant)
        return listasMedidas



def calcularForracao(dimensao,qnt=1):
        alt,larg = dimensao
        tiras = math.floor(alt/17)
        lista_cortes=[]
        for vezes in range(qnt):
            for i in range(tiras):
               lista_cortes.append(larg)


        return lista_cortes







def calcular_kg(lista , nome_peso):

        nome,kg = nome_peso
        quantidade , sobra , perfis_cortados = calcular_perfis(lista)
        correcao = corrigir_quantidade(sobra,quantidade)
        quantidade=correcao
        kg_total = quantidade*kg



        return  {'codigo':nome,
                 'quant':quantidade,
                 'kg/barra':kg,
                 "kg/total":kg_total,
                 'sobra':sobra,
                 'perfis_cortados':perfis_cortados}


def calcular_porta(dimensao, folhas = 1 , qnt=1):



            dados =[]
            kg_tot =0
            lista_montante = pegar_lista_de_corte(dimensao,qnt=qnt)
            lista_forracao = int(calcularForracao(dimensao,qnt=qnt))

            dados_montante = calcular_kg(lista_montante, 3.5, '201')
            dados_lambri = calcular_kg(lista_forracao, 4.2, 'lb8')


            dados.append(dados_montante)
            dados.append(dados_lambri)
            return dados



def get_preco_cor(cor):
        if cor ==1 :
            return 34,'brilho'
        if cor == 2 :
            return 35,'branco'
        if cor ==3 :
            return 39,'preto'
        if cor == 4 :
            return 40,'bronze'






def mostrar(dados):

        print("CODIGO   QUANT   KG/BARRA   KG/TOTAL   SOBRA ")
        for dado in dados:
            print(f"{dado['codigo']}       {dado['quant']}        {dado['kg/barra']:.3f}      {dado['kg/total']:.3f}         {dado['sobra']}")


def corrigir_quantidade(sobras,quant):

        for sobra in sobras:
            if sobra >= 3000:
                quant-=0.5
        return quant


def separar_cortes(lista,altura):
        lista_maior = []
        lista_menor = []

        for item in lista:
            if item >=altura:
                lista_maior.append(item)
            else :
                lista_menor.append(item)



        return lista_maior,lista_menor


def calcular_grade(perfil_externo,perfil_grade,altura_grade,largura_grade):

     desconto = perfil_externo*2
     largura_interna = largura_grade-desconto
     espaco = 25 + perfil_grade
     quantidade_travessao = int((largura_interna/espaco)-1)
     return (altura_grade-desconto,quantidade_travessao)



def getLista(qntItens,item):

    lista=[]
    for i  in range(qntItens):
        lista.append(item)
    return  lista