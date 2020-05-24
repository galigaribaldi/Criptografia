from Cryptodome.Cipher import AES
from Cryptodome import Random

def encriptar(mensaje):
    mensaje = mensaje
    key = b'llaveSecreta1212'#16 bits
    IV= b'0123456789abcdef'
    mode = AES.MODE_CFB
    cifrado = AES.new(key, mode, IV=IV)
    msg = cifrado.encrypt(mensaje)
    f = open('textoencriptado.txt', 'wb')
    f.write(msg)
    f.close

encriptar(b"atacar al anochecer")

f = open('textoencriptado.txt', 'rb')
mensaje = f.read()

def desencriptar(mensaje):
    mensaje = mensaje
    key = b'llaveSecreta1212'#16 bits
    IV= b'0123456789abcdef'
    mode = AES.MODE_CFB
    cifrado = AES.new(key, mode, IV=IV)
    msg = cifrado.decrypt(mensaje)
    print(msg)
desencriptar(mensaje)