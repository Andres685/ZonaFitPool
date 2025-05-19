from usuarioDAO import UsuarioDAO
from logging_personalizado import log
from usuario import Usuario
import sys
'''
salir = False
while not salir:
    print(f'Opciones:\n1. Listar Usuarios\n2. Agregar Usuario\n3. Modificar Usuario\n4. Eliminar Usuario\n5. Salir')
    opcion = int(input('Escribe Tu Opción (1-5): ').strip())
    if 1<=opcion<=5:
        if opcion == 1:
            print(' Lista de Todos los Usuarios:')
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                log.info(f'{usuario}\n')
        elif opcion == 2:
            print(' Ingresar Usuario:')
            usuario_ingresar = input('   Escibe el Username: ').strip()
            passwor_ingresar = input('   Escibe el Passworod: ').strip()
            usuario = Usuario(usuario=usuario_ingresar, contra=passwor_ingresar)
            valores_ingresados = UsuarioDAO.insertar(usuario)
            log.info(f'Usuarios Insertados: {valores_ingresados}\n')
        elif opcion == 3:
            print(' Actualizar Usuario:')
            id_actualizar = input('   Escribe el id_usuario a modificar: ').strip()
            usuario_actualizar = input('   Escibe el nuevo Username: ').strip()
            password_actualizar = input('   Escribe el Nuevo password: ').strip()
            usuario = Usuario(id_actualizar, usuario_actualizar,password_actualizar)
            valores_actualizados = UsuarioDAO.actualizar(usuario)
            log.info(f'Usuarios Actualizados: {valores_actualizados}\n')
        elif opcion == 4:
            print(' Eliminar Usuario')
            id_eliminar = input('   Escribe el id_usuario a eliminar: ').strip()
            usuario = Usuario(id_persona=id_eliminar)
            valores_eliminados = UsuarioDAO.eliminar(usuario)
            log.info(f'Usuario Eliminados: {valores_eliminados}')
        elif opcion == 5:
            print(f'Saliendo dle programa :)......\n')
            salir = True
    else:
        print('Opcion No valida >:(\n')
'''
#Metodo 2
        
def mostrar_menu():
    print(f'Opciones:\n1. Listar Usuarios\n2. Agregar Usuario\n3. Modificar Usuario\n4. Eliminar Usuario\n5. Salir')
    opcion = validar_opcion()
    return opcion
        
def validar_opcion():
    while True:
        try: 
            opcion = int(input('Escribe Tu opcion (1-5): ').strip())
            if 1<= opcion <=5:
                return opcion
            else:
                print('Opcion Fuera de Rango\n')
        except ValueError as e:
            print(f'Opcion no valida. Intenta de Nuevo {e}\n')
    
def listar_usuarios():
    print(' Lista de Todos los Usuarios:')
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
                log.info(f'{usuario}\n')

def insertar_usuarios():
    print(' Insertar Usuarios:')
    usuario_ingresar = input('   Escibe el Username: ').strip()
    passwor_ingresar = input('   Escibe el Passworod: ').strip()
    usuario = Usuario(usuario=usuario_ingresar, contra=passwor_ingresar)
    valores_ingresados = UsuarioDAO.insertar(usuario)
    log.info(f'Usuarios Insertados: {valores_ingresados}\n')
    
def actualizar_usuario():
    print(' Actualizar Usuarios:')
    id_actualizar = input('   Escribe el id_usuario a modificar: ').strip()
    usuario_actualizar = input('   Escibe el nuevo Username: ').strip()
    password_actualizar = input('   Escribe el Nuevo password: ').strip()
    usuario = Usuario(id_persona=id_actualizar, usuario=usuario_actualizar, contra=password_actualizar)
    valores_actualizados = UsuarioDAO.actualizar(usuario)
    log.info(f'Usuarios Actualizados: {valores_actualizados}\n')

def eliminar_usuario():
    print(' Eliminar Usuario')
    id_eliminar = input('   Escribe el id_usuario a eliminar: ').strip()
    usuario = Usuario(id_persona=id_eliminar)
    valores_eliminados = UsuarioDAO.eliminar(usuario)
    log.info(f'Usuario Eliminados: {valores_eliminados}')
    
def ejecutar_menu():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            listar_usuarios()
        elif opcion == 2: 
            insertar_usuarios()
        elif opcion == 3: 
            actualizar_usuario()
        elif opcion == 4: 
            eliminar_usuario()
        elif opcion == 5:
            print('Saliendo Del Programa :)\n')
            break
#PRUEBA
ejecutar_menu()