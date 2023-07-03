from Db import create_connection, obter_livro_diario

connection, cursor = create_connection()

livro_diario = obter_livro_diario(connection, cursor)


for registro in livro_diario:
    print(registro)

cursor.close()
connection.close()
