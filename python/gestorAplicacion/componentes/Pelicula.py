
class Pelicula:
    peliculas=[]
    def __init__(self,nombre, director,ano, duracion,genero,pais,calificacion,precio):
        self.nombre=nombre
        self.director=director
        self.ano=ano
        self.duracion=duracion
        self.genero=genero
        self.pais=pais
        self.calificacion=calificacion
        self.precio=precio
        
    def getNombre(self):
        return self.nombre
    
    
    def setNombre(self,nombre):
        self.nombre=nombre
        
    
    def getDirector(self):
        return self.director
         
    def setDirector(self,director):
        self.director=director
        
        
        
    def getAno(self):
        return self.ano
    
    def setAno(self,ano):
        self.ano=ano
        
        
        
    def getDuracion(self):
        return self.duracion
    
    def setDuracion(self,duracion):
        self.duracion=duracion
        
        
        
    def getPais(self):
        return self.pais
    
    def setPais(self,pais):
        self.pais=pais
        
        
        
    def getCalificacion(self):
        return self.calificacion
    
    def setCalificacion(self,calificacion):
        self.calificacion=calificacion
        
        
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,precio):
        self.precio=precio
        

    def toString(self):
        return self.nombre
    

    @staticmethod
    def getPeliculas():
         return Pelicula.peliculas

    @staticmethod
    def setPeliculas(pelicula):
        Pelicula.peliculas=pelicula

        
    