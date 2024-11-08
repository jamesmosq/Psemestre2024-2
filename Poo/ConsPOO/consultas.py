import mysql.connector
from tabulate import tabulate


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            #print("Conexión establecida correctamente.")
        except mysql.connector.Error as error:
            print("Error de conexión:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada correctamente.")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)
            return None

    def fetch_columns(self):
        if self.cursor:
            return [desc[0] for desc in self.cursor.description]
        else:
            return None
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

# Crear instancia de DatabaseManager
db_manager = DatabaseManager(host, user, password, database)

try:
    db_manager.connect()

    select_query = "SELECT CustomerID, CustomerName, ContactName, Address FROM Customers"

    # Ejecutar la consulta
    results = db_manager.execute_query(select_query)
    if results:
        # Obtener nombres de las columnas
        column_names = db_manager.fetch_columns()

        # Imprimir los resultados usando tabulate
        print(tabulate(results, headers=column_names, tablefmt='grid'))
    else:
        print("No se obtuvieron resultados.")

except Exception as e:
    print("Error inesperado:", e)
finally:
    # Cerrar la conexión
    db_manager.disconnect()
