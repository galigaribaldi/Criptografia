import psycopg2
import rsacrp as opeaciones
host = "ec2-23-22-156-110.compute-1.amazonaws.com"
database = "dfik7jcpmsldvr" 
user = "gkpagpicxkmkkg"
password = "59fec8e49626d750d287d0921984944c08bd4a5598d03f7d15a92d7ef0456cc7" 

def nuevo_usuario(nombre, apellido, correo_electroncio,pass2):
    conexion = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuario(nombre, apellido, correo_electronico, password) VALUES(%s, %s, %s, %s)",(nombre, apellido, correo_electroncio, pass2))
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
"""
mypic = open('textoCifrado.txt', 'rb').read()
nuevo_usuario("Usuario", "Apellido", "Correo",mypic )
d = consulta_usuario()
i = bytes(d[0][4])
#print(i)
opeaciones.des2(i)
"""

