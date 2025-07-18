import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect("expedicoes.db")
cursor = conexao.cursor()

# Buscando os nomes de todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("Tabelas encontradas no banco de dados:")
for tabela in tabelas:
    print("-", tabela[0])

conexao.close()
