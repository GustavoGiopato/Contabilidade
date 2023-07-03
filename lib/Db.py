import psycopg2

# Função para obter os dados do Livro Diário
def obter_livro_diario():
    # Conexão com o banco de dados
    conn = psycopg2.connect(
        host="localhost",
        port="5433",
        database="contabilidade",
        user="postgres",
        password="afn-8188"
    )
    
    # Criação do cursor
    cur = conn.cursor()
    
    # Consulta SQL
    sql = """
        SELECT lc.COD_LANCAMENTO, lc.DATA, lc.NUMERO_LANCAMENTO, lc.HISTORICO, ld.COD_CONTA_DEBITO, ld.COD_CONTA_CREDITO, ld.VALOR
        FROM LANCAMENTOS_CONTABEIS lc
        JOIN LIVRO_DIARIO ld ON lc.COD_LANCAMENTO = ld.COD_LANCAMENTO_CONTABIL;
    """
    
    # Execução da consulta
    cur.execute(sql)
    
    # Obtenção dos resultados
    resultados = cur.fetchall()
    
    # Fechamento do cursor e conexão com o banco de dados
    cur.close()
    conn.close()
    
    # Retorno dos resultados
    return resultados
