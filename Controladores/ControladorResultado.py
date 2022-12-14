from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self,infoResultado,id_mesa,id_candidato):
        nuevoResultado=Resultado(infoResultado)
        elMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        laCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = elMesa
        nuevoResultado.candidato = laCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultado,id_mesa,id_candidato):
        resultadoActual=Resultado(self.repositorioResultado.findById(id))
        resultadoActual.num_resultado=infoResultado["num_resultado"]
        resultadoActual.num_votos = infoResultado["num_votos"]
        elMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        laCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultadoActual.mesa = elMesa
        resultadoActual.candidato = laCandidato
        return self.repositorioResultado.save(resultadoActual)
    def delete(self,id):
        return self.repositorioResultado.delete(id)

    def listarInscritosCandidatos(self, id_candidato):
        return self.repositorioResultado.getListadoResultadoCandidato(id_candidato)