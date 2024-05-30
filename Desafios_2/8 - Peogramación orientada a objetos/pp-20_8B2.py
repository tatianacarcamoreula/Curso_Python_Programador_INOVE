# IMPORTANTE: NO borrar los comentarios

class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def agregar_puntaje(self, puntaje):
        self.puntaje += puntaje
        
    def obtener_puntaje(self):
        return self.puntaje


if __name__ == "__main__":
    print("Comencemos a practicar con objetos")
    # Alumno:
    # A la clase Jugador agrege un método 
    # llamado "agregar_puntaje"
    # el cual reciba por parámetro un número
    # Ese nuḿero se deberá sumar al puntaje
    # almacenado en la variable self.puntaje
    # dentro del objeto
    # A medida que se invoque el método para
    # ir aumentando el valor de puntaje,
    # este deberá ir incrementando (acumulador)

    # Ver los ejemplos a continuación de lo que
    # se espera al utilizar el método:

    jugador1 = Jugador("Laura")

    # Este valor de puntaje debe ser 0
    # Ya que es el valor inicial y no hemos
    # sumado nada hasta ahora
    puntaje = jugador1.obtener_puntaje()
    print("Puntaje inicial:", puntaje)

    # Agregar 10 puntos:
    jugador1.agregar_puntaje(10)

    # Este valor de puntaje debe ser 10
    # Ya que hemos agregado 10 puntos
    puntaje = jugador1.obtener_puntaje()
    print("Nuevo puntaje del jugador:", puntaje)
    
    # Agregar 5 puntos:
    jugador1.agregar_puntaje(5)

    # Este valor de puntaje debe ser 15
    # Ya que hemos agregado 5 puntos
    puntaje = jugador1.obtener_puntaje()
    print("Nuevo puntaje del jugador:", puntaje)


    print("terminamos")
