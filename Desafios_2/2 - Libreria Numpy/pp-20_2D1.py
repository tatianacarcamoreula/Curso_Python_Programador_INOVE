# IMPORTANTE: NO borrar los comentarios
import random

'''
Enunciado:
Se dispone del diccionario "producto" que se utiliza para
traducir el número ID de un producto en su nombre, por ejemplo:

producto 556070 --> nombre 'Auto'

Por otro lado se dispone de la lista de productos comprados "lista_compra_id"
por un cliente con sus códigos de productos

Su objetivo es crear una lista nueva llamada "lista_compra_productos" 
que sea la transformación de la lista "lista_compra_id",
que en vez de tener los "ID" de los productos tenga el "nombre"
de cada producto según su id.
'''

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno:
    # 1) Iterar sobre la lista "lista_compra_id" para generar 
    # la nueva lista "lista_compra_productos" utilizando
    # comprension de listas como generador

    # 2) En cada iteración acceder al diccionario para traducir
    # el ID del producto a nombre de producto.

    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados en el sistema, en esos casos se debe
    # almacenar en la lista la palabra 'NaN', para ello debe hacer
    # uso de condicionales.    
    # Para evaluar si un ID se encuentra registrado o no
    # en el sistema, es decir, en el diccionario "producto"
    # puede hacer uso del operador "in" o del método "get"

    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    # de una base de datos como veran más adelante.
    # Tambien se lo conoce como el proceso de transformar
    # variable numéricas en categóricas en análisis de datos.

    producto = {
            556070: 'Auto',
            704060: 'Moto',
            42135: 'Celular',
            1264: 'Bicicleta',
            905045: 'Computadora',
            }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    lista_compra_productos = [producto[x] if x in producto else "NaN" for x in lista_compra_id]
    print(f"Tu lista de compras es: {lista_compra_productos}")
    print("terminamos")