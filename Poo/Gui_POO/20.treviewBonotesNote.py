import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AplicacionEjemplo:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Treeview, Pestañas y Botones")
        self.root.geometry("600x400")

        # Crear el Notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        # Primera pestaña: Treeview
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Treeview")
        self.crear_treeview()

        # Segunda pestaña: Botones
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Botones")
        self.crear_botones()

    def crear_treeview(self):
        # Crear el Treeview
        self.tree = ttk.Treeview(self.tab1, columns=("Nombre", "Edad", "Ciudad"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Ciudad", text="Ciudad")
        self.tree.pack(expand=True, fill="both")

        # Agregar algunos datos de ejemplo
        datos = [
            ("Ana García", "28", "Madrid"),
            ("Juan López", "35", "Barcelona"),
            ("María Rodríguez", "42", "Valencia")
        ]
        for item in datos:
            self.tree.insert("", "end", values=item)

        # Botón para agregar elemento
        ttk.Button(self.tab1, text="Agregar Elemento", command=self.agregar_elemento).pack(pady=10)

    def crear_botones(self):
        ttk.Button(self.tab2, text="Botón 1", command=lambda: self.mostrar_mensaje("Botón 1")).pack(pady=10)
        ttk.Button(self.tab2, text="Botón 2", command=lambda: self.mostrar_mensaje("Botón 2")).pack(pady=10)
        ttk.Button(self.tab2, text="Botón 3", command=lambda: self.mostrar_mensaje("Botón 3")).pack(pady=10)

    def agregar_elemento(self):
        # En una aplicación real, aquí se abriría un diálogo para ingresar datos
        nuevo_elemento = ("Nuevo Usuario", "30", "Sevilla")
        self.tree.insert("", "end", values=nuevo_elemento)

    def mostrar_mensaje(self, boton):
        messagebox.showinfo("Mensaje", f"Has presionado el {boton}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionEjemplo(root)
    root.mainloop()