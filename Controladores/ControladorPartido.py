from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()
    def create(self,infoPartido):
        nuevoPartido=Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    def show(self,id):
        elPartido=Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    def update(self,id,infoPartido):
        PartidoActual=Partido(self.repositorioPartido.findById(id))
        PartidoActual.num_partido=infoPartido["num_partido"]
        PartidoActual.nombre_partido = infoPartido["nombre_partido"]
        PartidoActual.lema_partido = infoPartido["lema_partido"]
        return self.repositorioPartido.save(PartidoActual)
    def delete(self,id):
        return self.repositorioPartido.delete(id)

