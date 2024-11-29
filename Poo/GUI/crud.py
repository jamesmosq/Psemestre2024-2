import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
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
            messagebox.showerror("Error de conexión", f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")

    def execute_procedure(self, procedure_name, *args):
        try:
            self.cursor.callproc(procedure_name, args)
            results = []
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    results.append((headers, rows))
            self.connection.commit()
            return results
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"Error al ejecutar el procedimiento {procedure_name}: {e}")
            messagebox.showerror("Error", f"Error al ejecutar el procedimiento {procedure_name}: {e}")
            return None

class EmployeeApp(tk.Tk):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector
        self.title("Gestión de Empleados")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Campos de entrada
        self.fields = ['EmployeeID', 'LastName', 'FirstName', 'BirthDate', 'Photo', 'Notes']
        self.entries = {}

        for i, field in enumerate(self.fields):
            ttk.Label(main_frame, text=field).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            entry = ttk.Entry(main_frame, width=50)
            entry.grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
            self.entries[field] = entry

        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=len(self.fields), column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Buscar", command=self.search_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Insertar", command=self.insert_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.update_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Borrar", command=self.delete_employee).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Mostrar Todos", command=self.show_all_employees).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_fields).pack(side=tk.LEFT, padx=5)

        # Área de resultados
        self.result_text = tk.Text(main_frame, height=20, width=80)
        self.result_text.grid(row=len(self.fields)+1, column=0, columnspan=2, pady=10)

    def search_employee(self):
        employee_id = self.entries['EmployeeID'].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID de empleado")
            return

        results = self.db_connector.execute_procedure('GetEmployeeByID', employee_id)
        if results:
            self.display_results(results)
        else:
            messagebox.showinfo("Información", "No se encontró el empleado")

    def insert_employee(self):
        values = [self.entries[field].get() for field in self.fields[1:]]  # Excluimos EmployeeID
        results = self.db_connector.execute_procedure('InsertarDatos', *values)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado insertado correctamente")
            self.clear_fields()
            self.show_all_employees()

    def update_employee(self):
        values = [self.entries[field].get() for field in self.fields]
        results = self.db_connector.execute_procedure('ActualizarEmpleado', *values)
        if results is not None:
            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.show_all_employees()

    def delete_employee(self):
        employee_id = self.entries['EmployeeID'].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID de empleado")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este empleado?"):
            results = self.db_connector.execute_procedure('BorrarEmpleado', employee_id)
            if results is not None:
                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                self.clear_fields()
                self.show_all_employees()

    def show_all_employees(self):
        results = self.db_connector.execute_procedure('DetalleEmpleados')
        if results:
            self.display_results(results)

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def display_results(self, results):
        self.result_text.delete(1.0, tk.END)
        for headers, rows in results:
            table = tabulate(rows, headers=headers, tablefmt="grid")
            self.result_text.insert(tk.END, table + "\n\n")

# Configuración de la base de datos
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

# Crear y conectar a la base de datos
db_connector = DatabaseConnector(host, user, password, database)
db_connector.connect()

# Crear y ejecutar la aplicación
app = EmployeeApp(db_connector)
app.mainloop()

# Cerrar la conexión a la base de datos al cerrar la aplicación
db_connector.disconnect()