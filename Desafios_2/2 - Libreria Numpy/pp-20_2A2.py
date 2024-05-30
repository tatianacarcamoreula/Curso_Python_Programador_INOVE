# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno:
    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto de la lista de textos
    # El resultado (el len de cada palabra) se debe almacenar
    # en una nueva lista llamada "palabras_len"

    # Lista de string
    palabras = ['Inove', 'casa', 'programacion']

    # Comienza aquí su código
    palabras_len = list(map(lambda x: len(x), palabras))
    print(palabras_len)
    print("terminamos")
    