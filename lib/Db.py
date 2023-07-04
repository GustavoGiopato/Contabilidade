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
def obter_livro_diario(connection, cursor):
    # Consulta SQL
    sql = """
        SELECT lc.COD_LANCAMENTO, lc.DATA, lc.NUMERO_LANCAMENTO, lc.HISTORICO, ld.COD_CONTA_DEBITO, ld.COD_CONTA_CREDITO, ld.VALOR
        FROM LANCAMENTOS_CONTABEIS lc
        JOIN LIVRO_DIARIO ld ON lc.COD_LANCAMENTO = ld.COD_LANCAMENTO_CONTABIL;
    """
    
    # Execução da consulta
    cursor.execute(sql)
    
    # Obtenção dos resultados
    resultados = cursor.fetchall()
    
    # Retorno dos resultados
    return resultados
