from tkinter import Tk
root = Tk()  # Creas la ventana principal
root.geometry('600x400')
root.attributes('-alpha',0.50)
root.configure(bg='#00CED1') # se recomienda cargar configuraciiones basicas al inicio
root.title('Mi primera ventana') # title
root.resizable(False,False)
root.mainloop()  # Inicia el bucle de eventos de la ventana
root.attributes('-topmost',True)  # Coloca la ventana en primer plano
root.attributes('-zoomed',True)  # Coloca la ventana maximizada
root.attributes('-iconic',True)  # Coloca la ventana en estado minimizado


#1. Ventana principal (Tk)
