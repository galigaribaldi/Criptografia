##Operacion Web, con la BD
import models as coneccion
#Generar Llaves Publica y privada
import rsagenerate as generador
##Descifrar y Cifrar
import rsacrp as operaciones

"""
###Generar las llaves Publica y privada
g = generador.NewKey()
privada = g.generatePrivateKey()
publica = g.generatePublicKey()
print(privada)
print(publica)

###Operaciones de encriptacion
input()
mensajeEncriptado  = operaciones.enc2(b'Nuevo mensaje', publica)
print("Mensaje Encriptado: ", mensajeEncriptado)

###Operaciones de DEsencriptacion
mensajeDesencripado = operaciones.des2(mensajeEncriptado, privada)
print("Mensaje Desencriptado: ", mensajeDesencripado)

coneccion.nuevo_usuario("Usuario", "Apellido", "Correo", privada)
coneccion.insertaClaves(9, publica, privada)
"""
