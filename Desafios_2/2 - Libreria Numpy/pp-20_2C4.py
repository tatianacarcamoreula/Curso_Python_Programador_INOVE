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

    # La lista "padron" contiene las iniciales de los nombres
    # que se aceptan en el padron
    padron = ['A', 'E', 'J', 'T']

    # La lista "nombres" con tiene la lista de nombres que se
    # debe filtrar según la lista padron.
    nombres = ["Tamara", 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']


    # Utilizar filtrado por comprensión de listas
    # para crea una nueva lista de accesos llamada
    # "nombres_padron" la cual solo contenga
    # los nombres de las personas cuyas iniciales
    # estén contempladas en "padron".

    # En su comprensión de listas deberá recorrer los nombres
    # disponibles en "nombres" y solo deberá
    # dejar ingresar a la nueva lista "nombres_padron"
    # aquellos nombres cuyas iniciales se encuentren
    # disponibles en "padron".

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]

    # Comienza aquí su código
    # nombres_filtrados = [......]
    nombres_padron = [x for x in nombres if x[0] in padron]
    print(nombres_padron)


    print("terminamos")