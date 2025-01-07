import sqlite3

#conexão com o db ou criação do db
def conectar():
  return  sqlite3.connect("clientes.db")


# Função para criar a tabela de clientes
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT,
            endereco TEXT
        )
    ''')
    conn.commit()
    conn.close()



def cadastrar_cliente(nome, cpf, telefone, endereco):
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO clientes (nome, cpf, telefone, endereco)
        VALUES (?, ?, ?, ?)
    ''', (nome, cpf, telefone, endereco))
    
    conn.commit()  # Confirma a inserção
    conn.close()  # Fecha a conexão
    
    print("Cliente cadastrado com sucesso!")

def editar_cliente(id_cliente, nome, cpf, telefone, endereco):
  conn = conectar()
  cursor = conn.cursor()
  cursor.execute( '''
     UPDATE clientes 
     SET nome = ?, cpf = ?, telefone = ?, endereco = ?
     WHERE id = ?

''', (nome,cpf,telefone,endereco,id_cliente))

  conn.commit()
  conn.close()

  print("Cliente editado com sucesso!")


def excluir_cliente(id_cliente):
  conn = conectar()
  cursor = conn.cursor()
  cursor.execute(''' 
    DELETE FROM  clientes WHERE id = ?

''', (id_cliente,))

  conn.commit()
  conn.close()

  print("Cliente deletado com sucesso!")


def listar_clientes():
  conn = conectar()
  cursor = conn.cursor()
  cursor.execute(''' 
     SELECT * FROM clientes 
''')

  clientes = cursor.fetchall() 
  conn.close()

  if clientes:
    for cliente in clientes:
      print(f"ID: {cliente[0]}, NOME: {cliente[1]}, CPF: {cliente[2]}, TELEFONE: {cliente[3]}, ENDEREÇO: {cliente[4]} ")
  
  else: 
    print("Nenhum cliente encontrado!")


def cadastrar_cliente_usuario():
    
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    
    # Chamar a função para cadastrar o cliente
    cadastrar_cliente(nome, cpf, telefone, endereco)

