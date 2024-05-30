# IMPORTANTE: NO borrar los comentarios

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# IMPORTANTE
# Debe utilizar la base de datos "libreria.db"
# que se encuentra disponible en el repositorio de clase

# Estructura de la base de datos:
# * Tabla autor *
# - id [integer] --> id del autor --> número (autoincremental)
# - name [text] --> nombre del autor

# * Tabla libro *
# - id [integer] --> id del libro --> número (autoincremental)
# - titulo [text] --> Título del libro
# - cantidad_paginas [integer] --> Cantidad de páginas del libro
# - autor [relationship] --> Nombre del autor del libro

engine = sqlalchemy.create_engine("sqlite:///libreria.db")
base = declarative_base()

class Autor(base):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return f"autor: {self.name}"
    
class Libro(base):
    __tablename__ = "libro"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    cantidad_paginas = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autor.id"))

    autor = relationship("Autor")

    def __repr__(self):
        return f"Libro: {self.titulo}; cantidad de paginas: {self.cantidad_paginas}; y {self.autor}. "

base.metadata.create_all(engine)
   
   
def get_all():
    print('Comprobemos su contenido, ¿qué hay en la tabla?\n')
    # Alumno:
    # Obtener todos los libros de la base de datos
   
    # Estaba función debe retornar al programa principal
    # los libros de la base de datos obtenidos
    # en la query
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    query = session.query(Libro).all()
    
    print("LISTA DE LIBROS:")
    print(query, "\n")
    
    return query


def search_by_autor(autor):
    print('¡Operación búsqueda!\n')
    # Alumno:
    # Utilizar la sentencia filter para retornar
    # aquellos libros que hayan sido escritos por
    # el autor pasado por parámetro
    
    # Retornar la lista de libros que retorna la query
    # Puede utilizar all() para obtener
    # todos los libros encontrados por la query

    Session = sessionmaker(bind=engine)
    session = Session()
    
    query = session.query(Libro).join(Autor).filter(Autor.name == autor).all()
    
    print(f"Los libros encontrados de {autor} son:")
    for libro in query:
        print(f"* '{libro.titulo}' de {libro.cantidad_paginas} paginas.")
    
    return query


def cantidad_paginas(autor):
    print(f"\n¿Cuántas páginas escribio {autor}?\n")
    # Alumno:
    # Esta función debe retornar la suma de todas
    # las páginas que escribió el autor pasado
    # por parámetro en todos sus libros
    # que haya escrito el autor

    # Recomendamos obtener todos lis libros
    # que haya escrito el autor utilizando filter(..)
    # y luego con un bucle sumar la cantidad de páginas

    # Esta función debe retoronar
    # la cantidad de páginas que el autor
    # a escrito en total
    # ¡DEBE RETORNAR UN ENTERO! (int)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    query = session.query(Libro).join(Autor).filter(Autor.name == autor).all()
    total_paginas = sum([libro.cantidad_paginas for libro in query])
    
    print(f"En total, {autor} escribió {total_paginas} paginas.")
    
    return total_paginas

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python\n")
    get_all()
    search_by_autor("Gabriel Garcia Marquez")
    cantidad_paginas("Gabriel Garcia Marquez")