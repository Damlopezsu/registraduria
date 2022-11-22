from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId
class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoResultadoCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    def getMayorResultadoPorCandidato(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "max": {
                    "$max": "$resultado_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        return self.queryAgregation(pipeline)

    def promedioResultadosCandidatos(self, id_candidato):
        query1 = {
            "$match": {"candidatos.$id": ObjectId(id_candidato)}
        }
        query2 = {
            "$group": {
                "_id": "$candidato",
                "resultado": {
                    "$avg": "$num_votos"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def test(self, id_candidato):
        query1 = {
            "$match": {"candidato.$id": ObjectId(id_candidato)}
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)