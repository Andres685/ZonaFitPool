import sys
import psycopg2
from logger_base import log
class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _cursor = None
    _conexion = None
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = psycopg2.connect(user = cls._USERNAME, password = cls._PASSWORD, host =  cls._HOST, port= cls._DB_PORT, database = cls._DATABASE)
                log.debug(f'Conexion Exitosa {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener la conexion {e}')
                sys.exit()
        else:
            return cls._conexion
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Cursor Creado EXITOSAMENTE {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio Un error al obtener el cursor {e}')
                sys.exit()
        else:
            return cls._cursor
            
    
    @classmethod
    def cerrar(cls):
        try:
            if cls._cursor is not None:
                cls._cursor.close()
                cls._cursor = None
                log.debug(f'Cursor Cerrado Exitosamente')
        except Exception as e:
            log.error(f'Ocurrio un error al cerrar el cursor {e}')
        
        try:
            if cls._conexion is not None:
                cls._conexion.close()
                cls._conexion = None
                log.debug(f'Conexion Cerrada Exitosamente')
        except Exception as e:
            log.error(f'Ocurrio un error al cerrar la conexion {e}')
            
#Prueba de la clase Conexion
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    Conexion.cerrar()
        
    
    