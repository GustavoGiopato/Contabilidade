import psycopg2;

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
        print("success to connecting to postgres database")
        return connection, cursor
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None, None
