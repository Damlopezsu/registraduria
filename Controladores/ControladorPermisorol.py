from Modelos.Permisorol import Permisorol
class ControladorPermisorol():
    def __init__(self):
         print("Creando ControladorPermisorol")
    def index(self):
         print("Listar todos los Permisorol")
         unPermisorol = {
             "_id_Permisorol": "abc123",
             "_id_Permiso": "123",
             "_id_Rol": "1111",
         }
         return [unPermisorol]
    def create(self,elPermisorol):
         print("Crear un Permisorol")
         elPermisorol = Permisorol(infoPermisorol)
         return elPermisorol.__dict__
    def show(self,id):
         print("Mostrando un Permisorol con id ", id)
         elPermisorol = {
             "_id_Permisorol": "abc123",
             "_id_Permiso": "123",
             "_id_Rol": "1111",
         }
    def update(self, id, elPermisorol):
        print("Actualizando Permisorol con id ", id)
        elPermisorol = Permisorol(infoPermisorol)
        return elPermisorol.__dict__

    def delete(self, id):
        print("Elimiando Permisorol con id ", id)
        return {"deleted_count": 1}