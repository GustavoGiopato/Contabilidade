import psycopg2
import fdb

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5433",
            database="contabilidade",
            user="postgres",
            password="afn-8188"
        )
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None, None

def create_connection_FDB():
    try:
        connection = fdb.connect(
            dsn='C:\\Users\\bolad\\OneDrive\\Documentos\\Banco\\teste.fdb',
            user='SYSDBA', password='masterkey',
            charset='iso8859_1'
        )
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
        print("Error connecting to Firebird database:", e)
        return None, None

# Função para obter os dados do Livro Diário
def obter_cod_plano_de_contas(cursor, connection):
    try:        
        cursor.execute("SELECT cod, descricao FROM plano_de_contas")

        # Obter os resultados
        resultados = cursor.fetchall()
        
        # Fechar a conexão com o banco de dados
        connection.close()
        
        # Retornar os resultados como uma lista
        return [f'{resultado[0]} - {resultado[1]}' for resultado in resultados]
    
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados PostgreSQL:", e)
        return []
def insere_registros(conta_debito,conta_credito,valor,historico,data, cursor, connection):
    try:
        sql1 = cursor.execute("insert into livro_diario (valor,cod_conta_credito,cod_conta_debito) values (%s, %s, %s)", (valor, conta_credito, conta_debito))
        connection.commit()
        sql2 = cursor.execute("insert into partida_de_diario (data, historico) values (%s, %s)", (data, historico))
        connection.commit()
        print(conta_debito,conta_credito,valor,historico,data)
        return sql1, sql2
    except:
        print("deu erro pai")
    
     
