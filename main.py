from flask import Flask, jsonify, render_template
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/<quantia>")
def main(quantia):
    lista_cpf = []
    for cpf in range(int(quantia)):
        while True:
            lista_digitos = [randint(0, 9) for digito in range(9)]
            for multiplicador in [10, 11]:
                soma_total = 0
                for digito in lista_digitos:
                    soma_total += digito * multiplicador
                    multiplicador -= 1
                digito_verificador = 11 - soma_total % 11
                if digito_verificador >= 10:
                    digito_verificador = 0
                lista_digitos.append(digito_verificador)
            cpf = "".join(str(digito) for digito in lista_digitos)
            if cpf not in lista_cpf:
                lista_cpf.append(cpf)
                break
    return jsonify({"cpfs": lista_cpf})


app.run(host='0.0.0.0')
