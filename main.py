from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorUsuario import ControladorUsuario
from Controladores.ControladorPermiso import ControladorPermiso
from Controladores.ControladorRol import ControladorRol
from Controladores.ControladorPermisorol import ControladorPermisorol
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido

app=Flask(__name__)
cors = CORS(app)

miControladorUsuario=ControladorUsuario()
miControladorPermiso=ControladorPermiso()
miControladorRol=ControladorRol()
miControladorPermisorol=ControladorPermisorol()
miControladorMesa=ControladorMesa()
miControladorResultado=ControladorResultado()
miControladorCandidato=ControladorCandidato()
miControladorPartido=ControladorPartido()

@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/Mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)


@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorResultado.create(data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarResultado(id):
    data = request.get_json()
    json=miControladorResultado.update(id,data)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResultado(id):
    json=miControladorResultado.delete(id)
    return jsonify(json)


@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)


@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)





















































def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
"Usuario"
@app.route("/usuarios",methods=['GET'])
def getUsuarios():
    json=miControladorUsuario.index()
    return jsonify(json)
@app.route("/usuarios",methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json=miControladorUsuario.create(data)
    return jsonify(json)
@app.route("/usuarios/<string:id>",methods=['GET'])
def getUsuario(id):
    json=miControladorUsuario.show(id)
    return jsonify(json)

@app.route("/usuarios/<string:id>",methods=['PUT'])
def modificarUsurio(id):
    data = request.get_json()
    json=miControladorUsuario.update(id,data)
    return jsonify(json)

@app.route("/usuarios/<string:id>",methods=['DELETE'])
def eliminarUsuario(id):
    json=miControladorUsuario.delete(id)
    return jsonify(json)


"Rol"

@app.route("/roles",methods=['GET'])
def getRol():
    json=miControladorRol.index()
    return jsonify(json)
@app.route("/roles",methods=['POST'])
def crearRol():
    data = request.get_json()
    json=miControladorRol.create(data)
    return jsonify(json)
@app.route("/roles/<string:id>",methods=['GET'])
def getRol(id):
    json=miControladorRol.show(id)
    return jsonify(json)

@app.route("/roles/<string:id>",methods=['PUT'])
def modificarRol(id):
    data = request.get_json()
    json=miControladorRol.update(id,data)
    return jsonify(json)

@app.route("/roles/<string:id>",methods=['DELETE'])
def eliminarRol(id):
    json=miControladorRol.delete(id)
    return jsonify(json)
"Permisoroles"
@app.route("/permisoroles",methods=['GET'])
def getPermisorol():
    json=miControladorPermisorol.index()
    return jsonify(json)
@app.route("/permisoroles",methods=['POST'])
def crearPermisorol():
    data = request.get_json()
    json=miControladorPermisorol.create(data)
    return jsonify(json)
@app.route("/permisoroles/<string:id>",methods=['GET'])
def getPermisorol(id):
    json=miControladorPermisorol.show(id)
    return jsonify(json)

@app.route("/permisoroles/<string:id>",methods=['PUT'])
def modificarPermisorol(id):
    data = request.get_json()
    json=miControladorPermisorol.update(id,data)
    return jsonify(json)

@app.route("/permisoroles/<string:id>",methods=['DELETE'])
def eliminarPermisoroles(id):
    json=miControladorPermisorol.delete(id)
    return jsonify(json)

"Permiso"
@app.route("/permisos",methods=['GET'])
def getPermiso():
    json=miControladorPermiso.index()
    return jsonify(json)
@app.route("/permisos",methods=['POST'])
def crearPermiso():
    data = request.get_json()
    json=miControladorPermiso.create(data)
    return jsonify(json)
@app.route("/permisos/<string:id>",methods=['GET'])
def getPermiso(id):
    json=miControladorPermiso.show(id)
    return jsonify(json)

@app.route("/permisos/<string:id>",methods=['PUT'])
def modificarPermiso(id):
    data = request.get_json()
    json=miControladorPermiso.update(id,data)
    return jsonify(json)

@app.route("/permisos/<string:id>",methods=['DELETE'])
def eliminarPermiso(id):
    json=miControladorPermiso.delete(id)
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
