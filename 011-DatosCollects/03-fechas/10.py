from datetime import datetime, date, time, timedelta

# Obtener la fecha y hora actual
fecha = datetime.now()

# Sumar un día para obtener la fecha de mañana
mañana = fecha + timedelta(days=3)

# Calcular la diferencia entre mañana y hoy
diferencia = mañana - fecha

# Mostrar la diferencia
print("Diferencia:", diferencia)


# Días de la semana (0 = lunes, 6 = domingo)
print("Día de la semana:", fecha.weekday())