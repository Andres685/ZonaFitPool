from cursorPoll import CursorDelPool
from logging_personalizado import log
from usuario import Usuario
class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuarios'
    _INSERTAR = 'INSERT INTO usuarios(usuario,passwort) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuarios SET usuario =%s, passwort = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando Usuarios')
            usuarios = []
            cursor.execute(cls._SELECCIONAR)
            for usuariose in cursor.fetchall():
                usuario = Usuario(usuariose[0], usuariose[1], usuariose[2])
                usuarios.append(usuario)
            return usuarios
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a Ingresar {usuario}')
            valores = (usuario.usuario, usuario.contraseña)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar {usuario}')
            valores = (usuario.usuario, usuario.contraseña, usuario.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    @classmethod
    def eliminar (cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a Eliminar {usuario}')
            cursor.execute(cls._ELIMINAR, (usuario.id_persona,))
            return cursor.rowcount
        
#Prueba de la clase DAO
if __name__ == '__main__':
    usuario1 = Usuario(usuario='daniela', contra='daniboli79')
    #Metodo Insertar
    #UsuarioDAO.insertar(usuario1)
    #Metodo Eliminar
    usuario1 = Usuario(id_persona=4)
    UsuarioDAO.eliminar(usuario1)
    #Metodo Actualizar
    usuarioact = Usuario(usuario='German', contra='gguzmanc', id_persona=3)
    UsuarioDAO.actualizar(usuarioact)
    #Metodo COnsulta
    personas = UsuarioDAO.seleccionar()
    for persona in personas:
        log.info(persona)