import psycopg2

conexion = psycopg2.connect(user='postgres', password = 'admin', host = '127.0.0.1', port = '5432',database = 'test_db')
print(conexion) #Devuelve la direccion en memoria de la variable conexion

#Crear un cursos, el cual permitira ejecutar sentencias SQL
cursor = conexion.cursor()
sentencia  = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)
cursor.close()
conexion.close()
#Uso de with para cerrar todos los objetos asociados o creados a partir de la conexion
#Solo que a diferencia de otros usos de este mismo, este no cierra la conexion automaticamente
#Para eso se usa un bloque try-except y finally, para que en el finally se cierre la conexion
conexion = psycopg2.connect(user='postgres', password = 'admin', host = '127.0.0.1', port = '5432',database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()

#Uso del recuperador ficthone
conexion = psycopg2.connect(user='postgres', password = 'admin', host = '127.0.0.1', port = '5432',database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona= input('Que Id desea consultar? ')
            cursor.execute(sentencia,(id_persona,))
            registros = cursor.fetchone() #Solo regresara un solo registro y asi optimizar el codigo, que solo recupere la primera ocurrencia 
            print(registros)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()
    
#Uso del recuperador ficthall
conexion = psycopg2.connect(user='postgres', password = 'admin', host = '127.0.0.1', port = '5432',database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            #llaves_id = ((1,2,3),)
            entrada = input('Proporciona los ids a buscar (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),) #Crea una tupla de tuplas, eso porque el IN de sql, requiere una tupla
            cursor.execute(sentencia,llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()