import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# 1. showinfo()
messagebox.showinfo("Información", "Este es un mensaje informativo.")

# 2. showwarning()
messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")

# 3. showerror()
messagebox.showerror("Error", "Este es un mensaje de error.")

# 4. askquestion()
respuesta = messagebox.askquestion("Pregunta", "¿Estás seguro?")
print(f"Respuesta: {respuesta}")  # 'yes' o 'no'

# 5. askokcancel()
respuesta = messagebox.askokcancel("Confirmar", "¿Quieres continuar?")
print(f"Respuesta: {respuesta}")  # True o False

# 6. askyesno()
respuesta = messagebox.askyesno("Sí o No", "¿Deseas guardar los cambios?")
print(f"Respuesta: {respuesta}")  # True o False

# 7. askyesnocancel()
respuesta = messagebox.askyesnocancel("Opciones", "¿Quieres guardar antes de salir?")
print(f"Respuesta: {respuesta}")  # True, False o None

# 8. askretrycancel()
respuesta = messagebox.askretrycancel("Reintentar", "La operación falló. ¿Quieres reintentar?")
print(f"Respuesta: {respuesta}")  # True o False

root.mainloop()