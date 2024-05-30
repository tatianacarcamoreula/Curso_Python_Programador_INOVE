# IMPORTANTE: NO borrar los comentarios

import traceback
from flask import Flask, request, jsonify, render_template, Response

# Crear el server Flask
app = Flask(__name__)


# ------------ Base de datos ----------------- #
# Variable global para poner a prueba el método [GET]
# IMPORTANTE: Esta no es una buena forma de manejar datos,
# se debe usar una base de datos (se verá en otro desafio más adelante)
datos_gastos = [
    {
        "categoria": "comida",
        "gasto": 30,
    },
    {
        "categoria": "entretenimiento",
        "gasto": 50,
    },
    {
        "categoria": "comida",
        "gasto": 50,
    },
    {
        "categoria": "servicios",
        "gasto": 120,
    },
    {
        "categoria": "servicios",
        "gasto": 100,
    },
    {
        "categoria": "comida",
        "gasto": 20,
    },

]

# ------------ Rutas o endpoints ----------------- #
# Ruta que se ingresa por la ULR 127.0.0.1:5000
@app.route("/")
def index():
    try:
        result = "<h1>Bienvenido!!</h1>"
        result += "<h2>Alumno, Debe completar los siguientes endpoints en el backend:</h2>"
        result += "<h3>[GET] /gastos --> mostrar todo los gastos realizados en formato JSON"
        return result
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos
@app.route("/gastos")
def gastos():
    try:
        print("Endpoint gastos")
        # Alumno:
        # Leer todos los datos dentro de la base de datos
        # (en este caso la variable datos_gastos)
        # y devolver al frontend como JSON
        # utilizando la función jsonify
        data = datos_gastos
        print(data)
        return jsonify(data)
    except:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    print('¡Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
