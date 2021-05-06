import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO senhas (local, user, senha, link, obs, tipo, criado_em)
VALUES ('LOCAL DE USAR SENHA', 'USER', '***SENHA***', 'https://site.br/', 'Senha de acesso principal', 'Site', '2021-04-30')
""")
#INSERT INTO senhas (local, user, senha, link, obs, tipo, criado_em)
#VALUES ('LOCAL DE USAR SENHA', 'USUARIO', '***SENHA***', 'https://site.com/', 'Senha de acesso principal', 'Site', '2021-04-30')
#""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
