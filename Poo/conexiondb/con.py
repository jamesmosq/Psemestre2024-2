import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'northwind'
try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd = "",
        database=database,
    )
    print("Conexión exitosa")
except mysql.connector.Error as error:
    print("Error de conexión:", error)
