import sqlite3
import pandas as pd

# criar e conectar ao banco de dados
def criar_conexao_banco_dados(loja_roupas):
    conn = sqlite3.connect(loja_roupas)
    return conn



#criar as tabelas
def criar_tabelas(conn):
    cursor = conn.cursor()

    #tabela "Clientes"
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                        id INTEGER PRIMARY KEY,
                        nome TEXT,
                        email TEXT
                    )''')



    #tabela "Pedidos"
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                        id INTEGER PRIMARY KEY,
                        cliente_id INTEGER,
                        produto TEXT,
                        quantidade INTEGER,
                        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
                    )''')

    conn.commit()



#inserir dados nas tabelas
def inserir_dados(conn):
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('João', 'joao@email.com')")
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Maria', 'maria@email.com')")
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Lucas', 'lucas@email.com')")
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Marcos', 'marcos@email.com')")
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('Julia', 'julia@email.com')")
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES ('José', 'jose@email.com')")

    cursor.execute("INSERT INTO Pedidos (cliente_id, produto, quantidade) VALUES (1, 'Camiseta', 2)")
    cursor.execute("INSERT INTO Pedidos (cliente_id, produto, quantidade) VALUES (2, 'Calça', 1)")
    cursor.execute("INSERT INTO Pedidos (cliente_id, produto, quantidade) VALUES (3, 'Cueca', 3)")
    cursor.execute("INSERT INTO Pedidos (cliente_id, produto, quantidade) VALUES (4, 'Casaco', 5)")
    cursor.execute("INSERT INTO Pedidos (cliente_id, produto, quantidade) VALUES (5, 'Chapéu', 4)")


    conn.commit()


#executar a consulta INNER JOIN com Pandas
def consulta_inner_join(conn):
    query_inner = '''SELECT Clientes.nome, Pedidos.produto
                    FROM Clientes
                    INNER JOIN Pedidos ON Clientes.id = Pedidos.cliente_id'''

    df_inner = pd.read_sql_query(query_inner, conn)
    print("INNER JOIN com Pandas:")
    print(df_inner)
    print("----------------------")

#executar a consulta LEFT JOIN com Pandas
def consulta_left_join(conn):
    query_left = '''SELECT Clientes.nome, Pedidos.produto
                    FROM Clientes
                    LEFT JOIN Pedidos ON Clientes.id = Pedidos.cliente_id'''
    df_left = pd.read_sql_query(query_left, conn)
    print("LEFT JOIN com Pandas:")
    print(df_left)
    print("----------------------")


#função principal
def main():
    nome_banco = 'meu_.db'
    # Criar e conectar ao banco de dados
    conn = criar_conexao_banco_dados(nome_banco)
    # Criar as tabelas
    criar_tabelas(conn)
    # Inserir dados nas tabelas
    inserir_dados(conn)
    # Executar consultas INNER JOIN e LEFT JOIN usando Pandas
    consulta_inner_join(conn)
    consulta_left_join(conn)
    # Fechar a conexão
    conn.close()

# Executar a função principal
if __name__ == '__main__':
    main()