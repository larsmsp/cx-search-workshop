# coding=utf-8
import logging

from flask import Flask, request, jsonify
from google.appengine.api import search as search_api

logging.basicConfig(format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
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


@app.route('/search', methods=['GET'])
def search():
    """
    Brukere skal kunne gå til adressen <din appengine-adresse>/search?q=<søkestring> og få en liste av
    resultater tilbake. Listen skal returneres som JSON (JavaScript Object Notation).

    For å konvertere mellom en liste i Python og JSON som Flask kan returnere, så kan man bruke metoden "jsonify".
    :return: En liste av alle søkeresultater.
    """
    return jsonify(Document.search(request.args['q']))


class Document(object):

    _INDEX_NAME = 'computas-docs'

    ID = 'id'
    URL = 'url'
    TITLE = 'title'
    CONTENTS = 'contents'

    @classmethod
    def search(cls, query_string):
        index = search_api.Index(cls._INDEX_NAME)
        query_options = search_api.QueryOptions(
            snippeted_fields=[Document.CONTENTS]
        )
        query = search_api.Query(query_string.strip(), query_options)
        search_results = index.search(query)
        final_results = []
        for doc in search_results:
            result = {
                Document.ID: doc.doc_id
            }
            for field in doc.fields:
                if field.name == Document.TITLE:
                    result[Document.TITLE] = field.value
                if field.name == Document.URL:
                    result[Document.URL] = field.value
            for expr in doc.expressions:
                if expr.name == Document.CONTENTS:
                    result[Document.CONTENTS] = expr.value
            final_results.append(result)
        return final_results


if __name__ == '__main__':
    app.run()
