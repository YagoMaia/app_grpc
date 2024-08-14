import psycopg2

# Defina as informações de conexão
host = "localhost"
database = "grpc_teste"
user = "postgres"
password = "postgres"

class DB():
    connection = None
    def __init__(self):
        try:
            if self.connection is None:
                self.connection = psycopg2.connect(
                    host=host,
                    database=database,
                    user=user,
                    password=password
                )
        except Exception as error:
            print(f"Erro ao conectar ao PostgreSQL: {error}")

    @staticmethod
    def get_connection(self):
        return self.connection
    
    def cursor(self):
        if self.connection != None:
            return self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    def close(self):
        self.connection.close()