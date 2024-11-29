import tkinter as tk

class ShoppingList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de compras")

        # Crear el widget Listbox
        self.listbox = tk.Listbox(self, width=30, height=10)
        self.listbox.pack(padx=10, pady=10)

        # Agregar elementos a la lista
        self.items = ["Manzanas", "Peras", "Plátanos", "Leche", "Huevos", "Pan"]
        for item in self.items:
            self.listbox.insert(tk.END, item)

        # Crear un Entry y un botón para agregar nuevos elementos
        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=5)

        self.add_button = tk.Button(self, text="Agregar", command=self.add_item)
        self.add_button.pack(padx=10, pady=5)

        # Crear un botón para eliminar elementos seleccionados
        self.remove_button = tk.Button(self, text="Eliminar", command=self.remove_item)
        self.remove_button.pack(padx=10, pady=5)

    def add_item(self):
        new_item = self.entry.get().strip()
        if new_item:
            self.listbox.insert(tk.END, new_item)
            self.entry.delete(0, tk.END)

    def remove_item(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)

if __name__ == "__main__":
    app = ShoppingList()
    app.mainloop()