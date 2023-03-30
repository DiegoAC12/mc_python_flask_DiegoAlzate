from tutorialFUP.Modelos.Estudiante import Estudiante
from tutorialFUP.Repositorios.RepositorioEstudiante import RepositorioEstudiante

"""
#########################################################################################################################
REALIZAR LOS REPOSITORIOS PARA CADA MODELO, LOS CONTROLADORES Y MODIFICAR LOS MODELOS. HACER UN PDF PARA EL 29 DE MARZO.
#########################################################################################################################

Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorEstudiante():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        print("Creando ControladorEstudiante")
        self.repositorioEstudiante = RepositorioEstudiante()

    def index(self):
        print("Listar todos los estudiantes")
        return self.repositorioEstudiante.findAll()

    """
            unEstudiante = {
                "_id": "abc123",
                "cedula": "123",
                "nombre": "Juan",
                "apellido": "Perez"
            }

            return [unEstudiante]"""

    def create(self, elEstudiante):
        print("Crear un estudiante")
        nuevoEstudiante = Estudiante(elEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)
        """
        elEstudiante = Estudiante(elEstudiante)
        return elEstudiante.__dict__
        """

    def show(self, id):
        print("Mostrando un estudiante con id ", id)
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
        """
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante
        """

    def update(self, id, elEstudiante):
        print("Actualizando estudiante con id ", id)
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula = elEstudiante["cedula"]
        estudianteActual.nombre = elEstudiante["nombre"]
        estudianteActual.apellido = elEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)
        """
        elEstudiante = Estudiante(elEstudiante)
        return elEstudiante.__dict__
        """

    def delete(self, id):
        print("Elimiando estudiante con id ", id)
        return self.repositorioEstudiante.delete(id)
        """
        return {"deleted_count": 1}
        """
