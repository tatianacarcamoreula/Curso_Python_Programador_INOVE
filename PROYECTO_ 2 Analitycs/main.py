#Importo las librerias correspondientes
import numpy as np
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

#Creo el motor de la base de datos (sqlalchemy)
engine = sqlalchemy.create_engine("sqlite:///ventas_calzados.db")
base = declarative_base()

#Creo la tabla ventas
class Ventas(base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True)
    fecha = Column(String)
    producto_id = Column(Integer)
    pais = Column(String)
    genero = Column(String)
    talle = Column(String)
    precio = Column(String)
    
    def __repr__(self):
        return f"Id: {self.id}, fecha: {self.fecha}, producto_id: {self.producto_id}, pais: {self.pais}, genero: {self.genero}, talle: {self.talle}, precio: {self.precio}"
base.metadata.create_all(engine)

#FUNCIONES:

#Función "read_db()" 
# - encargada de leer todos los datos y almacenarlos en 4 listas, para al finalmete, convertirlos en arrays numpy
def read_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    query = session.query(Ventas).all()
    pais = []
    genero = []
    talle = []
    precio = []
    precio_modificado = []
    for dato in query:
        pais.append(dato.pais)
        genero.append(dato.genero)
        talle.append(dato.talle)
        precio.append(dato.precio)
    
    #le saco $ a precios para volverlo float
    for i in precio:
        b = i.replace("$"," ")
        precio_modificado.append(float(b))
    
    paises=np.array(pais)
    generos=np.array(genero)
    talles=np.array(talle)
    precios=np.array(precio_modificado)
        
    return paises, generos, talles, precios

#Función "obtener_paises_unicos"
# - recibe como parametro el array numpy paises
# - encargada de obtener una lista de los paises que realizaron ventas sin repetirlos
def obtener_paises_unicos(paises):
    paises = np.unique(paises)
    print(f"Paises que realizaron ventas:\n {paises}\n")
    return paises

#Funcion "obtener_ventas_por_pais"
# - recibe como parametro los paises objetivos(los que queremos analizar), los arrays numpy paises y precios 
# - encargada de almacenar en un diccionario lo recaudado de las ventas en cada país
def obtener_ventas_por_pais (paises_objetivo, paises, precios):
    dict_ventas = {}
    for pais in paises_objetivo:
        
        mask = paises == pais
        ventas_pais = sum(precios[mask])
        
        dict_ventas[pais] = ventas_pais     
        
    print(f"Precio total de las ventas:\n {dict_ventas}\n")
    return dict_ventas

#Función "obtener_calzado_mas_vendido_por_pais"
# - recibe como parametro los paises objetivos, y los arrays numpy paises y talles
# - ncargada de almacenar en un diccionario los talles mas vendido dependiendo el país
def obtener_calzado_mas_vendido_por_pais(paises_objetivos, paises, talles):
    dict_talle = {}
    for pais in paises_objetivos:
        
        mask = paises == pais
        talles_pais = talles[mask]
        
        talle, cantidad = np.unique(talles_pais, return_counts= True)
        dict_talle_cantidad = dict(zip(talle, cantidad))            
        dict_talle [pais] = max(dict_talle_cantidad.keys(), key=lambda k: dict_talle_cantidad[k])
        
    print(f"Talles más vendidos por pais:\n {dict_talle}\n")
    return dict_talle


#Función "obtener_ventas_por_genero_pais"
# - obtiene como parametro los paises objetivos, el genero objetivo y los arrays numpy paises y generos
# - encargada de obtener las ventas totales dependiendo el país y el genero
def obtener_ventas_por_genero_pais(paises_objetivos, genero_objetivo, paises, generos):
    dict_genero = {}
    for pais in paises_objetivos:   
        mask = paises == pais
        genero_pais = generos[mask]
        numero_genero = len([1 for genero in genero_pais if genero == genero_objetivo])
        dict_genero[pais] = numero_genero
    print(f"Total de ventas del genero {genero_objetivo}:\n {dict_genero}\n")
    return dict_genero
        
if __name__ == "__main__":
    #llamo a las funciones
    print("\n¡Aquí utilizo mis funciones!\n")
    paises, generos, talles, precios = read_db()

    obtener_paises_unicos(paises)
    
    paises_objetivos = ["Germany", "Canada"]
    print(f"Paises a analizar:\n {paises_objetivos}\n")
    
    obtener_ventas_por_pais(paises_objetivos, paises, precios)
    
    obtener_calzado_mas_vendido_por_pais(paises_objetivos, paises, talles)
    
    genero_objetivo = "Male"
    
    obtener_ventas_por_genero_pais(paises_objetivos, genero_objetivo, paises, generos)
    