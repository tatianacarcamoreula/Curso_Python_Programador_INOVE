# IMPORTANTE: NO borrar los comentarios


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Diccionario donde se encuentra almacenado
    # los datos de compra de Juan Perez

    compra_juan = {
        "cliente": {
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juanperez@mail.com"
        },
        "fecha": "2022-03-23",
        "productos": [
            {
            "nombre": "Camiseta deportiva",
            "precio": 20.99,
            "cantidad": 2
            },
            {
            "nombre": "Zapatillas de running",
            "precio": 79.99,
            "cantidad": 1
            },
            {
            "nombre": "Mallas deportivas",
            "precio": 12.99,
            "cantidad": 3
            }
        ],
        "envio": {
            "direccion": "Calle Falsa 123",
            "ciudad": "Buenos Aires",
            "pais": "Argentina",
            "codigo_postal": "1000"
        },
        "monto": 135.95
    }

    # Alumno:
    # Se le solicitará acceder a datos de
    # ese diccionario y que cada uno de ellos
    # lo almacene en la variable solicitada

    # Estude bien como está armado el diccionario
    # y analice en cada caso como debe acceder
    # a los datos por clave, valor, posición en una lista
    # para recorrer la estructura de datos

    # 1) Obtener el email del cliente
    # Acceda al email del cliente dentro del diccionario
    # y almacene su valor en una variable llamada "email"

    # 2) Obtener la cantidad de camisetas compradas
    # Acceda a la cantidad de camisas compras en la compra
    # que se encuentra disponible dentro del diccionario
    # y almacene su valor en una variable llamada "cantidad_camisetas"

    # 3) Obtener el monto total de la compra
    # Acceda al monto total de la compra dentro del diccionario
    # y almacene su valor en una variable llamada "monto"

    # Comienza aquí su código
    email = compra_juan["cliente"]["email"]
    
    cantidad_camisetas = compra_juan["productos"][0]["cantidad"]
    
    monto = compra_juan["monto"]
    
    print(f"""El email de Juan es: {email}. El compró {cantidad_camisetas} camisetas
y como monto total de toda la compra gastó {monto}""")
    
    print("terminamos")