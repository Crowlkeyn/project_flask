from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, ListaHabilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0',
     'nome': 'Marcos',
     'habilidades': ['Python', 'Flask', 'Django']
     },
    {'id': '1',
     'nome': 'Paulo',
     'habilidades': ['Python', 'Flask']
     }
]


#Devolve um desenvolvedor pelo id e tambem altera e deleta um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Desenvolvedor de ID {id} nao existe!'}
        except Exception:
            response = 'Erro desconhecido. Procure o administrador da API'
        return response

    def put(self, id):
        desenvolvedores[id] = json.loads(request.data)
        return json.loads(request.data)

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}


# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

    def get(self):
        return desenvolvedores


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(ListaHabilidades, '/habilidades/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)