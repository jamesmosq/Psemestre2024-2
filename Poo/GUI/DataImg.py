import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import mysql.connector
import os
import shutil
from PIL import Image, ImageTk

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gestión de Empleados")

        # Configuración de la conexión a la base de datos
        self.db_config = {
            "host": "localhost",
            "user": "root",
            "password": "base1234",
            "database": "northwind"
        }

        # Frame principal
        main_frame = tk.Frame(master, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame información empleado
        info_frame = tk.LabelFrame(main_frame, text="Información del Empleado", padx=10, pady=10)
        info_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.labels = ["ID:", "Apellido:", "Nombre:", "Fecha de Nacimiento (YYYY-MM-DD):", "Notas:"]
        self.entries = []

        for i, label in enumerate(self.labels):
            tk.Label(info_frame, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(info_frame, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
            self.entries.append(entry)

        # El campo ID no será de solo lectura para permitir la búsqueda
        self.entries[0].config(state='normal')

        # Botón de búsqueda por ID
        self.search_button = tk.Button(info_frame, text="Buscar por ID", command=self.search_by_id)
        self.search_button.grid(row=len(self.labels), column=0, columnspan=2, pady=10)

        # Frame de la foto
        photo_frame = tk.LabelFrame(main_frame, text="Foto del Empleado", padx=10, pady=10)
        photo_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.image_path = ""
        self.image_button = tk.Button(photo_frame, text="Seleccionar Foto", command=self.select_image)
        self.image_button.pack(pady=5)

        self.image_label = tk.Label(photo_frame)
        self.image_label.pack(pady=5)

        # Frame de botones CRUD
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.create_button = tk.Button(button_frame, text="Crear", command=self.create_employee)
        self.create_button.pack(side=tk.LEFT, padx=5)

        self.read_button = tk.Button(button_frame, text="Leer", command=self.read_employee)
        self.read_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(button_frame, text="Actualizar", command=self.update_employee)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(button_frame, text="Eliminar", command=self.delete_employee)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Treeview de mostrar empleados
        tree_frame = tk.Frame(main_frame)
        tree_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Apellido", "Nombre", "Fecha de Nacimiento", "Foto", "Notas"),
                                 show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
        self.tree.heading("Foto", text="Foto")
        self.tree.heading("Notas", text="Notas")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Configurar expansión de filas y columnas
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)

        # Cargar datos iniciales
        self.load_employees()

    def search_by_id(self):
        employee_id = self.entries[0].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para buscar.")
            return

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SELECT * FROM Employees WHERE EmployeeID = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()

            if employee:
                self.populate_fields(employee)
            else:
                messagebox.showinfo("Información", "No se encontró un empleado con ese ID.")

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al buscar empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def populate_fields(self, employee):
        # Cargar datos en los campos de entrada
        self.entries[0].delete(0, tk.END)
        self.entries[0].insert(0, employee[0])
        self.entries[1].delete(0, tk.END)
        self.entries[1].insert(0, employee[1])
        self.entries[2].delete(0, tk.END)
        self.entries[2].insert(0, employee[2])
        self.entries[3].delete(0, tk.END)
        self.entries[3].insert(0, employee[3].strftime('%Y-%m-%d') if employee[3] else '')
        self.entries[4].delete(0, tk.END)
        self.entries[4].insert(0, employee[5])

        # Manejar la imagen
        self.image_path = employee[4]
        if self.image_path:
            full_path = os.path.abspath(self.image_path)
            if os.path.exists(full_path):
                try:
                    image = Image.open(full_path)
                    image.thumbnail((100, 100))
                    photo = ImageTk.PhotoImage(image)
                    self.image_label.config(image=photo)
                    self.image_label.image = photo
                except Exception as e:
                    print(f"Error al cargar la imagen: {e}")
                    self.image_label.config(image="")
            else:
                self.image_label.config(image="")
        else:
            self.image_label.config(image="")

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def create_employee(self):
        last_name = self.entries[1].get()
        first_name = self.entries[2].get()
        birth_date = self.entries[3].get()
        notes = self.entries[4].get()

        if not self.image_path:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una imagen.")
            return

        if not os.path.exists('img'):
            os.makedirs('img')

        file_name = os.path.basename(self.image_path)
        new_image_path = os.path.join('img', file_name)
        shutil.copy(self.image_path, new_image_path)

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = """INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (last_name, first_name, birth_date, new_image_path, notes)

            cursor.execute(query, values)
            connection.commit()

            messagebox.showinfo("Éxito", "Empleado agregado correctamente")
            self.clear_entries()
            self.load_employees()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al agregar empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un empleado.")
            return

        employee_id = self.tree.item(selected_item)['values'][0]

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SELECT * FROM Employees WHERE EmployeeID = %s"
            cursor.execute(query, (employee_id,))
            employee = cursor.fetchone()

            if employee:
                self.populate_fields(employee)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al leer empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_employee(self):
        employee_id = self.entries[0].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un empleado para actualizar.")
            return

        last_name = self.entries[1].get()
        first_name = self.entries[2].get()
        birth_date = self.entries[3].get()
        notes = self.entries[4].get()

        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            if self.image_path:
                if not os.path.exists('img'):
                    os.makedirs('img')
                file_name = os.path.basename(self.image_path)
                new_image_path = os.path.join('img', file_name)
                shutil.copy(self.image_path, new_image_path)

                query = """UPDATE Employees 
                           SET LastName = %s, FirstName = %s, BirthDate = %s, Photo = %s, Notes = %s
                           WHERE EmployeeID = %s"""
                values = (last_name, first_name, birth_date, new_image_path, notes, employee_id)
            else:
                query = """UPDATE Employees 
                           SET LastName = %s, FirstName = %s, BirthDate = %s, Notes = %s
                           WHERE EmployeeID = %s"""
                values = (last_name, first_name, birth_date, notes, employee_id)

            cursor.execute(query, values)
            connection.commit()

            messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
            self.clear_entries()
            self.load_employees()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al actualizar empleado: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_employee(self):
        employee_id = self.entries[0].get()
        if not employee_id:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un empleado para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este empleado?"):
            try:
                connection = mysql.connector.connect(**self.db_config)
                cursor = connection.cursor()

                query = "DELETE FROM Employees WHERE EmployeeID = %s"
                cursor.execute(query, (employee_id,))
                connection.commit()

                messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
                self.clear_entries()
                self.load_employees()

            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Error al eliminar empleado: {error}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def load_employees(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SELECT EmployeeID, LastName, FirstName, BirthDate, Photo, Notes FROM Employees"
            cursor.execute(query)
            employees = cursor.fetchall()

            self.tree.delete(*self.tree.get_children())
            for employee in employees:
                self.tree.insert("", "end", values=employee)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al cargar empleados: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
        self.image_path = ""
        self.image_label.config(image="")

root = tk.Tk()
gui = EmployeeGUI(root)
root.mainloop()