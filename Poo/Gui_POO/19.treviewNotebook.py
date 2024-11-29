import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Pestañas con Treeview")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Pestaña con Treeview")
notebook.add(tab2, text="Pestaña 2")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# Crear el Treeview dentro de la primera pestaña (tab1)
tree = ttk.Treeview(tab1, columns=("ID", "Nombre", "Edad"), show="headings")

# Definir las cabeceras de las columnas
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")

# Insertar datos en el Treeview
tree.insert("", "end", values=(1, "Juan", 25))
tree.insert("", "end", values=(2, "María", 30))
tree.insert("", "end", values=(3, "Pedro", 40))

# Empaquetar el Treeview dentro de la pestaña
tree.pack(expand=True, fill="both", padx=10, pady=10)

# Añadir contenido a la segunda pestaña
label2 = tk.Label(tab2, text="Contenido de la Pestaña 2")
label2.pack(padx=10, pady=10)

# Iniciar el bucle de eventos
root.mainloop()
