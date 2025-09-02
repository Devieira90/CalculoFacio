import sqlite3


def criar_labela_perfil(database,tabela):
    conexao = None
    try:
        conexao = sqlite3.connect(database )
        cursor = conexao.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tabela}  (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        codigo text NOT NULL UNIQUE, 
                        peso REAL NOT NULL );''' )
        print(f"conectado com sucesso !!!")
        conexao.commit()

    except sqlite3.Error as e:

        print("Erro ao conctar : ", e)

    finally:

        conexao.close()


def cadastrar_perfil(lista_de_tupla):
    # Você pode testar se a tabela foi criada conectando-se e tentando inserir dados
    conn = None
    try:
        conn = sqlite3.connect("meu_banco.db")
        cursor = conn.cursor()

        for tupla in lista_de_tupla:
            cursor.execute("INSERT INTO perfis (codigo, peso) VALUES (?, ?)", tupla)

        print("\nDados inseridos com sucesso!")
        conn.commit()

        # Consultando os dados para verificar
        cursor.execute("SELECT * FROM perfis")
        rows = cursor.fetchall()
        print("Dados na tabela 'perfis':")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao testar a inserção/consulta: {e}")
    except sqlite3.ProgrammingError :
        print(" tente add uma linta de tupla ")
    finally:
        if conn:
            conn.close()
def mostrar_Tabela(tabela):
     # Você pode testar se a tabela foi criada conectando-se e tentando inserir dados
     conn = None
     try:
         conn = sqlite3.connect("meu_banco.db")
         cursor = conn.cursor()



         # Consultando os dados para verificar
         cursor.execute(f"SELECT * FROM {tabela}")
         rows = cursor.fetchall()
         print("Dados na tabela 'perfis':")
         for row in rows:
             print(row)

     except sqlite3.Error as e:
         print(f"Ocorreu um erro ao testar a inserção/consulta: {e}")
     finally:
         if conn:
             conn.close()

def get_dados(codigo):
    conn = None
    try:
        conn = sqlite3.connect("meu_banco.db")
        cursor = conn.cursor()

        # Consultando os dados para verificar
        cursor.execute("SELECT codigo, peso FROM perfis WHERE codigo = ?",(codigo,) )

        row = cursor.fetchone()
        return row
        print("Dados na tabela 'perfis':")


    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao testar a consulta: {e}")
        return 0
    finally:
        if conn:
            conn.close()


















