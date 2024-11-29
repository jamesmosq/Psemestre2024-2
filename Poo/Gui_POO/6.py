#6. Cajas de selección (Checkbutton)
from tkinter import Tk
from tkinter import Checkbutton, IntVar
root = Tk()
var = IntVar()  # Variable que guarda el estado del check
check_button = Checkbutton(root, text="Opción", variable=var)
check_button.pack()

root.mainloop()  # Inicia el bucle de eventos de la ventana
