# IMPORTANTE: NO borrar los comentarios

# https://extendsclass.com/sqlite-browser.html

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///secundaria.db")
base = declarative_base()


class Tutor(base):
    __tablename__ = "tutor"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return f"Tutor: {self.name}"


class Estudiante(base):
    __tablename__ = "estudiante"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Integer)
    tutor_id = Column(Integer, ForeignKey("tutor.id"))

    tutor = relationship("Tutor")

    def __repr__(self):
        return f"Estudiante: {self.name}, edad {self.age}, grado {self.grade}, tutor {self.tutor.name}"



def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos
    base.metadata.drop_all(engine)

    # Crear las tablas
    base.metadata.create_all(engine)


def fill():
    print('¡Completemos esta tablita!')
    # Alumno:
    # Llenar la tabla de la secundaria con 2 tutores
    # Cada tutor tiene los campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del tutor (puede ser solo nombre sin apellido)

    # Para insertar cada estudiante debe invocar a la función:
    # --> insert_tutor(...)
    # Complete primero el funcionamiento de la función insert_tutor
    # Luego deberá invocarla 2 veces aquí
    # para insertar 2 tutores nuevos

    # Llenar la tabla de la secundaria con 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Para insertar cada estudiante debe invocar a la función:
    # --> insert_estudiante(...)
    # Complete primero el funcionamiento de la función insert_estudiante
    # Luego deberá invocarla 5 veces aquí
    # para insertar 5 estudiantes nuevos
    insert_tutor("Julio")
    insert_tutor("Miranda")

    insert_estudiante("Jolanda", 12, 1, "Julio")
    insert_estudiante("Anita", 14, 3, "Julio")
    insert_estudiante("José", 17, 5, "Miranda")
    insert_estudiante("Paublo", 16, 4, "Julio")
    insert_estudiante("Ashelen", 18, 6, "Miranda")
    
    
def get_all():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Alumno:
    # Utilizar la sentencia all() para obtener
    # todos los estudiantes
    
    # Estaba función debe retornar al programa principal
    # los estudiantes de la base de datos obtenidos
    # en la query --> una lista de objetos Estudiantes
    Session = sessionmaker(bind=engine)
    session = Session()
    
    query = session.query(Estudiante)
    estudiantes = query.all()
    
    print(estudiantes)
    return estudiantes


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Alumno:
    # Utilizar la sentencia filter() para retornar
    # aquellos estudiantes que se encuentra en en año "grade"

    # Retornar la lista de estudiantes que retorna la query
    # Puede utilizar all() para obtener
    # todos los estudiantes encontrados por la query
    Session = sessionmaker(bind=engine)
    session = Session()
    
    busqueda = session.query(Estudiante).filter(Estudiante.grade == grade).all()
    
    return busqueda

def insert_tutor(name):
    print('¡Nuevo estudiante!')
    # Alumno:
    # Crear un nuevo objeto Tutor utilizando los parámetros
    # de la función (name)
    
    # Guardar el objeto en la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()
    
    persona_tutor = Tutor(name = name) 
    
    session.add(persona_tutor)
    session.commit()


def insert_estudiante(name, age, grade, tutor):
    print('¡Nuevo estudiante!')
    # Alumno:
    # Primero buscar en la base de datos el objeto
    # "Tutor" correspondiente al nombre del tutor pasado por
    # por parámetro

    # Crear un nuevo objeto Estudiante utilizando los parámetros
    # de la función (name, age, grade) y el objeto tutor
    
    # Guardar el objeto en la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()
    
    query_tutor = session.query(Tutor).filter(Tutor.name == tutor)
    tutor = query_tutor.first()
    if tutor is None:
        print(f"No exixte el tutor de {name}. Intente de nuevo.")
        return
    
    estudiante = Estudiante(name = name, age = age, grade = grade, tutor = tutor) 
    
    session.add(estudiante)
    session.commit()


def modify(id, name):
    print('Modificando la tabla')
    # Alumno:
    # Modificar el estudiante cuyo id sea el "id"
    # pasado como parámetro.
    # Modificar su nombre por "name" el pasado como parámetro
    # Almacenar el cambio en la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()
    
    estudiante = session.query(Estudiante).filter(Estudiante.id == id).update({Estudiante.name: name})
    session.commit()
    
    print((session.query(Estudiante)).all())
    return estudiante
    
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
    print(estudiantes)

    # Alumno:
    # Complete el comportamiento de "modify"
    # y luego descomentela para su uso
    name = 'Tomas'
    id = 2
    modify(id, name)
