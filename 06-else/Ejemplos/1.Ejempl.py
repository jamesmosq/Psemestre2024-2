"""puntuacion = 75

if puntuacion >= 90:
    print("A")
elif puntuacion >= 80:
    print("B")
elif puntuacion >= 70:
    print("C")
elif puntuacion >= 60:
    print("D")
else:
    print("F")
    """


puntuacion = 75

if puntuacion >= 90:
    print("A")
else:
    if puntuacion >= 80:
        print("B")
    else:
        if puntuacion >= 70:
            print("C")
        else:
            if puntuacion >= 60:
                print("D")
            else:
                print("F")