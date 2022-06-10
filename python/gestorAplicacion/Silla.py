

class Silla:
    def __init__(self,numero, tipo, ubicacion, cliente):
        
        self.numero =numero
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.clientes = cliente
        self.danada=False
        self.ocupada=False

        
    def getNumero(self):
        return self.numero
    
    def setNumero(self,numero):
        self.numero=numero
    
    def getTipo(self):
        return self.tipo
    
    def setTipo(self,tipo):
        self.tipo=tipo
        
    def getUbicacion(self):
        return self.ubicacion
    
    def setUbicacion(self,ubicacion):
        self.ubicacion=ubicacion
    
    def getClientes(self):
        return self.clientes
    
    def setClientes(self,clientes):
        self.clientes=clientes
    
    def getDanada(self):
        return self.danada
    
    def setDanada(self,danada):
        self.danada=danada
    
    def getOcupada(self):
        return self.ocupada
    
    def setOcupada(self,ocupada):
        self.ocupada=ocupada
        
    


   
        
