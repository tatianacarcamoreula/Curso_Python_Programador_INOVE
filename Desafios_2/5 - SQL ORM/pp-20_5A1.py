# IMPORTANTE: NO borrar los comentarios

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///productos.db")
base = declarative_base()


class Remeras(base):
    __tablename__ = "remeras"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    talle = Column(String)


def create_schema():
    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos
    base.metadata.drop_all(engine)

    # Crear las tablas
    base.metadata.create_all(engine)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    create_schema()

    # Alumno:
    # Arreglar el código a continuación para que funcione
    # en el editor de código.
    # Observe atentamente como se genera la base de datos
    # y como se crea la tabla en ella para encontrar el error

    # Conectarse a la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear una nueva remera
    remera_deportiva = Remeras(name="deportiva", talle="L")
    remera_larga = Remeras(name="manga-larga", talle="XL")

    # Agregar la nacionalidad a la DB
    session.add(remera_deportiva)
    session.add(remera_larga)
    session.commit()

    print("terminamos")
