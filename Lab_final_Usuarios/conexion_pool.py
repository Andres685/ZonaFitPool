from psycopg2 import pool
import sys
class ConexionPool:
    _DATABASE = 'laboratorio_db'
    _HOST = '127.0.0.1'
    _PORT = '5432'
    _USER = 'postgres'
    _PASSWORD = 'admin'
    _MiN_POOL = 1
    _MAX_POOL = 5
    _POOL = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._POOL == None:
            try:
                cls._POOL = pool.SimpleConnectionPool(cls._MiN_POOL,cls._MAX_POOL, user = cls._USER, password = cls._PASSWORD, host = cls._HOST, port = cls._PORT, database = cls._DATABASE)
                return cls._POOL
            except Exception as e:
                print(f'Ocurrio un error {e}')
                sys.exit() 
        else:
            return cls._POOL
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        return conexion
    
    @classmethod
    def liberar_conexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
    
    @classmethod
    def cerrar_todo(cls):
        cls.obtenerPool().closeall()
        