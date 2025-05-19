from logger_base import log
from conexion import Conexion
class CursorDelPool:
    def __init__(self):     
        self._conexion = None
        self._cursor = None
        
    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__') #Metodo encargado de obtener la conexion
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self,tipo_excepcion,valor_excepcion,detalle_excepcion): #Metodo que se llama cuando se manda a cerrar o temrina el bloque with
        log.debug('Se ejecuta Metodo __exit__()')
        if valor_excepcion: #Si el valor de la excpecion es diferente de None tons, si ocurrio un error y se hace rollback de la transaccion
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug(f'Se hizo Commit(de la transaccion)')  
        self._cursor.close() #Se cierra el cursor si hubo rollback o commit
        Conexion.liberarConexion(self._conexion) #Se libera la conexion de la clase

if __name__== '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
           