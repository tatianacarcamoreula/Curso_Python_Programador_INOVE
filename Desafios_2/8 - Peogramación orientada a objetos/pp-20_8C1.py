# IMPORTANTE: NO borrar los comentarios

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def obtener_puntaje(self):
        return self.puntaje


    def agregar_puntaje(self, puntos):
        self.puntaje += puntos

class JugadorVip(Jugador):
    def agregar_puntaje(self, puntos):
        self.puntaje += puntos * 2

if __name__ == "__main__":
    print("Comencemos a practicar con objetos")
    # Alumno:
    # Deberá crear una clase nueva llamada
    # "JugadorVip" la cual herede
    # de la clase "Jugador"

    # En esa nueva clase deberá crear
    # el método "agregar_puntaje" sobrecargando
    # al método de la clase "Jugador" (sobre escribiendolo)
    # Es decir, cuando un objeto creado a partir
    # de la clase "JugadorVip" llame al método
    # "agregar_puntaje", el sistema invocará al método
    # definido en "JugadorVip" en vez de "Jugador"

    # Este nuevo método "agregar_puntaje" que usted
    # debe crear en la clase "JugadorVip" sumará
    # el doble de puntos que el método de la clase "Jugador"
    # ... += puntos * 2

    # Ver los ejemplos a continuación de lo que
    # se espera al utilizar el método:

    jugador1 = JugadorVip("Laura")

    # Este valor de puntaje debe ser 0
    # Ya que es el valor inicial y no hemos
    # sumado nada hasta ahora
    puntaje = jugador1.obtener_puntaje()
    print("Puntaje inicial:", puntaje)

    # Agregar 10 puntos:
    jugador1.agregar_puntaje(10)

    # Este valor de puntaje debe ser 20
    # Ya que hemos agregado 10 puntos y se duplican
    # en "agregar_puntaje" de la clase "JugadorVip"
    puntaje = jugador1.obtener_puntaje()
    print("Nuevo puntaje del jugador:", puntaje)
    

    # Agregar 5 puntos:
    jugador1.agregar_puntaje(5)

    # Este valor de puntaje debe ser 30
    # Ya que hemos agregado 5 puntos y se duplican
    # en "agregar_puntaje" de la clase "JugadorVip"
    puntaje = jugador1.obtener_puntaje()
    print("Nuevo puntaje del jugador:", puntaje)


    print("terminamos")
