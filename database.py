import sqlite3

# conectando...
conn = sqlite3.connect('contatos.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE contatos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()