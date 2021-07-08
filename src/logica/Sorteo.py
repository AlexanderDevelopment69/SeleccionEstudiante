from sqlalchemy.orm import relationship

from src.modelo.Asignatura import Asignatura
from src.modelo.Actividad import Actividad
from src.modelo.Estudiante import Estudiante
from src.modelo.Equipo import Equipo



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

        def agregar_estudiante(self, nombreEstudiante):
            busqueda = session.query(Estudiante).filter(Estudiante.nombreEstudiante == nombreAsignatura).all()

            if len(busqueda) == 0:
                estudiante = Estudiante(nombreEstudiante=nombreEstudiante)
                session.add(estudiante)
                session.commit()
                return True
            else:
                return False

        def agregar_equipo(self, nombreEquipo):
            busqueda = session.query(Equipo).filter(Equipo.nombreEquipo == nombreEquipo).all()

            if len(busqueda) == 0:
                equipo = Equipo(nombreEquipo=nombreEquipo)
                session.add(equipo)
                session.commit()
                return True
            else:
                return False

        def agregar_actividad(self, nombreActividad):
            busqueda = session.query(Actividad).filter(Actividad.nombreActividad == nombreActividad).all()

            if len(busqueda) == 0:
                actividad = Actividad(nombreActividad=nombreActividad)
                session.add(actividad)
                session.commit()
                return True
            else:
                return False

