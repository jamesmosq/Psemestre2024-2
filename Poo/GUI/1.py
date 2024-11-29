import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from tabulate import tabulate

class DatabaseConnector:
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
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida a la base de datos")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def get_employee_by_id(self, employee_id):
        try:
            self.cursor.callproc('GetEmployeeByID', [employee_id])
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                return rows  # Devuelve los datos del empleado encontrado
        except mysql.connector.Error as e:
            print(f"Error al buscar empleado: {e}")
            return None

    def delete_employee(self, employee_id):
        try:
            self.cursor.callproc('BorrarEmpleado', [employee_id])
            self.connection.commit()
            print("Empleado borrado correctamente")
            return True
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"Error al borrar empleado: {e}")
            return False

# Datos de conexión a la base de datos
host = 'localhost'
user = 'root'
password = ''
database = 'Northwind'

# Función para buscar y mostrar empleado por ID
def buscar_empleado():
    employee_id = simpledialog.askinteger("Buscar Empleado", "Ingrese el EmployeeID:")
    if employee_id:
        db_connector = DatabaseConnector(host, user, password, database)
        db_connector.connect()
        employee_data = db_connector.get_employee_by_id(employee_id)
        db_connector.disconnect()

        if employee_data:
            headers = ["EmployeeID", "LastName", "FirstName", "BirthDate", "Photo", "Notes"]
            data = tabulate(employee_data, headers=headers, tablefmt="pretty")
            messagebox.showinfo("Empleado Encontrado", f"Datos del Empleado:\n{data}")
        else:
            messagebox.showerror("Error", "No se encontró empleado con ese EmployeeID")

# Función para borrar empleado por ID
def borrar_empleado():
    employee_id = simpledialog.askinteger("Borrar Empleado", "Ingrese el EmployeeID:")
    if employee_id:
        db_connector = DatabaseConnector(host, user, password, database)
        db_connector.connect()
        success = db_connector.delete_employee(employee_id)
        db_connector.disconnect()

        if success:
            messagebox.showinfo("Empleado Borrado", "Empleado borrado correctamente")
        else:
            messagebox.showerror("Error", "Error al borrar empleado")

# Crear ventana principal
root = tk.Tk()
root.title("Operaciones con Empleados")

# Crear botones en la ventana
btn_buscar = tk.Button(root, text="Buscar Empleado", command=buscar_empleado)
btn_buscar.pack(pady=10)
btn_borrar = tk.Button(root, text="Borrar Empleado", command=borrar_empleado)
btn_borrar.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
