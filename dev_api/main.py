from flask import Flask, jsonify,request
import json
app = Flask(__name__)


desenvolvedores = [
    {'id': '0',
     'nome': 'Marcos',
     'habilidades': ['Python', 'Flask']
     },
    {'id': '1',
     'nome': 'Paulo',
     'habilidades': ['Python', 'Flask']
     }
]

#devolve um desenvolvedor pelo id e tambem altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Desenvolvedor de ID {id} nao existe!'}
        except Exception:
            response = 'Erro desconhecido. Procure o administrador da API'
        return jsonify(response)

    elif request.method == 'PUT':
        desenvolvedores[id] = json.loads(request.data)
        return jsonify(json.loads(request.data))

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)
