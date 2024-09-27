from datetime import datetime, date, time, timedelta

# Crear una fecha y hora actual
fecha_hora = datetime.now()

# Formatear la fecha y hora
formato = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha formateada:", formato)

