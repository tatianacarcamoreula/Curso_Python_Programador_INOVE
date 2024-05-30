# IMPORTANTE: NO borrar los comentarios

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER NOT NULL,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('¡Completemos esta tablita!')
    # Alumno:
    # Llenar la tabla de la secundaria con 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Para insertar cada estudiante debe invocar a la función:
    # --> insert(...)
    # Complete primero el funcionamiento de la función insert
    # Luego deberá invocarla 5 veces aquí
    # para insertar 5 estudiantes nuevos
    
    insert("Tony", 14, 2, "Alberta")
    insert("Teodoro", 12, 1, "José")
    insert("Ana", 18, 6, "Milagros")
    insert("Pepe", 16, 3, "Ema")
    insert("Pepita", 15, 3, "Toto")    

def get_all():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Alumno:
    # Utilizar la sentencia SELECT para obtener
    # todas las filas con todas sus columnas
    # Utilizar fetchall para obtener todos los estudiantes

    # Debería ver los estudiantes que insertó en fill
    
    # Estaba función debe retornar al programa principal
    # los estudiantes de la base de datos obtenidos
    # en la query
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute("SELECT * FROM estudiante")
    data = c.fetchall()
    print(data, "\n")
    conn.close()
    return data


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Alumno:
    # Utilizar la sentencia SELECT para retornar
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # name / age

    # Retornar la lista de estudiantes que retorna la query
    # Puede utilizar fetchall para obtener
    # todos los estudiantes encontrados por la query
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute("""SELECT name, age FROM estudiante 
              WHERE grade = (?);""",(grade,))
    data = c.fetchall()
    conn.commit
    conn.close()
    return data

def insert(name, age, grade, tutor):
    print('¡Nuevos ingresos!\n')
    # Alumno:
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute("""
            INSERT INTO estudiante (name, age, grade, tutor)
            VALUES (?,?,?,?);""", (name, age, grade, tutor))
    conn.commit()
    conn.close()
    
    
def modify(id, name):
    print('Modificando la tabla')
    # Alumno:
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" el pasado como parámetro
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute("""UPDATE estudiante SET name = ?
              WHERE id = ?;""", (name, id))
    c.execute("SELECT * FROM estudiante")
    data = c.fetchall()
    print(data, "\n")
    conn.commit
    conn.close
    return data


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Crear y reinciar la base de datos (DB)
    create_schema()

    # Alumno:
    # Complete el comportamiento de "fill"
    # y luego descomentela para su uso
    fill()

    # Alumno:
    # Complete el comportamiento de "get_all"
    # y luego descomentela para su uso
    estudiantes = get_all()

    # Alumno:
    # Complete el comportamiento de "search_by_grade"
    # y luego descomentela para su uso
    grade = 3
    estudiantes = search_by_grade(grade)
    print(f"Estudiantes de grado {grade}:")
    print(estudiantes, "\n")

    # Alumno:
    # Complete el comportamiento de "modify"
    # y luego descomentela para su uso
    name = 'Tomas'
    id = 2
    modify(id, name)
