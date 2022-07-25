import json
import smtplib

from flask import Flask, request
from flask_restful import Resource, Api, abort
from email.message import EmailMessage
import os
import Banco_de_dados
import Validar_dados
import requests
app = Flask(__name__)
api = Api(app)

EMAIL_ADDRESS = '***********'
EMAIL_PASSWORD = '***********'

class Adicionar_Usuario(Resource):
    def post(self):
        nome = Validar_dados.validar_nome(request.json['nome'])
        email = Validar_dados.validar_email(request.json['email'])
        telefone = Validar_dados.valida_telefone(request.json['telefone'])

        if (nome == True) and (email== True ) and (telefone==True):
            Banco_de_dados.add_usuario(request.json['nome'],request.json['email'], request.json['telefone'])

        else:
            abort(404, message='Os dados foram passados na formataçao errada, mande novamente')

        return {"message": "Usuario adicionado"}

class Editar_Usuario(Resource):
    def post(self,id):
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


class Deletar_usuario(Resource):
    def delete(self,id):
        try:
            mensagem=Banco_de_dados.deletar_usuario(id)
            return mensagem
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
            if usuario is None:
                return {"message": "Usuario não existente"}
            else:
                return usuario
        except:
            abort(404, message='Ocorreu um erro')
class Enviar_email(Resource):
    def post(self):
        validar = Validar_dados.validar_email(request.json['destinatario'])
        if validar == True:

            try:
                consulta = requests.get(request.json['mensagem'])
                lista = json.loads(consulta.content)
                corpo_email = f'''
                           <p> Prezado usuário,</p>
                           <p> Este email é gerado automaticicamente.</p>
                           <p> A requisição feita via Json, contem o seguinte HTML: {request.json['mensagem']}.</p>
                           <p> Que é gerado o seguinte Json:</p>
                           <p> {lista}
                           <p> Agradeço a atenção</p>
                           <p> João Gabriel de Oliveira Ponciano</p>
                           '''
                email = EmailMessage()
                email['Subject']= request.json['assunto']
                email['From'] = 'jotagepb@gmail.com'
                email['To'] = request.json['destinatario']
                email.add_header('Content-Type','text/html')
                email.set_payload(corpo_email)
                s = smtplib.SMTP('smtp.gmail.com:587')
                s.starttls()
                s.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                s.sendmail( email['From'],email['To'],email.as_string().encode('utf-8'))
                return {"message": "Email enviado com sucesso"}
            except:
                abort(404, message='Ocorreu um erro')
        else:
            abort(404, message='Os dados foram passados na formataçao errada, mande novamente')

api.add_resource(Adicionar_Usuario, "/bridgehub/add_user")
api.add_resource(Editar_Usuario, "/bridgehub/edit_user/<int:id>")
api.add_resource(Deletar_usuario, "/bridgehub/delete_user/<int:id>")
api.add_resource(Consultar_todos_usuarios, "/bridgehub/users")
api.add_resource(Consultar_usuario_especifico, "/bridgehub/users/<int:id>")
api.add_resource(Enviar_email,"/bridgehub/send_email")
create_db = not os.path.isfile('BridgeHub.db')
if create_db:
    Banco_de_dados.criar_BD()
if __name__ == "__main__":
    app.run(debug=True)