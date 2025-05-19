
from conexion_pool import ConexionPool
from logging_personalizado import log
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
    
    def __enter__(self):
        self._conexion = ConexionPool.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipo_excep, valor_excep, detalle_excep):
        if valor_excep:
            log.error(f'Ocurrio Un error en la transaccion se hara Rollback')
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        ConexionPool.liberar_conexion(self._conexion)
    