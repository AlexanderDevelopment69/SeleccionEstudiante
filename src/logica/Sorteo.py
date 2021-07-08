from sqlalchemy import false
from sqlalchemy.orm import relationship

from src.modelo.Asignatura import Asignatura
from src.modelo.Actividad import Actividad
from src.modelo.Estudiante import Estudiante
from src.modelo.Equipo import Equipo



from src.modelo.declarative_base import engine, Base, session


class Sorteo():

    def _init_(self):
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

    def agregar_estudiante(self, apellidoPaterno, apellidoMaterno, nombres, elegible):
                if (apellidoPaterno == ""):
                    return False
                if (nombres == ""):
                    return False
                busqueda = session.query(Estudiante).filter(Estudiante.apellidoPaterno == apellidoPaterno,
                                                            Estudiante.apellidoMaterno == apellidoMaterno,
                                                            Estudiante.nombres == nombres,
                                                            Estudiante.elegible == elegible).all()
                if len(busqueda) == 0:
                    estudiante = Estudiante(apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno,
                                            nombres=nombres, elegible=elegible)
                    session.add(estudiante)
                    session.comit()
                    return True

                else:
                    return false
