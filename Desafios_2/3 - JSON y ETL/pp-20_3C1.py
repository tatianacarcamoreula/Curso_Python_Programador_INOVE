# IMPORTANTE: NO borrar los comentarios

def extraer(url):
    import requests
    reponse = requests.get(url)
    data = reponse.json()
    return data

def contar_titulos(data):
    for u in range(1,11):
        titulos[u] = len([1 for t in data if t["userId"] == u and t["completed"] == True])
    return titulos
    
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # URL a la API de jsonplaceholder
    url = "https://jsonplaceholder.typicode.com/todos"

    # Alumno:
    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".

    # 1) API request
    #   Deberá crear una función llamada "extraer"

    # - Entradas (argumentos): 
    #   Está recibe como entrada la variable URL

    # - Objetivo:
    #   Deberá obtener el JSON de la API request
    #   y almacenar el JSON en una variable data

    # - Salidas (parametros):
    #   Retornar la variable data y capturar
    #   su valor en el programa princiapl


    # 2) Contar títulos de todos los usuarios
    #   Deberá crear una función llamada "contar_titulos"

    # - Entradas (argumentos): 
    #   Está recibe como entrada la data
    #   que contiene el diccionario obtenido
    #   de la función extraer

    # - Objetivo:
    #   Deberá recorrer la variable data
    #   y contar cuántos títulos completó 
    #   cada usuario

    #   Deberá alcenar la cantidad de títulos
    #   completados de cada usuario en el diccionario
    #   titulos:
    #   --> las claves del diccionario serán los userId
    #       de cada usuario
    #   --> los valores del diccionario serán la cantidad
    #       de titulos completados de ese usuario (esa clave)

    # - Salidas (parametros):
    #   Retornar la variable titulos y capturar
    #   su valor en el programa principal

    
    # Al finalizar el programa la variable diccionario
    # titulos se verá así:

    # {1: 11, 2: 8, 3: 7, .....}

    # Comienza aquí su código
    titulos = {}

    data = extraer(url)
    titulos = contar_titulos(data)

    print("Titulos:", titulos)

    print("terminamos")