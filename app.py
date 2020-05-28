"""

@author: Cabrera Garibaldi Hernan Galileo
@description: Programa principal que corre la aplicacion WEB

"""

#################Modulos de Flask#######################
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask import request, flash
from flask import redirect, url_for, session
import json
import os
#######################################################

###################Modulos Propios###################
##Operacion Web, con la BD
import models as coneccion
#Generar Llaves Publica y privada
import rsagenerate as generador
##Descifrar y Cifrar
import rsacrp as operaciones
#####################################################
###Automatizador Bakcground
import redis
import automatizar as au
from rq import Queue
from urllib.parse import urlparse
url=urlparse(os.environ.get('REDISCLOUD_URL'))
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)
##
#r = redis.Redis()
q = Queue(connection=r)



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        d = coneccion.consulta_usuario_correo(correo)
        if d:
            PK = coneccion.consulta_llaves(d[0][0])
            c = operaciones.des2(bytes(d[0][4]), bytes(PK[0][1]))
            if bytes(password, 'utf8') == c:
                datos = coneccion.consulta_usuario()
                return render_template("salaChats.html", datos=datos)
            else:
                return "Password incorrecto"
        else:
            return "No tenemos cuenta de tu correo"
            #flash("Datos incorrectos")
            #return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/crearCuenta', methods = ['GET', 'POST'])
def crearCuenta():
    if request.method =='POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        password = request.form['password']
        #######Se crea el nuevo usuario
        coneccion.nuevo_usuario(nombre, apellidos, correo)
        #######Se generan las llaves publicas y privadas para cada usuario
        g = generador.NewKey()
        publica = g.generatePublicKey()
        privada = g.generatePrivateKey()
        ########## Se obtienen los datos del usuario creado
        d = coneccion.consulta_usuario_correo(correo)
        coneccion.insertaClaves(d[0][0], publica, privada)
        ####Consulta de la llave privada
        PK = coneccion.consulta_llaves(d[0][0])
        ###Actualizacion de el password encriptado
        passwordEncriptado = operaciones.enc2(bytes(password, 'utf8'),bytes(PK[0][1]) )
        coneccion.actualizar_password(d[0][0], passwordEncriptado)
        return render_template("index.html")
    else:
        return render_template("crearCuenta.html")

@app.route("/saladeChats/<id_usuario>")
def sala_chats(id_usuario):
    datos = coneccion.consulta_usuario_id(id_usuario)
    return render_template("chat.html", datos=datos,data=map(json.dumps, datos))

@app.route("/enviarllave/<id_usuario>/<correo>/<opcion>")
def enviarllave(id_usuario, correo, opcion):
    ###Llave privada
    if opcion =="1":
        job = q.enqueue(au.enviar_llave_privada, id_usuario, correo)
        flash("El correo fue enviado")
        datos = coneccion.consulta_usuario_id(id_usuario)
        return render_template("chat.html", datos=datos,data=map(json.dumps, datos))
    ##llave publica
    if opcion =="2":
        job = q.enqueue(au.enviar_llave_privada, id_usuario, correo)
        flash("El correo fue enviado")
        datos = coneccion.consulta_usuario_id(id_usuario)
        return render_template("chat.html", datos=datos,data=map(json.dumps, datos))
    
@socketio.on('message')
def handleMessage(msg):
    tam = len(msg)
    msg2 = msg[0:tam-2] ##Mensaje que se recibe
    id2 = int(msg[tam-2:tam]) ##Id del Usuario
    ###Se consulta la llave para cada usuario
    #PK = coneccion.consulta_llaves(id2)
    """
    ##Se cifra el mensaje
    msg2_enc = operaciones.enc2(bytes(msg2, 'utf8'), bytes(PK[0][0]))
    print("Mensaje Cifrado del usuar¡o con id: "+ id+" ")
    print(msg2_enc)
    #Se decifra el mensaje hacia el otro usuario con la llave privada propia
    msg2_desc= operaciones.des2(bytes(msg2_enc), bytes(PK[0][1]))
    #print(msg2_desc.decode('utf-8'))"""
    #print((id2))
    #print(PK)
    ##print(type(msg2))
    send(msg2, broadcast= True)
    job = q.enqueue(au.mensaje_cifrado, id2, msg2)

if __name__ == "__main__":
    socketio.run(app, debug=True)