import sqlite3
import os

def limpar_tela():
    sistema_operacional = os.name

    if sistema_operacional == 'posix':  # Sistema baseado no Unix (Linux/Mac)
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        print("Não foi possível detectar o sistema operacional. A tela não pode ser limpa.")

def conectar_bd():
    conn = sqlite3.connect('nome_do_banco.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            username TEXT,
            senha TEXT
        )
    ''')

def inserir_dados(nome, idade, username, senha):
    cursor.execute("INSERT INTO usuarios (nome, idade, username, senha) VALUES (?, ?, ?, ?)", (nome, idade, username, senha))

def consultar_dados():
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def atualizar_dados(username, nova_idade):
    cursor.execute("UPDATE usuarios SET idade=? WHERE username=?", (nova_idade, username))

def deletar_dados(username):
    cursor.execute("DELETE FROM usuarios WHERE username=?", (username,))

def fazer_login(username, senha):
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND senha=?", (username, senha))
    limpar_tela()
    return cursor.fetchone() is not None

if __name__ == "__main__":
    conn, cursor = conectar_bd()
    criar_tabela()

    # Exemplos de uso
    username = input('Usuário: ')
    senha = input('Senha: ')
    fazer_login(username, senha)
while True:
    print('1 - Inserir')
    print('2 - Consultar')
    print('3 - Atualizar')
    print('4 - Deletar')
    print('0 - Sair')
    opcao = input('Opção: ')
    limpar_tela()
    if opcao == '1':
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        username = input('Usuario: ')
        senha = input('Senha: ')
        inserir_dados(nome, idade, username, senha)
        limpar_tela()
        conn.commit()
    elif opcao == '2':
         consultar_dados()
    elif opcao == '3':
         
         atualizar_dados()
         conn.commit()
         conn.close()
    elif opcao == '4':
         consultar_dados()
         print('Digite o usuário a ser deletado')
         username = input('Usuario: ')
         deletar_dados(username)
         conn.commit()
    elif opcao == '0':
       conn.close()
       break
    else:
        print('Opção invalida!')