import psycopg2
conexion = psycopg2.connect(user = 'postgres', password = 'admin', host='127.0.0.1', port = '5432', database='test_db')
try:
    #No se va a manejar with en este caso, para usar manualmente el commit() y rollback()
    conexion.autocommit = False #Anula guardar los cambios automaticos
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    valores=('Carlos', 'Esparta','cariae@mail.com')
    cursor.execute(sentencia,valores)
    
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan', 'Gabriel', 'jgabriel@mail.com',1)
    cursor.execute(sentencia,valores)
    
    conexion.commit() #Guarda la transaccion
    print(f'Termina la Transaccion, se hizo Commit ')
    
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback de la transaccion {e}')
finally:
    conexion.close()
    
#Manejo de transaccion con with
conexion = psycopg2.connect(user = 'postgres', password = 'admin', host='127.0.0.1', port = '5432', database='test_db')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores=('Alex', 'Rojas','RojasAlex@mail.com')
            cursor.execute(sentencia,valores)
            
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Daniela', 'Gonzales', 'dgonzales@mail.com',3)
            cursor.execute(sentencia,valores)
    
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback de la transaccion {e}')
finally:
    conexion.close()

print(f'Termina la Transaccion, se hizo Commit ')