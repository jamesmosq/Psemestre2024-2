import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejemplo avanzado de Frames en Tkinter")

        # Crear el frame principal
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Dividir el frame principal en dos partes
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, padx=10, fill="both", expand=True)

        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.LEFT, padx=10, fill="both", expand=True)

        # Crear widgets en el frame izquierdo
        self.label = tk.Label(self.left_frame, text="Etiqueta en el frame izquierdo")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.left_frame)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.left_frame, text="Clic aquí", command=self.on_button_click)
        self.button.pack(pady=10)

        # Crear widgets en el frame derecho
        self.text_area = tk.Text(self.right_frame, width=30, height=10)
        self.text_area.pack(pady=10)

        self.combobox = ttk.Combobox(self.right_frame, values=["Opción 1", "Opción 2", "Opción 3"])
        self.combobox.pack(pady=10)

        self.checkbox = tk.Checkbutton(self.right_frame, text="Casilla de verificación")
        self.checkbox.pack(pady=10)

    def on_button_click(self):
        text = self.entry.get()
        self.text_area.insert(tk.END, f"{text}\n")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()