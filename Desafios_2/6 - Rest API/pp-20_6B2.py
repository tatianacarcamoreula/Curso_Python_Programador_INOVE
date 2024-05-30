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
        result += "<h3>[GET] /gastos/[categoria] --> mostrar todos los gastos de un categoría específica en formato JSON"
        return result
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})


# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos
@app.route("/gastos")
def gastos():
    try:
        print("Endpoint gastos")
        return jsonify(datos_gastos)
    except:
        return jsonify({'trace': traceback.format_exc()})


# Alumno:
# Crear a continuación el endpoint para la ruta:
# /gastos/<categoria>
# A la función asociada al endpoint la puede llamar:
# gastos_categoria

# El endpoint debe devolver un JSON unicamente
# con los gastos asociados a la categoria
# pasada por la URL
# Ruta que se ingresa por la ULR 127.0.0.1:5000/gastos/<categoria>
@app.route("/gastos/<categoria>")
def gastos_categoria(categoria):
    try:
        categoria = categoria.lower()
        gastos = []
        for dato in datos_gastos:
            if dato["categoria"] == categoria:
                gastos.append(dato)
                
        print("Gastos de la categoria", categoria)
        print(gastos)
        
        return jsonify(gastos)
    
    except:
        return jsonify({'trace': traceback.format_exc()})
    
if __name__ == '__main__':
    print('¡Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
