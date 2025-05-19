import psycopg2
from conexion import Conexion
from logger_base import log
from persona import Persona
class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _DETELETE = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor: #Como no se trata d euna conexion, si no sdirectamente una consulta, no se usa el with anidado con conexion, si no solo el cursor
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
        
    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerConexion() as conexion: #Este si usa el metodo de oobbtener conexion, pues reuiqere del commit automatica al tratarse de una transaccion
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount
    @classmethod
    def actualizar (cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores= (persona.nombre, persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._UPDATE,valores)
                log.debug(f'Persona actualizada, nuevos valores: {persona}')
                return cursor.rowcount
    
    @classmethod
    def eliminar (cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valor = persona.id_persona
                cursor.execute(cls._DETELETE, (valor,))
                log.debug(f'Persona Eliminada : {persona}')
                return cursor.rowcount
if __name__ =='__main__':
    #INSERTAR UN REGISTRO
    '''
    persona1 = Persona(nombre='Pedro',apellido='Najera',email='pajera@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas Insertadas {personas_insertadas}')
    #Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
    
    #Actulizar Registro
    persona2 = Persona(nombre='Andres', apellido='Guzman', email='guzman@mail.com', id_persona=1)
    persona_actualizada = PersonaDAO.actualizar(persona2)
    log.debug(f'Personas Actualizadas {persona_actualizada}') 
    '''
    #Eliminar Registro
    #persona3 = Persona(id_persona=15)
    #personas_eliminadas = PersonaDAO.eliminar(persona3)
    #log.debug(f'Personas Eliminadas: {personas_eliminadas}')
    
    #Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)