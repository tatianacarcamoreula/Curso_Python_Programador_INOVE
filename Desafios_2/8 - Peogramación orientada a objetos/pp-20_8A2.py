# IMPORTANTE: NO borrar los comentarios

# Alumno: Arreglar el código a continuación para que funcione
# en el editor de código:

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_datos(self):
        datos = f"{self.nombre} tiene {self.edad} años"
        return datos


if __name__ == "__main__":
    print("Comencemos a practicar con objetos")
    
    # Crear un nuevo objeto a partir
    # de la clase Persona
    juan = Persona("juan", 30)

    # Obtener los datos de Juan
    datos_juan = juan.obtener_datos()
    print(datos_juan)

    print("terminamos")
