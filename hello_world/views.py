from hello_world import app
from hello_world.formater import get_formatted, SUPPORTED, PLAIN
from flask import request, jsonify

moje_imie = "Wiktor"
msg = "Hello World!"


@app.route('/')
def index():
    output = request.args.get('output', 'plain')
    if output == 'json':
        return jsonify({"imie": "Wiktor", "mgs": "Hello World!"})
    return get_formatted(msg, moje_imie), output.lower()


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)


def blad():
    print("To blad")
