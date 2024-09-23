# 4.IndexError: Lista de tareas con acceso a índice inexistente
def mostrar_tarea(tareas, indice):
    print(f"Tarea seleccionada: {tareas[indice]}")

tareas = ["Comprar víveres", "Lavar ropa", "Estudiar Python"]
mostrar_tarea(tareas, 3)  # Error: el índice 3 no existe en la lista