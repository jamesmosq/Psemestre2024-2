nombres = ['Juan', 'María', 'Pedro']
apellidos = ['Pérez', 'González', 'Rodríguez']
edades = [25, 30, 35]
for nombre, apellido, edad in zip(nombres, apellidos, edades):
    print(f"{nombre} {apellido} tiene {edad} años")