# IMPORTANTE: NO borrar los comentarios

# Alumno: Arreglar el código a continuación para que funcione
# en el editor de código:

import traceback
from flask import Flask, request, jsonify, render_template, Response


# ------------ Rutas o endpoints ----------------- #
# Ruta que se ingresa por la ULR 127.0.0.1:5000

app = Flask(__name__)

@app.route("/")
def index():
    try:
        return "¡Hola mundo desde Flask!"
    except:
        # En caso de falla, retornar el mensaje de error
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    print('¡Inove@Server start!')

    # Lanzar server
    app.run(host="127.0.0.1", port=5000)
