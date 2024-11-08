import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

try:

    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()

    select_query = "SELECT * FROM Employees"
    cursor.execute(select_query)

    empleados = cursor.fetchall()

    for empleado in empleados:
        print(empleado)

except mysql.connector.Error as error:
    print("Error al obtener los empleados:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    # Cerrar la conexión
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
