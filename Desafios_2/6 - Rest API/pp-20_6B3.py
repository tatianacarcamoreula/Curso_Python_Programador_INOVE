# IMPORTANTE: NO borrar los comentarios

import traceback
from flask import Flask, request, jsonify, render_template, Response

# Base de datos
from flask_sqlalchemy import SQLAlchemy

# Crear el server Flask
app = Flask(__name__)

# Indicamos al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gastos.db"

# Asociamos nuestro controlador de la base de datos con la aplicacion
db = SQLAlchemy()
db.init_app(app)

# ------------ Base de datos ----------------- #
class Gastos(db.Model):
    __tablename__ = "gastos"
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String)
    gasto = db.Column(db.Integer)


# ------------ Rutas o endpoints ----------------- #
# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        result = "<h1>Bienvenido!!</h1>"
        result += "<h3>[GET] /iniciar --> endpoint utilizado para llenar la base de datos"
        result += "<h2>Alumno, Debe completar los siguientes endpoints en el backend:</h2>"
        result += "<h3>[GET] /gastos --> mostrar todo los gastos realizados en formato JSON"
        result += "<h3>[GET] /gastos/[categoria] --> mostrar todos los gastos de un categoría específica en formato JSON"
        return result
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/iniciar
@app.route("/iniciar")
def iniciar():
    try:
        # Borrar la base de datos antes de cargar los datos
        db.drop_all()

        # Volver a crear la base de datos
        db.create_all()

        # Cargar todos los datos para practicar
        # los endpoints del desafio
        # IMPORTANTE: Esta no es una buena forma de insertar datos,
        # debe utilizarse un endpoint de POST para estas prácticas
        # como se vio en clase. Pero ahora, para facilitar la práctica
        # utilizaremos este recurso
        gasto = Gastos(categoria="comida", gasto=30)
        db.session.add(gasto)
        gasto = Gastos(categoria="entretenimiento", gasto=50)
        db.session.add(gasto)
        gasto = Gastos(categoria="comida", gasto=50)
        db.session.add(gasto)
        gasto = Gastos(categoria="servicios", gasto=120)
        db.session.add(gasto)
        gasto = Gastos(categoria="servicios", gasto=100)
        db.session.add(gasto)
        gasto = Gastos(categoria="categoria", gasto=20)
        db.session.add(gasto)
        
        db.session.commit()

        return "datos generados"
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos
@app.route("/gastos")
def gastos():
    try:
        print("Endpoint gastos")
        # Alumno:
        # Leer todos los datos dentro de la base de datos
        # utilizando un bucle y extraer los datos
        # para devolver al frontend como JSON los datos
        # utilizando la función jsonify
        query = db.session.query(Gastos)
        data = []
        for gasto in query:
            json_result = {}
            json_result["categoria"] = gasto.categoria
            json_result["gasto"] = gasto.gasto
            data.append(json_result)
        print("Categorias y gastos almacenados:")
        print(data)
        return jsonify(data)
            
    except:
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos/<categoria>
@app.route("/gastos/<categoria>")
def gastos_categoria(categoria):
    try:
        print("Endpoint gastos_categoria")
        # Alumno:
        # El endpoint debe devolver un JSON unicamente
        # con los gastos asociados a la categoria
        # pasada por la URL
        categoria = categoria.lower()
        query = db.session.query(Gastos)
        gastos = []
        for i in query:
            if i.categoria == categoria:
                json_result = {}
                json_result["categoria"] = i.categoria
                json_result["gasto"] = i.gasto
                gastos.append(json_result)
        return jsonify(gastos)
            
    except:
        return jsonify({'trace': traceback.format_exc()})


# Este método se ejecutará la primera vez
# cuando se construye la app.
with app.app_context():
    # Crear aquí la base de datos
    db.create_all()
    print("Base de datos generada")


if __name__ == '__main__':
    print('¡Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
