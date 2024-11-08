import mysql.connector

# Configuración de conexión
user = 'root'
password = ''  # Asegúrate de que esto es correcto y seguro
host = 'localhost'
database = 'Northwind'

# Parámetros del empleado a eliminar
employee_id = 1  # Por ejemplo, elimina el empleado con EmployeeID 1

try:
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()

    # Primero elimina las filas dependientes en 'orders'
    delete_orders_query = "DELETE FROM Orders WHERE EmployeeID = %s"
    cursor.execute(delete_orders_query, (employee_id,))

    # Luego elimina el empleado
    delete_employee_query = "DELETE FROM Employees WHERE EmployeeID = %s"
    cursor.execute(delete_employee_query, (employee_id,))

    # Confirmar la transacción
    conexion.commit()

    # Verificar si alguna fila fue afectada
    if cursor.rowcount > 0:
        print("Empleado eliminado correctamente.")
    else:
        print("No se encontró ningún empleado con el EmployeeID proporcionado.")

except mysql.connector.Error as error:
    print("Error al eliminar el empleado:", error)
except Exception as e:
    print("Error inesperado:", e)
finally:
    # Cerrar la conexión
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()
