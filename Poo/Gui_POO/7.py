from tkinter import Tk, Radiobutton, IntVar
#7. Botones de opción (Radiobutton)

root = Tk()  # Crea la ventana principal

# Crea una variable de control para los botones de opción
var = IntVar()

# Crea los botones de opción
radio_button1 = Radiobutton(root, text="Opción 1", variable=var, value=1)
radio_button2 = Radiobutton(root, text="Opción 2", variable=var, value=2)

# Coloca los botones de opción en la ventana
radio_button1.pack()
radio_button2.pack()

root.mainloop()  # Inicia el bucle de eventos de la ventana