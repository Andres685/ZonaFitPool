import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432',database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES(%s, %s,%s)'
            valores = ('carlos', 'lara', 'clara@mail.com')
            cursor.execute(sentencia,valores)
            registros_insertados = cursor.rowcount
            print(f'Rgistros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()
    
#Insercion de varios Registros
conexion = psycopg2.connect(user = 'postgres', password = 'admin', host='127.0.0.1', port = '5432', database = 'test_db')
try:
    with conexion: 
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
            valores=(('Carlitos','Vaca','cala@mail.com'),
                 ('Migelon', 'Cobarrubia', 'mcobarrubia@mail.com'),
                 ('Angel', 'Quintana', 'aquintana@mail.com'))
            cursor.executemany(sentencia,valores)
            registros = cursor.rowcount
            print(f'Registros Insertados {registros}')
except Exception as e:
    print(f'Ourrio un Error {e}')
finally:
    conexion.close()
