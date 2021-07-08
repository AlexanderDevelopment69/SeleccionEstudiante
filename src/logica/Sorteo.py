from src.modelo.Asignatura import Asignatura
from src.modelo.Estudiante import Estudiante
from src.modelo.declarative_base import engine, Base, session


class Sorteo():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_asignatura(self, nombreAsignatura):
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False

    def agregar_estudiante(self, apellidoPaterno):
        busqueda = session.query(Estudiante).filter(Estudiante.apellidoPaterno == apellidoPaterno).all()
        if len(busqueda) == 0:
            asignaturas= Estudiante(apellidoPaterno=apellidoPaterno)

            session.add(Estudiante)
            session.commit()
            return True
        else:
            return False

