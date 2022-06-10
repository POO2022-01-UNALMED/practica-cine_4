from gestorAplicacion.Pelicula import Pelicula


class Cartelera:
    def __init__(self,peliculas):
        self.peliculas=peliculas
        
        
    def getPeliculas(self):
        return self.peliculas
    
    def cambiarPelicula(self,nombre,nuevaPelicula):
        
        
        peliculas=self.getPeliculas()
        
        for i in range(len(peliculas)):
            if (peliculas[i]==nombre):
                peliculas.remove(peliculas[i])
                peliculas.append(nuevaPelicula)
                
        return(peliculas)
    
    
    def imprimirCartelera(self):
        pelis=[]
        l=[]
        
        
        for i in self.getPeliculas():
            a="Nombre: "+ i.nombre+"\nDirector: "+i.director+"\nAno: "+ str(i.ano)+"\nDuracion: "+str(i.duracion)+"\nGenero: "+i.genero+"\nPais: "+str(i.precio)+"\n____________________________________________________________________"
           
            l.append(a)
        
        for i in l:
            print(i)
        
        

       
        


        
        

            
                


  
 
