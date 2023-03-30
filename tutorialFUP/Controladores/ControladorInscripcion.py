from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Modelos.Estudiante import Estudiante
from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Repositorios.RepositorioInscripcion import RepositorioInscripcion
from tutorialFUP.Repositorios.RepositorioEstudiante import RepositorioEstudiante
from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria


class ControladorInscripcion():
    def __init__(self):
        print("Creando ControladorInscripcion")
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioEstudiantes = RepositorioEstudiante()
        self.repositorioMaterias = RepositorioMateria()

    def index(self):
        print("Listar todas las inscripciones")
        return self.repositorioInscripcion.findAll()

    def create(self, infoInscripcion, id_estudiante, id_materia):
        nuevaInscripcion = Inscripcion(infoInscripcion)
        elEstudiante = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        nuevaInscripcion.estudiante = elEstudiante
        nuevaInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        elInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return elInscripcion.__dict__

    def update(self, id, infoInscripcion, id_estudiante, id_materia):
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        laInscripcion.anio = infoInscripcion["año"]
        laInscripcion.semestre = infoInscripcion["semestre"]
        laInscripcion.notaFinal = infoInscripcion["nota_final"]
        elEstudiante = Estudiante(self.repositorioEstudiantes.findById(id_estudiante))
        laMateria = Materia(self.repositorioMaterias.findById(id_materia))
        laInscripcion.estudiante = elEstudiante
        laInscripcion.materia = laMateria
        return self.repositorioInscripcion.save(laInscripcion)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)
