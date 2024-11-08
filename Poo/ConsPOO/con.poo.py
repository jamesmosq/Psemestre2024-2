import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            print("Conexión exitosa")
        except mysql.connector.Error as error:
            print("Error de conexión:", error)
        return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada correctamente")

# Configuración de la conexión
db_manager = DatabaseManager('localhost', 'root', '', 'northwind')

# Conectar a la base de datos y desconectar
connection = db_manager.connect()
db_manager.disconnect()
