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
    """
    Hjelpeklasse for å søke etter dokumenter i indeksen.
    Finn riktige verdier i Google Cloud Platform-konsollet og fyll inn.
    """
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
        final_results = [{
                Document.ID: cls.get_id(doc),
                Document.TITLE: cls.get_title(doc),
                Document.URL: cls.get_url(doc),
                Document.CONTENTS: cls.get_contents(doc)
            } for doc in search_results]
        return final_results

    @classmethod
    def get_id(cls, search_doc):
        return search_doc.doc_id

    @classmethod
    def get_title(cls, search_doc):
        return cls.get_document_field(search_doc, Document.TITLE)

    @classmethod
    def get_url(cls, search_doc):
        return cls.get_document_field(search_doc, Document.URL)

    @classmethod
    def get_contents(cls, search_doc):
        return cls.get_snippeted_field(search_doc, Document.CONTENTS)

    @classmethod
    def get_document_field(cls, search_doc, field_name):
        for field in search_doc.fields:
            if field.name == field_name:
                return field.value
        return ""

    @classmethod
    def get_snippeted_field(cls, search_doc, field_name):
        for expr in search_doc.expressions:
            if expr.name == field_name:
                return expr.value
        return ""


if __name__ == '__main__':
    app.run()
