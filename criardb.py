import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# criar a tabela
cursor.execute("""
CREATE TABLE senhas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        local TEXT NOT NULL,
        user INTEGER,
        senha     VARCHAR(11) NOT NULL,
        link TEXT NOT NULL,
        obs TEXT,
        tipo TEXT,
        criado_em DATE NOT NULL
);
""")

print('Tabela criada com sucesso.')
conn.close()
