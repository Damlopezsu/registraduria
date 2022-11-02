from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        CandidatoActual=Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula_candidato=infoCandidato["cedula_candidato"]
        CandidatoActual.nombre_cand = infoCandidato["nombre_candidato"]
        CandidatoActual.apellido_cand = infoCandidato["apellido_candidato"]
        CandidatoActual.num_resolucion = infoCandidato["numero_resolucion"]
        CandidatoActual._id_partido = infoCandidato["_id_partido"]
        return self.repositorioCandidato.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)