import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

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
            messagebox.showerror("Error de conexión", f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def execute_stored_procedure(self, procedure_name):
        try:
            self.cursor.callproc(procedure_name)
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    return headers, rows
                else:
                    return None, None
        except mysql.connector.Error as e:
            print(f"Error al ejecutar procedimiento almacenado: {e}")
            messagebox.showerror("Error", f"Error al ejecutar procedimiento almacenado: {e}")
            return None, None

class EmployeeDetailsApp(tk.Tk):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector
        self.title("Detalles de Empleados")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Frame para los controles de navegación
        nav_frame = ttk.Frame(self)
        nav_frame.pack(pady=10)

        ttk.Button(nav_frame, text="Anterior", command=self.previous_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Siguiente", command=self.next_employee).pack(side=tk.LEFT, padx=5)

        # Frame para los detalles del empleado
        self.details_frame = ttk.Frame(self)
        self.details_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.entries = {}
        self.current_row = 0
        self.total_rows = 0

        # Cargar datos
        self.load_data()

    def load_data(self):
        headers, rows = self.db_connector.execute_stored_procedure('DetalleEmpleados')
        if headers and rows:
            self.headers = headers
            self.rows = rows
            self.total_rows = len(rows)
            self.create_entry_fields()
            self.display_employee(0)
        else:
            messagebox.showinfo("Sin datos", "No se encontraron detalles de empleados")

    def create_entry_fields(self):
        for i, header in enumerate(self.headers):
            ttk.Label(self.details_frame, text=header).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(self.details_frame, width=50)
            entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            self.entries[header] = entry

    def display_employee(self, row_index):
        if 0 <= row_index < self.total_rows:
            for header, value in zip(self.headers, self.rows[row_index]):
                self.entries[header].delete(0, tk.END)
                self.entries[header].insert(0, str(value))
            self.current_row = row_index

    def next_employee(self):
        if self.current_row < self.total_rows - 1:
            self.display_employee(self.current_row + 1)

    def previous_employee(self):
        if self.current_row > 0:
            self.display_employee(self.current_row - 1)

# Configuración de la base de datos
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

# Crear y conectar a la base de datos
db_connector = DatabaseConnector(host, user, password, database)
db_connector.connect()

# Crear y ejecutar la aplicación
app = EmployeeDetailsApp(db_connector)
app.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
db_connector.disconnect()