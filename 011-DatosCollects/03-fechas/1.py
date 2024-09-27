from datetime import datetime, date, time, timedelta

# Crear una fecha
fecha = date(2023, 9, 23)
print("Fecha:", fecha)

# Crear una hora
hora = time(14, 30, 0)
print("Hora:", hora)

# Crear un datetime (fecha y hora)
fecha_hora = datetime(2023, 9, 23, 14, 30, 0)
print("Fecha y hora:", fecha_hora)

# Obtener la fecha y hora actual
ahora = datetime.now()
print("Ahora:", ahora)

# Formatear una fecha
formato = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha formateada:", formato)

# Parsear una cadena a fecha
fecha_parseada = datetime.strptime("23/09/2023 14:30:00", "%d/%m/%Y %H:%M:%S")
print("Fecha parseada:", fecha_parseada)

# Operaciones con fechas no found
mañana = fecha + timedelta(days=1)
print("Mañana:", mañana)

diferencia = mañana - fecha
print("Diferencia:", diferencia)

# Obtener componentes de la fecha
print("Año:", fecha_hora.year)
print("Mes:", fecha_hora.month)
print("Día:", fecha_hora.day)
print("Hora:", fecha_hora.hour)
print("Minuto:", fecha_hora.minute)

# Días de la semana (0 = lunes, 6 = domingo)
print("Día de la semana:", fecha.weekday())