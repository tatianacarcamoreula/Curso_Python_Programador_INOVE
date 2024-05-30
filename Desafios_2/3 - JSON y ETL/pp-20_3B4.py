# IMPORTANTE: NO borrar los comentarios

def obtener_cambio(data, moneda):
    print("Obtener tipo de cambio de:", moneda)
    
    if moneda in data["rates"]:
        cambio = data["rates"][moneda]
        print(f"El cambio de la moneda {moneda} es {cambio}.")
        return cambio
    else:
        print("No se encuentra esa moneda, intenta con otra.")
        
    # Esta función recibe como parámetro
    # del bloque principal:
    # 1) el diccionario data 
    # 2) la moneda de la cual deseamos obtener el cambio
    
    # Deberá obtener el valor de cambio
    # utilizando data y moneda
    # y retornar el valor de cambio al programa principal 


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # URL a la API de exchangerate
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    # Alumno:
    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver dentro de la clave "rate"
    # se encuentran los tipos de cambio de todas las monedas
    # 2) Cada moneda es una clave (key) dentro de rate, y el tipo
    # de cambio es el valor de esa clave

    # 1) API request
    # Deberá obtener el JSON de la API request
    # y almacenarlo en una variable llamada data

    # 2) Obtener tipo de cambio
    # Deberá completar la función "obtener_cambio"
    # Debe invocar a la función obtener_cambio
    # pasando como parámetro las variables
    # data y moneda
    # Y almacenar el valor de retorno de la función
    # en una variable llamada "cambio"
    
    # Importante:
    # La función obtener_cambio deberá función
    # con cualquier valor válido que se pase
    # por parámetro para moenda

    # Comienza aquí su código
    
    import requests
    import json
    
    reponse = requests.get(url)
    data =reponse.json()
    
    #Por si quiere visualizar los datos de la url
    #print(json.dumps(data, indent = 4))
    
    moneda = "EUR"
    obtener_cambio(data, moneda)
    
    print("terminamos")