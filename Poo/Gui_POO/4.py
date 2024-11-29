#4. Entradas de texto (Entry)
from tkinter import Tk,Entry
root = Tk()
root.geometry('400x200')
entry = Entry(root)
entry.pack()
root.mainloop()  # Inicia el bucle de eventos de la ventana