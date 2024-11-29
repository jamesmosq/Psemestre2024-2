#13. Scrollbar (Barra de desplazamiento)
from tkinter import Tk
root = Tk()
from tkinter import Scrollbar
scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")
root.mainloop()  # Inicia el bucle de eventos de la ventana
