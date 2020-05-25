##Operacion Web, con la BD
import models as coneccion
#Generar Llaves Publica y privada
import rsagenerate as generador
##Descifrar y Cifrar
import rsacrp as operaciones


###Generar las llaves Publica y privada
#g = generador.NewKey()
#publica = g.generatePublicKey()
##privada = g.generatePrivateKey()
#print(publica)
##print(privada)
"""
###Operaciones de encriptacion
input()
mensajeEncriptado  = operaciones.enc2(b'Nuevo mensaje', publica)
print("Mensaje Encriptado: ", mensajeEncriptado)

###Operaciones de DEsencriptacion
mensajeDesencripado = operaciones.des2(mensajeEncriptado, privada)
print("Mensaje Desencriptado Numero 2: ", mensajeDesencripado)

coneccion.nuevo_usuario("Usuario2", "Apellido2", "Correo2", privada)
coneccion.insertaClaves(10, publica, privada)
"""
#operaciones.enc2(b"Mensaje nuevo",)
#d = coneccion.consulta_llaves(10)
#print(bytes(d[0][1]))#Private Key
##print(bytes(d[0][0]))#Public Key
#me = operaciones.enc2(b"Mensaje nuevo 2",bytes(d[0][0]))
#print(me)
#md = operaciones.des2(bytes(me), bytes(d[0][1]))
#print(md)
##Actualizar Password:
#coneccion.actualizar_password(9, b"password")
"""
d = coneccion.consulta_usuario_id(9)
print(bytes(d[0][4]))
c = ((bytes(d[0][4])))
p = 'password'
if c == bytes(p, 'utf8'):
    print("dio")
"""

#input("Consulta por correo")
d = coneccion.consulta_usuario_correo("Correo")
#print("Contraseña del usuario: ", bytes(d[0][4]))

#input("Consulta de la llave: ")
PK = coneccion.consulta_llaves(d[0][0])
#print("Consulta de la llave privada: " ,bytes(PK[0][1]))

#input("Actualizando Contraseña Encriptada")
#passwordEncriptado = operaciones.enc2(b"password2",bytes(PK[0][1]) )
#input("Actualizada!")
#coneccion.actualizar_password(9, passwordEncriptado)

c = operaciones.des2(bytes(d[0][4]), bytes(PK[0][1]))
print(c)
opcion = input("Dame el password: ")
if bytes(opcion, 'utf8') == c:
    print("Entraste")
else:
    print("Fuera! ")