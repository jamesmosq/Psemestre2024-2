from datetime import datetime, date, time, timedelta



# Obtener la fecha actual
fecha = datetime.now()

# Sumar un día para obtener la fecha de mañana
mañana = fecha + timedelta(days=1)

# Mostrar el resultado
print("Mañana:", mañana)



