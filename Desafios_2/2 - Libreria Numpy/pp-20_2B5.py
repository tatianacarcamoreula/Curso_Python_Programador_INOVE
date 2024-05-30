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

    # La lista "id_validos" contiene los números de ID de personal
    # que están autorizados a ingresar a la planta/oficina
    id_validos = [3, 4, 7, 8, 15]

    # Utilizar filtrado por comprensión de listas
    # para crea una nueva lista de accesos llamada
    # "personal_validado" la cual solo contenga
    # los ID de las personas que intentaron ingresar
    # a la planta (definido en accesos)
    # cuyo ID sea válido.
    # Un ID válido es aquel que se encuentra disponible
    # dentro de la lista "id_validos"

    # ¡Importante! Para validar que un "ID" se encuentra
    # disponible dentro de "id_validos" deberá utilizar
    # el operador "in"

    # En su comprensión de listas deberá recorrer los IDs
    # disponibles en accesos y solo deberá
    # dejar ingresar a la nueva lista "personal_validado"
    # aquellos IDs que se encuentren disponibles en "id_validos"
    # utilizando el un condicional con un operador "in".

    # Resultado esperado:
    # [7, 15, 3, 4]

    # Comienza aquí su código
    personal_validado = [x for x in accesos if x in id_validos]
    print(personal_validado)

    print("terminamos")