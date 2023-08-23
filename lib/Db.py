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
            dsn=r'C:\Users\SUPORTE SISMETRO\Documents\BancoFDB\TESTE.FDB',
            user='SYSDBA', password='masterkey',
            charset='iso8859_1'
        )
        cursor = connection.cursor()
        return connection, cursor
    except fdb.Error as e:
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
    
    except fdb.Error as e:
        print("Erro ao conectar ao banco de dados PostgreSQL:", e)
        return []
    
def obter_lancamento_contabel(cursor, connection):
    try:
        cursor.execute("select cod_lancamento_contabil from contabilidade group by 1")
        
        resultados = cursor.fetchall()
        
        connection.close()
        return [resultado for resultado in resultados]
    except fdb.Error as e:
        print("Erro ao conectar ao banco de dados PostgreSQL:", e)
        return []

    

def insere_registros(conta_debito,conta_credito,valor,historico,data):
    # connection = fdb.connect(
    #         dsn=r'C:\Users\SUPORTE SISMETRO\Documents\BancoFDB\TESTE.FDB',
    #         user='SYSDBA', password='masterkey',
    #         charset='iso8859_1'
    #     )
    connection, cursor = create_connection_FDB() 
    cursor = connection.cursor()
    print(historico, data,int(conta_debito),int(conta_credito),valor)
    cursor.execute("insert into contabilidade (historico,dia,cod_conta_debito,cod_conta_credito,valor) values (%s, %s, %d, %d, %d)", (historico,data,conta_debito,conta_credito,valor))
    connection.commit()  
    
    #cursor.execute("insert into livro_diario (valor, cod_conta_credito, cod_conta_debito) values (%s, %d, %d)" % (valor, int(conta_credito), int(conta_debito)))
    connection.commit()
    connection.close()

    
    
     
