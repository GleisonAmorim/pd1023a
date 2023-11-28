import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

sql = 'select id, descricao from categorias'
resultado = cursor.execute(sql)
print("Categorias disponíveis: ")

for categoria in resultado:
    print("ID:", categoria[0], "Descrição:", categoria[1])
categoria_id = input("Informe o ID da categoria: ")

titulo = input("Digite o título do evento: ")

data = input("Digite a data do evento (d/m/a): ")

sql = 'insert into eventos(titulo, categoria_id, data) values (?, ?, ?)'
valores = [titulo, categoria_id, data]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
