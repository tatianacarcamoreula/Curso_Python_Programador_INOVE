# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno:
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    
    # NOTA: Importar el módulo random y utilizar randrange
    # o randint para generar números aleatorios.
    #https://docs.python.org/3/library/random.html

    # Comienza aquí su código
    import random
    dias_mes = [random.randint (1, 30) for x in range (10)]
    print(dias_mes)


    print("terminamos")