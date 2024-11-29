#8. Listbox (Lista de selección)
from tkinter import Tk,Listbox
root = Tk()
listbox = Listbox(root)
listbox.insert(1, "Elemento 1")
listbox.insert(2, "Elemento 2")
listbox.insert(3, "Elemento 3")
listbox.pack()
root.mainloop()  # Inicia el bucle de eventos de la ventana
