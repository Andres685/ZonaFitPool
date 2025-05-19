import psycopg2
from conexion import Conexion
from logger_base import log
from persona import Persona
from cursor_del_pool import CursorDelPool
class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _UPDATE = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    _DETELETE = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
        
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona Insertada: {persona}')
            return cursor.rowcount
    @classmethod
    def actualizar (cls,persona):
        with CursorDelPool() as cursor:
            valores= (persona.nombre, persona.apellido,persona.email,persona.id_persona)
            cursor.execute(cls._UPDATE,valores)
            log.debug(f'Persona actualizada, nuevos valores: {persona}')
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,persona):
        with CursorDelPool() as cursor:
            valor = persona.id_persona
            cursor.execute(cls._DETELETE, (valor,))
            log.debug(f'Persona Eliminada : {persona}')
            return cursor.rowcount
if __name__ =='__main__':    
    
    #Insertar un Registro
    '''
    persona1 = Persona(nombre='Alejandra', apellido='Sanchez',email='sancha@mail.com')
    Personas_Ingresadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas Ingresadas: {Personas_Ingresadas}') 
    '''
    #Actualizar Registro
    #persona2 = Persona(id_persona =16, nombre='Andres', apellido='Guzman',email='guzandres685@gmial.com')
    #Personas_actualizadas = PersonaDAO.actualizar(persona2)
    #log.debug(f'Personas Actulizadas con id = {persona2.id_persona}: {Personas_actualizadas}')
    #Eliminar Registro
    #persona1 = Persona(id_persona=18)
    #persona_eliminada = PersonaDAO.eliminar(persona1)
    #log.debug(f'Perosnas Eliminadas con id: {persona1.id_persona} = {persona_eliminada}')
    #Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.info(persona)  