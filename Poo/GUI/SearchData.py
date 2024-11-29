import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import tkinter as tk
from tkinter import messagebox

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establece la conexión con la base de datos."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida a la base de datos")
            return True
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")
            return False

    def disconnect(self):
        """Cierra la conexión con la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")
            messagebox.showinfo("Información", "Conexión cerrada")

    def execute_stored_procedure(self, procedure_name, *args):
        """Ejecuta un procedimiento almacenado con los argumentos dados."""
        if not self.connection or not self.connection.is_connected():
            if not self.connect():
                return "No se pudo establecer la conexión a la base de datos."

        try:
            self.cursor.callproc(procedure_name, args)
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    table = PrettyTable(headers)
                    table.align = "l"  # Alinea el texto a la izquierda
                    for row in rows:
                        table.add_row(row)
                    return table.get_string()
                else:
                    return "No se encontraron resultados"
        except Error as e:
            return f"Error al ejecutar procedimiento almacenado: {e}"

class App(tk.Tk):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector
        self.title("Database GUI")
        self.geometry("700x500")

        self.label = tk.Label(self, text="Employee ID:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.search_button = tk.Button(self, text="Buscar Empleado", command=self.search_employee)
        self.search_button.pack(pady=10)

        self.result_text = tk.Text(self, height=15, width=70)
        self.result_text.pack(pady=10)

        self.connect_button = tk.Button(self, text="Conectar", command=self.connect_to_db)
        self.connect_button.pack(pady=10)

        self.disconnect_button = tk.Button(self, text="Desconectar", command=self.disconnect_from_db)
        self.disconnect_button.pack(pady=10)

        # Intenta conectar automáticamente al iniciar la aplicación
        self.connect_to_db()

    def connect_to_db(self):
        if self.db_connector.connect():
            messagebox.showinfo("Información", "Conexión establecida a la base de datos")

    def disconnect_from_db(self):
        self.db_connector.disconnect()

    def search_employee(self):
        employee_id = self.entry.get()
        if employee_id:
            result = self.db_connector.execute_stored_procedure('GetEmployeeByID', employee_id)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID de empleado")

# Datos de conexión a la base de datos
host = 'localhost'
user = 'root'
password = ''
database = 'northwind'

# Creación del objeto DatabaseConnector
db_connector = DatabaseConnector(host, user, password, database)

# Creación de la aplicación Tkinter
app = App(db_connector)
app.mainloop()