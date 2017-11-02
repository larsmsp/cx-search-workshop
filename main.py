# coding=utf-8
import logging

from flask import Flask, request

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    """
    :return: "Hello, world!" til de som besøker siden. 
    """
    return ""


@app.route('/calculator', methods=['GET'])
def calculator():
    """
    Operatorer og operand er angitt i query-parametrene "operator", "operand1" og "operand2", 
    f.eks /calculator?operator=plus&operand1=2&operand2=2
    Verdiene kan hentes ut av objektet request.args
    Endepunktet skal støtte "plus", "minus", "mult" og "div".
    :return: Resultatet av enkle heltallsoperasjoner.
    """
    operand1 = int('hent ut verdient til operand1')
    operand2 = int('hen tut verdient til operand2')
    operator = 'hent ut operator'
    result = 0  # Utfør riktig operasjon og skriv til result
    # Kode for å gjøre riktig operasjon.
    return "Resultatet er {0}".format(result)


if __name__ == '__main__':
    app.run()
