##Operacion Web, con la BD
import models as coneccion
#Generar Llaves Publica y privada
import rsagenerate as generador
##Descifrar y Cifrar
import rsacrp as operaciones
###Correos
import correo as enviar

#####################################################
def mensaje_cifrado(id,msg2):
    id=int(id)
    msg2 = str(msg2)
    PK = coneccion.consulta_llaves(id)
    ##Se cifra el mensaje
    msg2_enc = operaciones.enc2(bytes(msg2, 'utf8'), bytes(PK[0][0]))
    print("Mensaje Cifrado del usuar¡o con id: "+ str(id)+" ")
    print(msg2_enc)
    #Se decifra el mensaje hacia el otro usuario con la llave privada propia
    msg2_desc= operaciones.des2(bytes(msg2_enc), bytes(PK[0][1]))
    print("Mensaje Decifrado: ")
    print(msg2_desc.decode('utf-8'))
#############################################################
def enviar_llave_privada(ids, correo):
    llave = coneccion.consulta_llaves(ids)
    g = open('llave.pem', 'wb')
    g.write(llave[0][1])
    g.close()
    enviar.enviar_correo_archivo(correo, 'Llave Privada')
def enviar_llave_publica(ids, correo):
    llave = coneccion.consulta_llaves(ids)
    g = open('llave.pem', 'wb')
    g.write(llave[0][0])
    g.close()
    enviar.enviar_correo_archivo(correo, 'Llave Publica')
    
#enviar_llave_privada(10,'galigaribaldi0@gmail.com')