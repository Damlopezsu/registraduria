from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
         print("Creando ControladorCandidato")
    def index(self):
         print("Listar todos los Candidato")
         unCandidato = {
             "cedula_candidato": "123567",
             "nombre_candidato": "jose",
             "apellido_candidato": "ruiz",
            "num_resolucion": "30",
            "id_partido": "11",
         }
         return [unCandidato]
    def create(self,infoCandidato):
         print("Crear un Candidato")
         elCandidato = Candidato(infoCandidato)
         return elCandidato.__dict__
    def show(self,id):
         print("Mostrando un Candidato con id ", id)
         elCandidato = {
            "cedula_candidato": id,
             "nombre_candidato": "jose",
             "apellido_candidato": "ruiz",
            "num_resolucion": "30",
            "id_partido": "11",
         }
         return elCandidato

    def update(self, id, infoCandidato):
        print("Actualizando Candidato con id ", id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__

    def delete(self, id):
        print("Elimiando Candidato con id ", id)
        return {"deleted_count": 1}