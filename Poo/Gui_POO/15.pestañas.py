import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry('400x300')
root.title("Ejemplo de pestañas")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Pestaña 1")
notebook.add(tab2, text="Pestaña 2")
notebook.add(tab3, text="Pestaña 3")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both")

# Añadir contenido a las pestañas
label1 = tk.Label(tab1, text="Contenido de la Pestaña 1")
label1.pack(padx=10, pady=10)

label2 = tk.Label(tab2, text="Contenido de la Pestaña 2")
label2.pack(padx=10, pady=10)

label3 = tk.Label(tab3, text="Contenido de la Pestaña 3")
label3.pack(padx=10, pady=10)

# Iniciar el bucle de eventos
root.mainloop()
