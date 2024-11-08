import mysql.connector
from tabulate import tabulate

user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

try:
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()

    select_query = "SELECT employeeID, LastName, FirstName, BirthDate,Photo FROM Employees"
    cursor.execute(select_query)

    empleados = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    print(tabulate(empleados, headers=column_names, tablefmt='grid'))

except mysql.connector.Error as error:
    print("Error al obtener los empleados:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    # Cerrar la conexión
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
