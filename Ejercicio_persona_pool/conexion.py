import sys
import psycopg2
from logger_base import log
from psycopg2 import pool
class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON=1
    _MAX_CON=5
    _pool = None
    #_cursor = None   - estos dos objetos ya no sera andministrados desde esta clase
    #_conexion = None  - e creara una clase mas para poder administrar estos objetos
    @classmethod
    def obtener_pool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON, host=cls._HOST, user =cls._USERNAME, password=cls._PASSWORD, port = cls._DB_PORT, database = cls._DATABASE)
                log.debug(f'Creacion del Pool Exxitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
                sys.exit()  
        else:
                return cls._pool  
    
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f'Conexion Obtenida del pool: {conexion}')
        return conexion
    @classmethod
    def liberarConexion (cls,conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()
    
            
#Prueba de la clase Conexion
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion() #Un cliente usa un objeto de tipo conexion del pool
    Conexion.liberarConexion(conexion1) #El cliente deja de usar el objjeto y se libera
    conexion2 = Conexion.obtenerConexion() #Otro cliente u otra peticion de conexion del pool
    #Tal vez asigne el mismo objeto a esta nueva conexion
        
    
    