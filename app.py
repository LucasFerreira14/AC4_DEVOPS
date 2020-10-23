import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)


@app.route('/')
def fibonacci():
    lista = [0, 1]
    x = []
    i = 1

    while len(lista) < 50:
        soma = lista[i-1] + lista[i]
        i += 1
        lista.append(soma)

    for i in range(len(lista)):
        m = str(lista[i])
        x.append(m)

    def convert(s):
        m = ", "
        return m.join(s)

    resultado = convert(x)

    return resultado


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
