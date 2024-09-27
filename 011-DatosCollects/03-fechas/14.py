from datetime import datetime
fecha1 = datetime(2023, 9, 15)
fecha2 = datetime(2023, 9, 20)

if fecha1 < fecha2:
    print("fecha1 es anterior a fecha2")
elif fecha1 > fecha2:
    print("fecha1 es posterior a fecha2")
else:
    print("Las fechas son iguales")