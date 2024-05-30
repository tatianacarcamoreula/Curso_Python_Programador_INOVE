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

    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # La nueva lista convertida se deberá llamar "lista_convertida"

    # Este programa se comportará como un un conversor string --> int
    # Debe utilizar la función int()

    # ¡Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # y reemplazar dicho str "no numérico" por 0

    # TIP: Recomendamos ver el método "isdigit()" de strings
    # para identificar si una variable puede transformarse a número.

    lista_numeros_str = ['5', '2', '3', '', '7', 'NaN']

    # Resultado esperado:
    # [5, 2, 3, 0, 7, 0]

    # Comienza aquí su código
    lista_convertida = [int(x) if x.isdigit() else 0 for x in lista_numeros_str]
    print(lista_convertida)

    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? ¿Sorprendente no?
    
    lista_convertida_negativa = [-x if x % 2 == 0 else x for x in lista_convertida]
    print(lista_convertida_negativa)
    
    print("terminamos")