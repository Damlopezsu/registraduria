from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido

miControladorMesa = ControladorMesa()
miControladorResultado = ControladorResultado()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://YulianaBahamon:Yuliana13.@cluster0.dm8hjhl.mongodb.net/db-resgistraduria?retryWrites=true&w=majority",tlsCAFile=ca);
db = client.test
print(db)

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)


@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)


@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>",methods=['POST'])
def crearInscripcion(id_mesa,id_candidato):
    data = request.get_json()
    json=miControladorResultado.create(data,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/resultados/mesas/<string:id_mesa>/candidatos/<string:id_candidato>",methods=['PUT'])
def modificarResultados(id,id_mesa,id_candidato):
    infoResultado = request.get_json()
    json=miControladorResultado.update(id,infoResultado,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)
@app.route("/resultados/mesas/<string:id_candidato>",methods=['GET'])
def inscritosCandidatos(id_candidato):
    json=miControladorResultado.listarInscritosCandidatos(id_candidato)
    return jsonify(json)


@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>/partidos/<string:id_partido>",methods=['PUT'])
def asignarCandidatoPartido(id,id_partido):
    json=miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)


@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
