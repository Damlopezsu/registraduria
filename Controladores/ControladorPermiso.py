from Modelos.Permiso import Permiso
class ControladorPermiso():
    def __init__(self):
         print("Creando ControladorPermiso")
    def index(self):
         print("Listar todos los Permiso")
         unPermiso = {
             "_id_Permiso": "abc123",
             "url_Permiso": "123",
             "metodo": "Juan",
         }
         return [unPermiso]
    def create(self,elPermiso):
         print("Crear un Permiso")
         elPermiso = Permiso(infoPermiso)
         return elPermiso.__dict__
    def show(self,id):
         print("Mostrando un Permiso con id ", id)
         elPermiso = {
             "_id_Permiso": "abc123",
             "url_Permiso": "123",
             "metodo": "Juan",
         }
         return [elPermiso]

    def update(self, id, elPermiso):
        print("Actualizando Permiso con id ", id)
        elPermiso = Permiso(infoPermiso)
        return elPermiso.__dict__

    def delete(self, id):
        print("Elimiando Permiso con id ", id)
        return {"deleted_count": 1}