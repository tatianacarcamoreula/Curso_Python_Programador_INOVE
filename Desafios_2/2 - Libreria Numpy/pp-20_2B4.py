# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # Alumno:
    # ¡IMPORTANTE!
    # Sino pueden resolver el problema con comprensión de listas,
    # resuelvalo con bucles y condiciones comunes como ya conoce.
    # Luego de que su programa funcione puede modificarlo
    # para que utilice comprensión de listas

    # La lista "accesos" contiene los números de ID de personal
    # que desean ingresar a una planta/oficina
    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]
    
    # Utilizar filtrado por comprensión de listas
    # para crea una nueva lista de accesos llamada
    # "personal_1_10" la cual solo contenga
    # los ID de las personas que intentaron ingresar
    # a la planta (definido en accesos)
    # cuyo ID sea menor o igual a 10

    # En su comprensión de listas deberá recorrer los IDs
    # disponibles en accesos y filtrar aquellos IDs que
    # sean mayor a 10, o dicho de otra manera, solo deberá
    # dejar ingresar a la nueva lista "personal_1_10"
    # aquellos IDs que sean menores o igual a 10

    # Resultado esperado:
    # [10, 7, 5, 3, 4]

    # Comienza aquí su código
    personal_1_10 = [x for x in accesos if x <= 10]
    print(personal_1_10)

    print("terminamos")