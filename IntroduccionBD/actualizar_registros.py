import psycopg2
conexion = psycopg2.connect(user = 'postgres',password = 'admin', host='127.0.0.1', port = '5432', database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            id_persona = input('Digite el Registro que desea actualizar: ')
                        #Nombre      #Apellido  #Correo            #id_persona
            valores = ('JeanCarlos', 'ardila', 'jeanardila@mail.com',  id_persona)
            cursor.execute(sentencia,valores)
            registros_Act = cursor.rowcount
            print(f'Registros Actualizados: {registros_Act}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()
    
    
print('Actualizacion de Varios Registros'.center(50,'*'))
#Actulizar Varios Registros
conexion = psycopg2.connect(user = 'postgres',password = 'admin', host='127.0.0.1', port = '5432', database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
                        #Nombre      #Apellido  #Correo            #id_persona
            valores = (('JeanCarlos', 'ardila', 'jeanardila@mail.com', 1),
                       ('Jean', 'Diaz', 'jeandia@mail.com', 2 ))
            cursor.executemany(sentencia,valores)
            registros_Act = cursor.rowcount
            print(f'Registros Actualizados: {registros_Act}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()
            
            