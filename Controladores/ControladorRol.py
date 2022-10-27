from Modelos.Rol import Rol
class ControladorRol():
    def __init__(self):
         print("Creando ControladorRol")
    def index(self):
         print("Listar todos los Rol")
         unRol = {
             "_id_Rol": "a",
             "nombre_Rol": "archivar",
         }
         return [unRol]

    def create(self,infoRol):
         print("Crear un Rol")
         elRol = Rol(infoRol)
         return elRol.__dict__
    def show(self,id):
         print("Mostrando un Rol con id ", id)
         elRol = {
             "_id_Rol":id,
             "nombre_Rol": "archivar",
         }
         return elRol

    def update(self, id, infoRol):
        print("Actualizando Rol con id ", id)
        elRol = Rol(infoRol)
        return elRol.__dict__

    def delete(self, id):
        print("Elimiando Rol con id ", id)
        return {"deleted_count": 1}