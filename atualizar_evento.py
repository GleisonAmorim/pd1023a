import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

sql = 'select id, titulo from eventos'

resultado = cursor.execute(sql)
print("Eventos disponíveis: ")
for evento in resultado:
    print("ID:", evento[0], "Título:", evento[1])

evento_id = input("Digite o ID do evento a ser atualizado: ")

sql = 'select id, titulo, categoria_id, data from eventos where id = ?'
resultado = cursor.execute(sql, [evento_id])
evento = next(resultado)
# for evento in resultado:
#     break

titulo = input("Informe o título do evento (deixe em branco caso não deseje alterar): ")
if not titulo:
    titulo = evento[1]

sql = 'select id, descricao from categorias'
resultado = cursor.execute(sql)
print("Categorias disponíveis: ")

for categoria in resultado:
    print("ID:", categoria[0], "Descrição:", categoria[1])
categoria_id = input("Informe o ID da categoria (deixe em branco caso não deseje alterar): ")
if not categoria_id:
    categoria_id = evento[2]

data = input("Informe a data do evento (deixe em branco caso não deseje alterar): ")
if not data:
    data = evento[3]

sql = 'update eventos set categoria_id = ?, titulo = ?, data = ? where id = ?'
valores = [categoria_id, titulo, data, evento_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
