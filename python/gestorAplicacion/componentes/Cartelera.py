from gestorAplicacion.componentes.Pelicula import Pelicula


class Cartelera:
    def __init__(self,peliculas):
        self.peliculas=peliculas
        
        
    def getPeliculas(self):
        return self.peliculas
    
    
    
    
    def imprimirCartelera(self):
        pelis=[]
        l=[]
        
        
        for i in self.getPeliculas():
            a="Nombre: "+ i.nombre+"\nDirector: "+i.director+"\nAno: "+ str(i.ano)+"\nDuracion: "+str(i.duracion)+"\nGenero: "+i.genero+"\nPais: "+str(i.precio)+"\n____________________________________________________________________"
           
            l.append(a)
        
        for i in l:
            return(i)
        
        

       
        


        
        

            
                


  
 
