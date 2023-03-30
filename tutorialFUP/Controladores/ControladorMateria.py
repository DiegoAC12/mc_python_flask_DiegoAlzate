from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria
from tutorialFUP.Repositorios.RepositorioDepartamento import RepositorioDepartamento
from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Modelos.Departamento import Departamento


class ControladorMateria:
    def __init__(self):
        print("Creando ControladorMateria")
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        print("Listar todas los materias")
        return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        print("Crear una materia")
        nuevaMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevaMateria)

    def show(self, id):
        print("Listando materias por ID")
        laMateria = Materia(self.repositorioMateria.findById(id))
        return laMateria.__dict__

    def update(self, id, infoMateria):
        print("Actualizando materias con ID")
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        print("Eliminando materias por ID")
        return self.repositorioMateria.delete(id)

    """
    Relación departamento y materia
    """
    def asignarDepartamento(self, id, id_departamento):
        print("Asignando la relacion materia departamento")
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)
