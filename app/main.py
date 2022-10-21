# Importar a classe Flask, objeto request e o objeto jsonify:
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

jornada = [{'tipo': 'hora-normal', 'valor': 40.00},
{'tipo': 'hora-extra', 'valor': 50.00}]

# http://127.0.0.1:5000/jornada
@app.route('/jornada', methods=['GET'])
def retornar_todos_as_horas_trabalhas():
    resp = jornada

    if 'X-tipo' in request.headers:
        tipo = request.headers['X-tipo']
        for produto in jornada:
            if produto['tipo'] == tipo:
                resp = produto
    return jsonify(resp)
# http://127.0.0.1:5000/jornada/total
@app.route('/jornada/total', methods=['GET'])
def retornar_total_das_horas_trabalhadas():

    if 'X-normal' in request.headers:
        normal = int(request.headers['X-normal'])
    if 'X-extra' in request.headers:
        extra = int(request.headers['X-extra'])
    total = normal * 40 + extra * 50
    desconto = total * 0.9 
    return jsonify({"Salário bruto": total, "Salário liquido":desconto})

if __name__ == '__main__':
# Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)
