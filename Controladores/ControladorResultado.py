from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
         print("Creando ControladorResultado")
    def index(self):
         print("Listar todos los Resultado")
         unResultado = {
             "id_Resultado": "abc",
             "id_mesa": "23",
             "id_candidato": "Juan",
              "num_votos": "30",
         }
         return [unResultado]
    def create(self,infoResultado):
         print("Crear un Resultado")
         elResultado = Resultado(infoResultado)
         return elResultado.__dict__
    def show(self,id):
         print("Mostrando un Resultado con id ", id)
         elResultado = {
             "id_Resultado":id,
             "id_mesa": "123",
             "id_candidato": "Juan",
             "num_votos": "30",
         }
         return elResultado

    def update(self, id, infoResultado):
        print("Actualizando Resultado con id ", id)
        elResultado = Resultado(infoResultado)
        return elResultado.__dict__

    def delete(self, id):
        print("Elimiando Resultado con id ", id)
        return {"deleted_count": 1}