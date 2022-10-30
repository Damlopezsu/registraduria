from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,id):
        elMesa=Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__
    def update(self,id,infoMesa):
        MesaActual=Mesa(self.repositorioMesa.findById(id))
        MesaActual._id_mesa=infoMesa["_id_mesa"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)