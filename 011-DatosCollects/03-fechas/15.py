from datetime import datetime

# fechas
fecha1 = datetime(1986, 8, 9)
fecha2 = datetime(2024, 9, 27)

# Calcular la diferencia
diferencia = fecha2 - fecha1

# Obtener los años de la diferencia
anios_dif = diferencia.days // 365

# Mostrar el resultado
print("Diferencia en años:", anios_dif)
