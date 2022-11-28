import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

def gravar(nome, email, telefone):
    query = "INSERT INTO contatos (nome, email, telefone) VALUES ('{}', '{}', '{}')".format(nome, email, telefone)
    cursor.execute(query)
    conn.commit()

def listar():
    cursor.execute("SELECT * FROM contatos")
    return cursor.fetchall()

def buscar(parametro):
    query = "SELECT * FROM contatos WHERE nome LIKE '%{}%' OR email LIKE '%{}%'".format(parametro, parametro)
    cursor.execute(query)
    return cursor.fetchall()

def editar(id, nome, email, telefone):
    query = "UPDATE contatos SET nome = '{}', email = '{}', telefone = '{}' WHERE id = {}".format(nome, email, telefone, id)
    print(query)
    cursor.execute(query)
    conn.commit()

def deletar(id):
    query = "DELETE FROM contatos WHERE id = {}".format(id)
    cursor.execute(query)
    conn.commit()

