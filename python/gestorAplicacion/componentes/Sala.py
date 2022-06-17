from gestorAplicacion.componentes.Silla import Silla


class Sala:
    sillasVIP=5
    totalSillas=20
    totalSalas=10
    def __init__(self,tipo, sillas, pelicula, trabajadores, numero):
        
        
        
        self.tipo =tipo
        self.sillas = sillas
        self.pelicula = pelicula
        self.trabajadores = trabajadores
        self.numero = numero
        self.basura =0
        
        
        
        
        
        
        for i in range(0,Sala.totalSillas+1):
            if i>=1 and i<=int(Sala.totalSillas/2):
                silla=Silla(i, "Economica", "Parte baja")
                self.sillas.append(silla)
            elif i>int(Sala.totalSillas/2) and i<= int(Sala.totalSillas/2)+Sala.sillasVIP:
                silla=Silla(i, "VIP", "Central")
                self.sillas.append(silla)        
            elif i>int(Sala.totalSillas/2)+Sala.sillasVIP and i<=Sala.totalSillas:
                silla=Silla(i, "Economica", "Parte arriba")
                self.sillas.append(silla)
            
              
            

        
    def getTipo(self):
        return self.tipo
    
    def setTipo(self,tipo):
        self.tipo=tipo
        
        
        
    def getSillas(self):
        return self.sillas
    
    def setSillas(self,sillas):
        self.sillas=sillas
    
    
        
    def getPelicula(self):
        return self.pelicula
    
    def setPelicula(self,pelicula):
        self.pelicula=pelicula
        
    
    def getTrabajadores(self):
        return self.trabajadores
    
    def setTrabajadores(self,trabajadores):
        self.trabajadores=trabajadores
        
        
    def getNumero(self):
         return self.numero
     
    def setNumero(self,numero):
         self.numero=numero
        
        
     
    def getBasura(self):
         return self.basura
     
    def setBasura(self,basura):
         self.basura+=basura
         
    
    
        
        
    


   
        
