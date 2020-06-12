from flask import Blueprint

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route(rule='/', methods=['GET'])
def main():
    html = ''
    html += '<html>'
    html += '<body>'
    html += '<h1>Webservice</h1>'
    html += '<h3>Teste Boticario</h3>'
    html += '<a href="https://github.com/mabattistini/desafio-boticario/blob/master/README.md">Instruções</a>'
    html += '</body>'
    html += '</html>'

    return html


