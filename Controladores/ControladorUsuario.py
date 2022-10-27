from Modelos.Usuario import Usuario
class ControladorUsuario():
    def __init__(self):
         print("Creando ControUsuario")
    def index(self):
         print("Listar todos los Usuario")
         unUsuario = {
             "cedula": "79542749",
             "seudonimo": "JuanitoP",
             "correo": "juanperez@gmail.com",
             "contraseña": "JPerez59"
         }
         return [unUsuario]
    def create(self,infoUsuario):
         print("Crear un Usuario")
         elUsuario = Usuario(infoUsuario)
         return elUsuario.__dict__
    def show(self,id):
         print("Mostrando un Usuario con id ", id)
         elUsuario = {
             "cedula": id,
             "seudonimo": "JuanitoP",
             "correo": "juanperez@gmail.com",
             "contraseña": "JPerez59"
         }
         return elUsuario

    def update(self, id, infoUsuario):
        print("Actualizando Usuario con id ", id)
        elUsuario = Usuario(infoUsuario)
        return elUsuario.__dict__

    def delete(self, id):
        print("Elimiando Usuario con id ", id)
        return {"deleted_count": 1}