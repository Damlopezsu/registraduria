from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
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
        CandidatoActual.num_candidato=infoCandidato["num_candidato"]
        CandidatoActual.cedula_candidato=infoCandidato["cedula_candidato"]
        CandidatoActual.nombre_cand = infoCandidato["nombre_candidato"]
        CandidatoActual.apellido_cand = infoCandidato["apellido_candidato"]
        CandidatoActual.num_resolucion = infoCandidato["numero_resolucion"]
        CandidatoActual.num_partido = infoCandidato["num_partido"]
        return self.repositorioCandidato.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)