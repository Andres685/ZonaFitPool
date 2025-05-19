import psycopg2
conexion = psycopg2.connect(user = 'postgres',password = 'admin', host='127.0.0.1', port = '5432', database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            entrada = input('Proporciona el id_persona a eliminar: ')
            id_persona = tuple(entrada)
            cursor.execute(sentencia,id_persona)
            registros_eli = cursor.rowcount
            print(f'Registros Eliminados: {registros_eli}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()

#Eliminar varios Registros
print(' Eliminar varios Registros '.center(40,'-'))
conexion = psycopg2.connect(user = 'postgres',password = 'admin', host='127.0.0.1', port = '5432', database = 'test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona el id_persona a eliminar (separados por comas): ').split(',')
            valores =tuple(entrada)
            cursor.execute(sentencia,(valores,))
            registros_eli = cursor.rowcount
            print(f'Registros Eliminados: {registros_eli}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()