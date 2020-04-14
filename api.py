from flask import Flask, jsonify, request, make_response, send_from_directory, abort
from flask_restful import Resource, Api
import os
import jwt
import datetime
from functools import wraps
from os import urandom
# app config######################################################
app = Flask(__name__)

hashapi = urandom(1000)
app.config["SECRET_KEY"] = str(hashapi)

# diretori de arquivos
UPLOAD_DIRECTORY = "./project/api_uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
#################################################################


# decorator para verificacao de token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # htpp://127.0.0.1:5000/route?token={}
        token = request.args.get('token')
        if not token:
            return jsonify({"info": "sem token sem acesso sinto muito"}), 403

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return jsonify({"info": "poxa parceiro o token esta invalido ou voce deixou vazio"}), 403

        return f(*args, **kwargs)
    return decorated

# bloco de login
@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        )+datetime.timedelta(minutes=30)}, app.config["SECRET_KEY"])
        return jsonify({'token': token.decode("utf-8")})
    return make_response('nao consigo verificar', 401, {"WWW-Authenticate": "Basic realm='Login Required'"})
###########################################################################################################################
########                                                  bloco de rotas                                           ########
###########################################################################################################################
@app.route("/")
@token_required
def root():
    """Endpoint to list files on the server."""
    return jsonify({"info": "seja bem vindo ao th"})


@app.route("/files")
@token_required
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route("/files/<path:path>")
@token_required
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route("/files/<filename>", methods=["POST"])
@token_required
def post_file(filename):
    """Upload a file."""

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories directories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201


if __name__ == '__main__':
    app.run(debug=True)
