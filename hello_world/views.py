from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request, jsonify

moje_imie = "Wiktor"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output')
    if output == 'json':
        return jsonify({"imie": "Wiktor", "mgs": "Hello World!"})
    return "Output is not JSON"


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)


def blad():
    print("To blad")
