from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
         print("Creando ControladorMesa")
    def index(self):
         print("Listar todos los Mesa")
         unMesa = {
             "_id_Mesa": "a1",
             "cantidad_inscritos": "123",
         }
         return [unMesa]
    def create(self,infoMesa):
         print("Crear una Mesa")
         elMesa = Mesa(infoMesa)
         return elMesa.__dict__
    def show(self,id):
         print("Mostrando unq Mesa con id ", id)
         elMesa = {
             "_id_Mesa": id,
             "cantidad_inscritos": "123",

         }
         return elMesa

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        elMesa = Mesa(infoMesa)
        return elMesa.__dict__

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        return {"deleted_count": 1}