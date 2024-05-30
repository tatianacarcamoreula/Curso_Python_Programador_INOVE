# IMPORTANTE: NO borrar los comentarios
import random


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno:
    # ¡IMPORTANTE!
    # Sino pueden resolver el problema con comprensión de listas,
    # resuelvalo con bucles y condiciones comunes como ya conoce.
    # Luego de que su programa funcione puede modificarlo
    # para que utilice comprensión de listas

    # 1) 
    # Generar una lista de 3 numéros aleatorios con random (pueden repetirse),
    # Estos 3 nuḿeros deben estar comprendidos entre 1 al 10 inclusive.
    # La lista generada deberá llamarse "numeros"

    # 2) 
    # Luego de generar la lista sumar los números y ver si el resultado
    # de la suma es menor o igual a 21
    #  --> Si el número es menor o igual a 21 debe colocar la variable:
    #      perdiste = False
    #  --> Si el número es mayor a 21 debe colocar la variable:
    #      perdiste = True

    perdiste = False
    
    # Comienza aquí su código
    
    print("""Sí la suma total de los tres números tocados es
menor o igual a 21, ganaste, sino, perdiste.\n""")
    
    numeros = [random.randint (1, 10) for x in range (3)]
    print(f"Te tocó {numeros}")
    suma = [sum(numeros)]
    """if sum(numeros)<= 21:
        perdiste = False
    else:
        perdiste = True"""
    
    suma =  [perdiste == False if x <= 21 else perdiste == True  for x in suma]
    print(perdiste)
    
    valor = [print(f"La suma total es: {sum(numeros)} ¡Perdiste\n") if perdiste == True 
                    else print(f"La suma total es: {sum(numeros)} ¡Ganaste!\n")]

    print("terminamos")