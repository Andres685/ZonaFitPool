class Usuario:
    def __init__(self,id_persona = None, usuario = None, contra = None):
        self._id_persona = id_persona
        self._usuario = usuario
        self._contra = contra
    @property
    def id_persona(self):
        return self._id_persona
    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self,usuario):
        self._usuario = usuario
    @property
    def contraseña(self):
        return self._contra
    @contraseña.setter
    def contraseña(self,contra):
        self._contra = contra
    def __str__(self):
        return f'Id_Persona:{self._id_persona}, Usuario: {self._usuario}, Contraseña: {self._contra}'
    
#Prueba de la clase
if  __name__ == '__main__':
    usuario1 = Usuario(id_persona=1, usuario='Andres',contra='ag685' )
    #ACCESO Y USO DEL METODO SETTER:
    usuario1.contraseña = 'blblblblblb'
    #prueba de metodos get y str
    print(usuario1.contraseña)
    print(usuario1)