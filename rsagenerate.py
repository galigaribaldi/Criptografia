from Cryptodome.PublicKey import RSA
"""
llave = RSA.generate(2048) #1025, 2048 

####llave privada
f = open('llaveprivada.pem', 'wb')
f.write(llave.exportKey('PEM'))
f.close()

### Llave publica
g = open('llavepublica.pem', 'wb')
g.write(llave.publickey().exportKey('PEM'))
g.close()
"""
class NewKey():
    llave = ""
    def __init__(self):
        self.llave = RSA.generate(2048) #1025, 2048 
        
    def generatePrivateKey(self):
        #f = open('llaveprivada.pem', 'wb')
        #f.write(self.llave.exportKey('PEM'))
        return self.llave.exportKey('PEM')
        #f.close()
        
    def generatePublicKey(self):
        #g = open('llavepublica2.pem', 'wb')
        #g.write(self.llave.publickey().exportKey('PEM'))
        #g.close()
        return self.llave.publickey().exportKey('PEM')
    
    def generatePrivateKey_txt(self):
        f = open('llave.pem', 'wb')
        f.write(self.llave.exportKey('PEM'))
        f.close()
        
    def generatePublicKey_txt(self):
        g = open('llave.pem', 'wb')
        g.write(self.llave.publickey().exportKey('PEM'))
        g.close()        

#generatePublicKey()
#generatePrivateKey()
#nueva_Llave = NewKey()
#nueva_Llave.generatePrivateKey()
#nueva_Llave.generatePublicKey()