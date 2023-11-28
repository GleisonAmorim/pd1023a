import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

cursor = conexao.cursor()

sql = 'select id, titulo from eventos'

resultado = cursor.execute(sql)
print("Eventos disponíveis: ")
eventos_possiveis = []
for evento in resultado:
    print("ID:", evento[0], "Título:", evento[1])
    eventos_possiveis.append(evento[0])

while True:
    try:
        evento_id = int(input("Digite o ID do evento a ser removido: "))
        if evento_id in eventos_possiveis:
            break
        else:
            print("Digite um ID válido!")
    except:
        print("Digite um valor númerico!")

sql = 'delete from eventos where id = ?'

cursor.execute(sql, [evento_id])

conexao.commit()
conexao.close()
