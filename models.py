import psycopg2
import rsacrp as opeaciones
host = "ec2-23-22-156-110.compute-1.amazonaws.com"
database = "dfik7jcpmsldvr" 
user = "gkpagpicxkmkkg"
password = "59fec8e49626d750d287d0921984944c08bd4a5598d03f7d15a92d7ef0456cc7" 

###Crear una nueva cuenta sin el password
def nuevo_usuario(nombre, apellido, correo_electroncio):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuario(nombre, apellido, correo_electronico) VALUES(%s, %s, %s)",(nombre, apellido, correo_electroncio))
    conexion.commit()
    cursor.close()
    conexion.close()

##Actualizar el password a usuario
def actualizar_password(ids, pass2):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuario SET password=%s WHERE usuario_id=%s",(pass2, ids))
    conexion.commit()
    cursor.close()
    conexion.close()
    
def insertaClaves(id_usuario,public, private):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clave(usuario_id, public_key, private_key) VALUES(%s, %s, %s)",(id_usuario,public, private))
    conexion.commit()
    cursor.close()
    conexion.close()
def consulta_usuario():
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario")
    datos_estudiantes = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return datos_estudiantes

def consulta_usuario_id(ids):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario WHERE usuario_id=%s",(ids,))
    datos_estudiantes = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return datos_estudiantes

def consulta_usuario_correo(correo):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario WHERE correo_electronico=%s",(correo,))
    datos = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return datos

def consulta_llaves(ids):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("SELECT public_key, private_key FROM clave WHERE usuario_id=%s",(ids,))
    datos_eclave = cursor.fetchall()
    conexion.commit()
    cursor.close()
    conexion.close()
    return datos_eclave
"""
mypic = open('textoCifrado.txt', 'rb').read()
nuevo_usuario("Usuario", "Apellido", "Correo",mypic )
d = consulta_usuario()
i = bytes(d[0][4])
#print(i)
opeaciones.des2(i)
"""

