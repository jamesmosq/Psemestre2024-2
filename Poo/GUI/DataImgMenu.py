import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


class NorthwindGUI:
    def __init__(self, master):
        self.master = master
        master.title("Northwind Database Manager")
        master.geometry("800x600")

        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "Northwind"
        }

        # Crear menú
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Menú de tablas
        self.table_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Tablas", menu=self.table_menu)

        # Añadir opciones de tablas
        tables = ["Categories", "Customers", "Employees", "OrderDetails", "Orders", "Products", "Shippers", "Suppliers"]
        for table in tables:
            self.table_menu.add_command(label=table, command=lambda t=table: self.open_table_window(t))

        # Frame principal
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Label de bienvenida
        tk.Label(self.main_frame, text="Bienvenido al gestor de la base de datos Northwind", font=("Arial", 16)).pack(
            pady=20)

    def open_table_window(self, table_name):
        window = tk.Toplevel(self.master)
        window.title(f"Insertar datos en {table_name}")
        window.geometry("600x400")

        frame = tk.Frame(window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Obtener estructura de la tabla
        columns = self.get_table_structure(table_name)

        # Crear campos de entrada
        entries = []
        for i, col in enumerate(columns):
            tk.Label(frame, text=col).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(frame, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        # Botón para insertar datos
        tk.Button(frame, text="Insertar", command=lambda: self.insert_data(table_name, columns, entries)).grid(
            row=len(columns), column=0, columnspan=2, pady=10)

    def get_table_structure(self, table_name):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(f"DESCRIBE {table_name}")
            return [column[0] for column in cursor.fetchall()]
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al obtener la estructura de la tabla: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def insert_data(self, table_name, columns, entries):
        values = [entry.get() for entry in entries]
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Éxito", "Datos insertados correctamente")
            for entry in entries:
                entry.delete(0, tk.END)
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al insertar datos: {error}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


root = tk.Tk()
gui = NorthwindGUI(root)
root.mainloop()