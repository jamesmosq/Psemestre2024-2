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

    select_query = "SELECT CustomerID, CustomerName, ContactName, Address, City, Postalcode FROM Customers"
    cursor.execute(select_query)

    customers = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]

    print(tabulate(customers, headers=column_names,tablefmt='grid',numalign='center'))

except mysql.connector.Error as error:
    print("Error de MySQL:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
