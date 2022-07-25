from flask import Flask, request
from flask_restful import Resource, Api, abort
import os
import Banco_de_dados
import Validar_dados
app = Flask(__name__)
api = Api(app)

class Adicionar_Usuario(Resource):
    def post(self):
        try:
            nome = Validar_dados.validar_nome(request.json['nome'])
            email = Validar_dados.validar_email(request.json['email'])
            telefone = Validar_dados.valida_telefone(request.json['telefone'])
            if (nome == True) and (email== True ) and (telefone==True):
                Banco_de_dados.add_usuario(request.json['nome'],request.json['email'], request.json['telefone'])
            else:
                abort(404, message='Os dados foram passados na formataçao errada, mande novamente')
            return {"message": "Usuario adicionado"}
        except:
            abort(404, message='Ocorreu um erro')



class Editar_Usuario(Resource):
    def post(self,id):
        try:
            nome = Validar_dados.validar_nome(request.json['nome'])
            email = Validar_dados.validar_email(request.json['email'])
            telefone = Validar_dados.valida_telefone(request.json['telefone'])
            if (nome == True) and (email == True) and (telefone == True):
                Banco_de_dados.atulizar_usuario(request.json['nome'],id,1)
                Banco_de_dados.atulizar_usuario(request.json['email'], id, 2)
                Banco_de_dados.atulizar_usuario(request.json['telefone'], id, 3)
            else:
                abort(404, message='Os dados foram passados na formataçao errada, mande novamente')

            return {"message": "Usuario atualizado"}
        except:
            abort(404, message='Ocorreu um erro')


class Deletar_usuario(Resource):
    def get(self,id):
        try:
            Banco_de_dados.deletar_usuario(id)
            return {"message:Usuario deletado"}
        except:
            abort(404, message='Usuario não deletado, verifique se o id é existente')
class Consultar_todos_usuarios(Resource):
    def get(self):
        try:
            todos_usuarios = Banco_de_dados.consultar_todos_usuarios()
            return todos_usuarios
        except:
            abort(404, message='Ocorreu um erro')
class Consultar_usuario_especifico(Resource):
    def get(self,id):
        try:
            usuario = Banco_de_dados.consultar_usuario_id(id)
            return usuario
        except:
            abort(404, message='Ocorreu um erro')

api.add_resource(Adicionar_Usuario, "/bridgehub/add_user")
api.add_resource(Editar_Usuario, "/bridgehub/edit_user/<int:id>")
api.add_resource(Deletar_usuario, "/bridgehub/delete_user/<int:id>")
api.add_resource(Consultar_todos_usuarios, "/bridgehub/users")
api.add_resource(Consultar_usuario_especifico, "/bridgehub/users/<int:id>")

create_db = not os.path.isfile('BridgeHub.db')
if create_db:
    Banco_de_dados.criar_BD()
if __name__ == "__main__":
    app.run(debug=True)