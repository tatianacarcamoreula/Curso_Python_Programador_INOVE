# Alumno:
# El objetivo es realizar un ejercicio muy similar al
# realizado en el pasado con la API de jsonplaceholder.
# Deberan consumir toda la información que retorna
# el request de la API y almacenarla en una db.
url = "https://jsonplaceholder.typicode.com/todos"

# Luego deberá crear una serie de endpoints
# para consultar la información almacenada
# en la base de datos
# En este desafio solo se utilizarán endpoints
# con HTTP GET (no se utilizará POST)

import traceback
from flask import Flask, request, jsonify, render_template, Response
import requests
#Base de datos
from flask_sqlalchemy import SQLAlchemy

#creo el server Flask
app = Flask(__name__)

#y le indico de donde leer los datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///secundaria2.db"

#asocio el controlador de la base de datos con la aplicacion
db = SQLAlchemy()
db.init_app(app)

# ------------ Base de datos ----------------- #
    
# Deberá generar una base de datos SQL
# que posea los siguientes campos:
# - id --> [número] id de la consulta
# - userId --> [número] id del usuario
# - titulo --> [texto] nombre del título
# - completado --> [bool] completado o no el título
class Secundaria(db.Model):
    __tablename__ = "estudiantes"
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    titulo = db.Column(db.String)
    completado = db.Column(db.Boolean)

# ------------ Rutas o endpoints ----------------- #
    
# A)
# Ruta que se ingresa por la ULR 127.0.0.1:5000/iniciar
# Crear un endpoint para "iniciar" en el cual
# 1) Deberá vaciar la base de datos y volverla a crear
# 2) Utilizar requests para consumir toda la información
# de jsonplaceholder utilizando la URL indicanda al comienzo
# del enunciado
# 3) Utilizar un bucle para guardar esa información recolectada
# (una por una) en la base de datos
# 4) Retornar al frontend un texto que lo ayude a usted a
# comprender que la ruta se completó con éxito
# IMPORTANTE: Esta no es una buena forma de insertar datos,
# debe utilizarse un endpoint de POST para estas prácticas
# como se vio en clase. Pero ahora, para facilitar la práctica
# utilizaremos este recurso
@app.route("/")
def index():    
    try:
        result = "<h1>Bienvenido!!</h1>"
        result += "<h3>[GET] /iniciar --> endpoint utilizado para llenar la base de datos"
        result += "<h3>[GET] /usuarios --> mostrar todo los usuarios registardos en formato JSON"
        result += "<h3>[GET] /usuarios/[userId] --> mostrar todos los registros de un userId especifico en formato JSON"
        return result
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})
    
@app.route("/iniciar")
def iniciar():
    try:
        
        db.drop_all()
        db.create_all()
        
        reponse = requests.get(url)
        data = reponse.json()
        for datos in data:
            usuario = Secundaria(userId = datos["userId"], titulo = datos["title"], completado = datos ["completed"])
            db.session.add(usuario)
        db.session.commit()
        return "datos generados"
    except:
        return jsonify({'trace': traceback.format_exc()})


# B)
# Ruta que se ingresa por la ULR 127.0.0.1:5000/usuarios
# Crear un endpoint usuarios en el cual: recibe el userId
# 1) Deberá buscar en la base de datos todos los usuarios
# 2) Deberá armar una lista de todos los usuarios según
# el userId (sin duplicar)
# 3) Deberá retornar al frontend un JSON que tenga la lista
# de usuarios respetando esta estructura:
# [
#    {"userId": ...},
#    {"userId": ...},
# ]
# Cada elemento de esa lista (cada diccionario dentro de la lista)
# representa cada usuario en la base de datos.
# Esta lista debería retornar 10 elementos, porque
# en los datos de jsonplaceholder hay 10 usuarios (10 userId distintos)
@app.route("/usuarios")
def usuarios():
    try:
        usuarios = []
        for datos in range (1,11):
            filtro = db.session.query(Secundaria).filter(Secundaria.userId == datos).first()
            if filtro is not None:
                json_result = {}
                json_result["userId"] = filtro.userId
                usuarios.append(json_result)  
        return jsonify(usuarios)
    
    except:
        return jsonify({'trace': traceback.format_exc()})

# C)
# Ruta que se ingresa por la ULR 127.0.0.1:5000/usuarios/<userId>
# Crear un endpoint usuarios/<userId> el cual recibe el userId
# del usuario que se desea consultar.
# 1) Deberá buscar en la base de datos todos los títulos
# completados por ese usuario según el userId
# Para realizar esta operación utilice filter de ORM
# 2) Deberá contar cuantos títulos completó ese usuario
# y almacenar ese valor en una variable llamda "titulos_completados"
# 3) Deberá retornar al frontend un JSON que tenga la siguiente
# estructura:
# {"userId": userId, "titulos_completados": titulos_completados}
@app.route("/usuarios/<userId>")
def usuarios_userId(userId):
    try:
        userId = int(userId)
        query = db.session.query(Secundaria).filter(Secundaria.completado == True, Secundaria.userId == userId)
        json_result = {}
        json_result["userId"] = userId
        json_result["titulos_completados"] = query.count()
        
        return jsonify(json_result)
    except:
        return jsonify({'trace': traceback.format_exc()})
                
if __name__ == '__main__':
    print("¡Comenzamos!")

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)