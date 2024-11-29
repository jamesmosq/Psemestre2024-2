#14. Treeview (Vista de árbol)
from tkinter import Tk
from tkinter.ttk import Treeview

root = Tk()

# Crear el widget Treeview
tree = Treeview(root, columns=("Columna 1", "Columna 2"), show="headings")

# Definir las cabeceras de las columnas
tree.heading("Columna 1", text="ID")
tree.heading("Columna 2", text="Nombre")

# Insertar datos en las filas
tree.insert("", "end", values=(1, "Elemento 1"))
tree.insert("", "end", values=(2, "Elemento 2"))

tree.pack()

root.mainloop()
