from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request, jsonify

moje_imie = "Natalia"
msg = "Hello World!"

@app.route('/')
def index():
    name = "Fabian"
    response_data = {
        "imie": name,
        "msg": "Hello, World!"
        }
    return jsonify(response_data)

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)