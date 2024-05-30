# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Lambda expression
    # Alumno:
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro
    # Esa función lambda deberá almacenarse en una variable
    # llamada "elevar_cuadrado"

    # 2)
    # Utilice la función map para mapear la función lambda
    # "elevar_cuadrado" cada una lista "numeros"
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista llamada "numeros_potencia"

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # Comienza aquí su código
    
    elevar_cuadrado = lambda x: x**2
    numeros_potencia = list(map(elevar_cuadrado, numeros))
    print(numeros_potencia)    

    print("terminamos")