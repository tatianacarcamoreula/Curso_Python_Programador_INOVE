# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno:
    # Debe transformar el siguiente código resuelto
    # con bucles y condicionales tradicionales
    # en una comprensión de lista con condicionales

    # Código a transformar
    edades = [10, 25, 49, 16, 60]
    mayores_edad = []

    # Código que almacena en mayores_edad:
    # 1 -> Si la persona es mayor o igual de 18 años
    # 0 -> Si la persona es menos de 18 años
    for edad in edades:
        if edad >= 18:
            mayores_edad.append(1)
        else:
            mayores_edad.append(0)
    
    print("Mayores de edad:", mayores_edad)

    # Alumno:
    # Debe realizar un programa que haga lo mismo,
    # utilizando comprensión de listas
    # generando una nueva lista que se llame:
    # "mayores_edad_por_compresion"

    # El resultado esperado es:
    # [0, 1, 1, 0, 1]

    # Comienza aquí su código
    mayores_edad_por_compresion = [1 if x >18 else 0 for x in edades]
    print(f"Mayores de edad (usando compresión): {mayores_edad_por_compresion}")

    print("terminamos")