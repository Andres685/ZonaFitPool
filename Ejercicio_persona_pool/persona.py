from logger_base import log
class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre=nombre
        self._apellido = apellido
        self._email = email
    @property
    def nombre (self):
        return self._nombre
    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor
    
    @property
    def apellido (self):
        return self._apellido
    @apellido.setter
    def apellido(self,valor):
        self._apellido = valor
        
    @property
    def email (self):
        return self._email
    @email.setter
    def email(self,valor):
        self._email = valor
        
    @property
    def id_persona (self):
        return self._id_persona
        
    def __str__(self):
        return f'Id: {self._id_persona}\nNombre: {self._nombre}\nApellido: {self._apellido}\nEmail: {self._email}'

#Prueba de la Clase Persona
if __name__ == '__main__':
    print('Clase Persona test')
    persona1 = Persona(id_persona = 1,nombre ='andres',apellido = 'Guzman',email='aguzman@mail.com')
    print(persona1)
    log.debug(persona1)
    print(f'Nombre de la persona {persona1.nombre}')