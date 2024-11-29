#9. Menús (Menu)
from tkinter import Tk,Menu
root = Tk()
menu_bar = Menu(root)
root.title("Mi Aplicación")  # Asigna un título a la ventana principal
root.geometry('500x400')
root.configure(bg='#228B22')
root.resizable(False,False)
root.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Nuevo")
file_menu.add_command(label="Salir", command=root.quit)
root.mainloop()  # Inicia el bucle de eventos de la ventana
