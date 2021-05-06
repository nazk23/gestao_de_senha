import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()


# lendo os dados
cursor.execute("""
SELECT * FROM senhas;
""")

mytable = from_db_cursor(cursor)

#print senha em modo tabela
print(mytable) 

conn.close()
