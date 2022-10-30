from Modelos.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self,infoResultado):
        nuevoResultado=Resultado(infoResultado)
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultado):
        ResultadoActual=Resultado(self.repositorioResultado.findById(id))
        ResultadoActual._id_resultado=infoResultado["_id_resultado"]
        ResultadoActual._id_mesa = infoResultado["_id_mesa"]
        ResultadoActual._id_candidato = infoResultado["_id_candidato"]
        ResultadoActual.num_votos = infoResultado["num_votos"]
        return self.repositorioResultado.save(ResultadoActual)
    def delete(self,id):
        return self.repositorioResultado.delete(id)
