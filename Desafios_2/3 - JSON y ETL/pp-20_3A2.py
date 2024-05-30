# IMPORTANTE: NO borrar los comentarios

import json
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Alumno: Arreglar el código a continuación para que funcione
    # en el editor de código:

    # JSON String
    json_string = '{"nombre": "Juan", "tarjetas": [] }'
    
    # Transformar el JSON string a diciconario
    diccionario = json.loads(json_string)
    print(diccionario)

    print("terminamos")