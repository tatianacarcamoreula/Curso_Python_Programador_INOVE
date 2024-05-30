# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno:
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar essa lista
    # Lo esperable es que genere una lista de 11 elementos,
    # del 0 al 10 (como el ejer anterior) pero que cada
    # elemento lo multipliquen x5 durante la comprensión de listas.
    # La variable de la nueva lista generada
    # se debe llamar "tabla_5"

    # Comienza aquí su código
    tabla_5 = [x*5 for x in range(11)]
    print(tabla_5)


    print("terminamos")