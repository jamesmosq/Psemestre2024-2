import mysql.connector
from tabulate import tabulate

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

    procedure_name = 'empleados'
    cursor.callproc(procedure_name)

    for result in cursor.stored_results():
        empleados = result.fetchall()
        column_names = [desc[0] for desc in result.description]

    print(tabulate(empleados, headers=column_names, tablefmt='grid'))

except mysql.connector.Error as error:
    print("Error al obtener los empleados:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
