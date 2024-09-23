#Ejercicio 7: Juego de preguntas y respuestas
respuesta = ""

while respuesta.lower() != "salir":
    respuesta = input("Escribe algo (escribe 'salir' para terminar): ")
    if respuesta.lower() == "salir":
        print("¡Adiós!")
    else:
        print("Tú dijiste:", respuesta)
