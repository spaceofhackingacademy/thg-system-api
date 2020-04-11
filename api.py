from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class THGapi(Resource):
    def get(self):
        cpf = request.args['CPF']
        datanascimento = request.args['DataNascimento']
        nomeMae = request.args['NomeMae']
        return "cpf={}datanascimento={}\nNomeMae={}".format(cpf+"\n", datanascimento,
                                                            nomeMae)


api.add_resource(THGapi, '/thg')

if __name__ == '__main__':
    app.run(debug=True)
