# IMPORTANTE: NO borrar los comentarios

import sqlite3

def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect("productos.db")

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("DROP TABLE IF EXISTS remeras;")

    # Ejecutar una query
    c.execute("""
            CREATE TABLE remeras(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [talle] TEXT NOT NULL
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    create_schema()

    # Alumno:
    # Arreglar el código a continuación para que funcione
    # en el editor de código.
    # Observe atentamente como se genera la base de datos
    # y como se crea la tabla en ella para encontrar el error

    # Conectarse a la base de datos
    conn = sqlite3.connect("productos.db")
    c = conn.cursor()

    c.execute("""
        INSERT INTO remeras (name, talle)
        VALUES (?,?);""", ("deportiva", "L"))
    
    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()

    print("terminamos")