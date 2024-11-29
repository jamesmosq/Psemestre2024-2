from tkinter import Tk
from tkinter import Label
root = Tk()

root.geometry('400x200')
root.title("Mi primera ventana")
root.resizable(False,False)
label = Label(root, text="Hola Mundo")
label.pack()  # Empaqueta y coloca el widget en la ventana
root.mainloop()  # Inicia el bucle de eventos de la ventana
#2. Etiquetas (Label)
