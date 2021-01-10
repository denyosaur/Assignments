# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/math/<ops>')
def adding(ops):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations[ops](a, b)
    return str(result)
