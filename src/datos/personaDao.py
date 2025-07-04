from src.datos.conexion import Conexion
from src.dominio.persona import Persona


class PersonaDao:
    _ERROR_ = -1
    _INSERT = ("INSERT INTO Persona (Nombre, apellido, cedula,"
               "Sexo, email) values (?, ?, ?, ?, ?)")



    @classmethod
    def insertar_persona(cls, persona):
        try:
            #cursor = Conexion.obtenerCursor()
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula,
                         persona.sexo, persona.email,)
                retorno = cursor.execute(cls._INSERT, datos)


                return retorno.rowcount

        except Exception as e:
            print(e)
            cursor.rollback()
            return cls._ERROR_



if __name__ == '__main__':
    p1 = Persona('Karen2', 'Carvo', '0123456789', 'F', 'arielandres779@gmail.com')
    PersonaDao.insertar_persona(p1)





