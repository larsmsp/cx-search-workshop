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
    return "Hello, World! This is a search engine for Computas.com!"


@app.route('/calculator', methods=['GET'])
def calculator():
    """
    Operatorer og operand er angitt i query-parametrene "operator", "operand1" og "operand2", 
    f.eks /calculator?operator=plus&operand1=2&operand2=2
    Endepunktet skal støtte "plus", "minus", "mult" og "div".
    :return: Resultatet av enkle heltallsoperasjoner.
    """
    try:
        operand1 = int(request.args['operand1'])
        operand2 = int(request.args['operand2'])
        operator = request.args['operator']
        return _do_math(operator, operand1, operand2)
    except KeyError:
        return "Feil i forespørsel: Mangler operand1, operand2 eller mangler/ugyldig operator.", 400
    except ValueError:
        return "Feil i forespørsel: operand1 og operand2 må kunne konverteres til heltall.", 400


def _do_math(operator, operand1, operand2):
    operations = {
        'plus': "{0} + {1} = {2}".format(operand1, operand2, operand1 + operand2),
        'minus': "{0} - {1} = {2}".format(operand1, operand2, operand1 - operand2),
        'mult': "{0} * {1} = {2}".format(operand1, operand2, operand1 * operand2),
        'div': "{0} / {1} = {2}".format(operand1, operand2, operand1 / operand2)
    }
    return operations[operator]

if __name__ == '__main__':
    app.run()
