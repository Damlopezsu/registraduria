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
app=Flask(__name__)
cors = CORS(app)

miControladorUsuario=ControladorUsuario()
miControladorPermiso=ControladorPermiso()
miControladorRol=ControladorRol()
miControladorPermisorol=ControladorPermisorol()

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
