import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="contabilidade",
            user="postgres",
            password="afn-8188"
        )
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None, None

# Função para obter os dados do Livro Diário
def obter_cod_plano_de_contas(cursor, connection):
    try:
        
        cursor.execute("SELECT codigo, descricao FROM plano_de_contas")
        
        
        # Obter os resultados
        resultados = cursor.fetchall()
        
        # Fechar a conexão com o banco de dados
        connection.close()
        
        # Retornar os resultados como uma lista
        return [f'{resultado[0]} - {resultado[1]}' for resultado in resultados]
    
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados PostgreSQL:", e)
        return []

     
