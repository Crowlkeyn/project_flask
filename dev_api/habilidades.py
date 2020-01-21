import json
from flask import request
from flask_restful import Resource


lista = ['Python', 'Java', 'Flask', 'PHP', 'Django', 'MySQL', 'PostgreSQL']
class Habilidades(Resource):
    def get(self):
        return lista

    def post(self):
        dados = json.loads(request.data)
        lista.append(dados[len(lista)])
        return lista


class ListaHabilidades(Resource):
    def put(self, id):
        lista[id] = json.loads(request.data)[id]
        return json.loads(request.data)

    def delete(self, id):
        try:
            lista.pop(id)
            return {'status': 'sucesso', 'mensagem': 'Registro excluído'}
        except Exception:
            return{ 'status': 'erro', 'mensagem': 'Não foi possível excluir registro'}
