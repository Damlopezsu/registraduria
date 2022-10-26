from Modelos.Rol import Rol
class ControladorRol():
    def __init__(self):
         print("Creando ControladorRol")
    def index(self):
         print("Listar todos los Rol")
         unRol = {
             "_id_Rol": "abc123",
             "nombre_Rol": "123",
         }
         return [unRol]

    def create(self,elRol):
         print("Crear un Rol")
         elRol = Rol(infoRol)
         return elRol.__dict__
    def show(self,id):
         print("Mostrando un Rol con id ", id)
         elRol = {
             "_id_Rol": "79542749",
             "nombre_Rol": "Juan Perez",
         }
         return [elRolRol]

    def update(self, id, elRol):
        print("Actualizando Rol con id ", id)
        elRol = Rol(infoRol)
        return elRol.__dict__

    def delete(self, id):
        print("Elimiando Rol con id ", id)
        return {"deleted_count": 1}