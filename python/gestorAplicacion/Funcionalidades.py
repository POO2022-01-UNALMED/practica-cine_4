import random
import time
from gestorAplicacion.Cliente import Cliente
from gestorAplicacion.Silla import Silla
from gestorAplicacion.Cartelera import Cartelera
from gestorAplicacion.Sala import Sala
from gestorAplicacion.Pelicula import Pelicula
from gestorAplicacion.Trabajador import Trabajador




class Funcionalidades:
    
    def inicializarSalas(self, cartelera):
        numeroSillas =12
        
        sillas=[]
        
        salas=[  ]
        trabajadores=[  ]
        cliente=Cliente(0,0,"NA", "NA", "NA",0)
        

        for i in range(0,numeroSillas):
            if i>0 and i<=80:
                silla=Silla(i, "Economica", "Lateral izquierdo", cliente)
                sillas.append(silla)
            
            elif i>80 and i<=160:
                silla=Silla(i, "VIP", "Central", cliente)
                sillas.append(silla)
                
            else:
                silla=Silla(i, "VIP", "Central", cliente)
                sillas.append(silla)
        
        
                
        sillasge=[]
        silla1=sillas.copy()   
        sillasge.append(silla1)
        silla2=sillas.copy()   
        sillasge.append(silla2)
        silla3=sillas.copy()   
        sillasge.append(silla3)
        silla4=sillas.copy()   
        sillasge.append(silla4)
        silla5=sillas.copy()   
        sillasge.append(silla5)
        silla6=sillas.copy()   
        sillasge.append(silla6)
        silla7=sillas.copy()   
        sillasge.append(silla7)
        silla8=sillas.copy()   
        sillasge.append(silla8)
        silla9=sillas.copy()   
        sillasge.append(silla9)
        silla10=sillas.copy()   
        sillasge.append(silla10)
       
        varNumeroSalas=10
                
        peliculas=cartelera.getPeliculas()
        
        for i in range(0,varNumeroSalas):
            if i>0 and i<5:
                sala=Sala("3D", sillasge[i], peliculas[i], trabajadores, i)
                salas.append(sala)
            else:
                sala=Sala("2D", sillasge[i], peliculas[i], trabajadores, i)
                salas.append(sala)
            
        return salas
    
    
#--------------------------------------------------------------------------------    
    
    def inicializarCartelera(self):
        peliculas=[]
        peli1 =  Pelicula("La caida de la casa blanca", "Roland Emmerich", 2013, 131, "Accion", "Estados unidos", "+14",20000)
        peli2 =  Pelicula("Ciudad de Dios", "Fernando Meirelles", 2002, 130, "Accion", "Brasil", "+18",20000)
        peli4 =  Pelicula("Salvando al soldado Ryan", "Steven Spielberg", 1998, 169, "Belico","Estados Unidos", "+16",20000)
        peli3 =  Pelicula("Terminator","James Cameron", 1984, 108, "Ciencia ficcion","Estados unidos", "+16",20000)
        peli5 =  Pelicula("Matrix", "Hermanas Wachowski", 2001, 136, "Ciencia ficcion", "Estados unidos", "+16",20000)
        peli6 =  Pelicula("Robots", "Chris Wedge", 2005, 84, "Animacion", "Estados unidos", "+4",15000)
        peli7 =  Pelicula("Enemigo a las puertas", "Jean-Jacques Annaud", 2001, 131, "Accion", "Estados unidos", "+16",15000)
        peli8 =  Pelicula("Interstellar  ", "Christopher Nolan", 2014, 169,"Ciencia ficcion","Estados undidos", "+13",15000)
        peli9 =  Pelicula("The Godfather", "Francis Ford Coppola", 1972, 177, "Gangsters", "Estados unidos", "+16",15000)
        peli10 = Pelicula("El gran hotel budapest", "Wes Anderson", 2014, 99, "Comedia", "Estados unidos", "+16",15000)
        
        peliculas.append(peli1)
        peliculas.append(peli2)
        peliculas.append(peli3)
        peliculas.append(peli4)
        peliculas.append(peli5)
        peliculas.append(peli6)
        peliculas.append(peli7)
        peliculas.append(peli8)
        peliculas.append(peli9)
        peliculas.append(peli10)
        
        
        cartelera=Cartelera(peliculas)
        return cartelera
    
#-----------------------------------------------------------------------------------
    
    def inicializarTrabajdores(self):
        trabajadores=[]
        trabajador1 =  Trabajador(100053321, 310402011, "Jaime Lozano", "M", 34, "Administrador")
        trabajador2 =  Trabajador(101012342, 310401233, "Kevin Duran", "M", 36, "Empleado de planta")
        trabajador3 =  Trabajador(105123423, 310501232, "Juan Alzate", "M", 24, "Empleado de planta")
        trabajador4 =  Trabajador(106421321, 305123214, "Maria Dos Santos", "F", 26, "Empleado de planta")
        trabajador5 = Trabajador(107421321, 305231234, "Anderson Castano", "M", 29, "Empleado de planta")
        trabajador6 =  Trabajador(101232134, 310452122,"Alejandro Sanchez" , "M", 42, "Empleado de servicio")
        trabajador7 =  Trabajador(106121321, 306232123, "Juan Castrillon", "M", 23, "Empleado de planta")
        trabajador8 =  Trabajador(102135231, 305324231, "Mariana Carillo", "F", 29, "Empleado de planta")
        trabajador9 =  Trabajador(10432521, 342151232, "Cindy Perez", "F", 24, "Empleado de planta")
        trabajador10 =  Trabajador(107421321, 305231234, "Juanita Gomez", "F", 33, "Empleado de planta")
        trabajador11 =  Trabajador(104324321, 310331234, "Manuelito Ortega", "M", 24, "Empleado de planta")
        trabajador12 =  Trabajador(107421321, 305231234, "Alex Castano", "M", 27, "Empleado de planta")
        trabajador13 =  Trabajador(107421321, 306233234, "Manuela Ortega", "M", 25, "Empleado de servicio")
        
        trabajadores.append(trabajador1)
        trabajadores.append(trabajador2)
        trabajadores.append(trabajador3)
        trabajadores.append(trabajador4)
        trabajadores.append(trabajador5)
        trabajadores.append(trabajador6)
        trabajadores.append(trabajador7)
        trabajadores.append(trabajador8)
        trabajadores.append(trabajador9)
        trabajadores.append(trabajador10)
        trabajadores.append(trabajador11)
        trabajadores.append(trabajador12)
        trabajadores.append(trabajador13)
        
        return trabajadores
    
   
    
    def peliculas(self, cartelera):
        a=[]
        
        pelicula=cartelera.getPeliculas()
        
        for i in range(len(pelicula)):
            b=str(i+1)+":  "+pelicula[i].toString()
            a.append(b)
        for i in a:
            return a
    
    
    
    
    
    def danarSilla(self,sala, salas):
 
        lista=list(range(1,240))
        n=random.choice(lista)
        sal=Sala(0, 0, 0, 0, 0)
      
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
            if i==n:
                sal.getSillas()[i].setDanada(True)
    
    
    
    
    
    
    
    def reportarSilla(self,silla,sala, salas):
           
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        
        for i in range(len(sal.getSillas())):
            if i==silla and sal.getNumero()==sala:
                if sal.getSillas()[i].getDanada()==False:
                    sal.getSillas()[i].setDanada(True)
                    return "La silla: "+str(silla)+" esta en mantenimiento"
               
            
            
            
            
            
    
    def PedirTrabajador(self, tipo, trabajadotres):
        tra = Trabajador(0, 0, "Na", "M", 0, "Na")
        for i in trabajadotres:
            if i.getCargo()=="Administrador" and tipo ==1:
                tra=i
                
            elif i.cargo != "Administrador" and tipo>1:
                tra=i
        
        return tra
    
    
    
    
    def arreglarSilla(self, sala,silla, trabajador, salas):
        
        lista=list(range(1,100))
        n=random.choice(lista)     
        for i in range(1,len(salas)):
            for j in range(1,len(salas[i].getSillas())):
                if silla==salas[i].getSillas()[j].getNumero():
                    if sala==i:
                        if trabajador.isOcupado()==False:
                            if salas[i].getSillas()[j].getDanada()==True:
                                trabajador.setOcupado(True)
                                
                                
                                if n>40:
                                    
                                    salas[i].getSillas()[j].setDanada(False)
                                    trabajador.setOcupado(False)
                                    
                                return trabajador.getNombre()+" esta reparando la silla  "+str(silla)
                            else:
                                return "La silla esta en buenas condiciones"
                       
        
            
            
                
            
        
                
            
    def vericarSilla(self,sala, salas):
      
        sal=Sala(0, 0, 0, 0, 0)
     
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
            if sal.getSillas()[i].getDanada()==True:
                b="La silla "+str(sal.getSillas()[i].getNumero())+" en la sala "+str(sala)+" esta en dañada"
                print(b)
        
        
        
        
        
        
        
    def devolucion(self, cliente,  salas):
        a=""
        encontrado=False
        for i in range(1,len(salas)):
            
            
            for j in range(len(salas[i].getSillas())):
                
               
                
                if cliente.getCedula() == salas[i].getSillas()[j].getClientes().getCedula():
                    a=self.pagoPelicula(i, salas)
                    encontrado=True
                    if salas[i].getSillas()[j].getDanada()==True:
                        salas[i].getSillas()[j].getClientes().setCosto(2000)
                                   
                    a= "se le hizo la devolucion a "+ salas[i].getSillas()[j].getClientes().getNombre()+" Total a pagar: "+str(salas[i].getSillas()[j].getClientes().getCosto()+a)
                elif encontrado==False:
                    a="No ha comprado"
        
        return a              
                           
                            
    
    
    
    def asiganarCliente(self, cliente, sala, silla,salas):
        lista=list(range(1,6))
        n=random.choice(lista)
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
            if sal.getSillas()[i].getNumero()==silla:
                sila=sal.getSillas()[silla]
                if sila.getOcupada()==False:
                    sila.setClientes(cliente)
                    sila.setOcupada(True)
                    sal.setBasura(n)
                    
                    return "La silla: "+str(sal.getSillas()[i].getNumero())+" esta asiganda Por el Cliente: "+ cliente.getNombre()
            
                elif sal.getSillas()[i].getOcupada()==True:
                    return "La silla " +str(sal.getSillas()[i].getNumero())+" esta ocupada"
    
    
    
    
    
    def buscarSillaLibre(self,sala, ubica, salas):
        c=0
        a=""
        l=[]
        
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        for i in range(0,240):
            if ubica==1:
                if i>0 and i<=80:
                    if sal.getSillas()[i].getOcupada()==False:
                        c+=1
                        a="Silla numero: "+str(sal.getSillas()[i].getNumero())+ " Esta libre"
                        l.append(a)
            elif ubica==2:
                if i>80 and i<=160:
                    if sal.getSillas()[i].getOcupada()==False:
                        c+=1
                        a="Silla numero: "+str(sal.getSillas()[i].getNumero())+ " Esta libre"
                        l.append(a)
                
                
            else:
                if i>160 and i<240:
                    if sal.getSillas()[i].getOcupada()==False:
                        c+=1
                        a="Silla numero: "+str(sal.getSillas()[i].getNumero())+ " Esta libre"
                        l.append(a)
        print(" \nSillas libre: "+ str(c)+"\nlista de sillas libres: \n")                 
        for i in l:
            print(i)
    
    
    
    
    
    def nivelBasura(self, sala, salas):
        
        for i in range(1,len(salas)):
                if sala==i:
                    return salas[i].getBasura()
                
                
    def pagoPelicula(self, sala,salas):
        
        for i in range(1,len(salas)):
                if sala==i:
                    return salas[i].getPelicula().getPrecio()

    
    
    def buscarSala(self, sala,salas):
        for i in range(len(salas)):
            if sala==1:
                return salas[i]
        
    
    
    def Combos(self,tipo,cliente,sala,salas):
        
        if tipo==1:
            cliente.setCosto(5000)
            sa=self.buscarSala(sala, salas)
            sa.setBasura(10)
        elif tipo==2:
            cliente.setCosto(8000)
            sa=self.buscarSala(sala, salas)
            sa.setBasura(15)
        elif tipo==3:
            cliente.setCosto(15000)
            sa=self.buscarSala(sala, salas)
            sa.setBasura(19)
        elif tipo==4:
            cliente.setCosto(20000)
            sa=self.buscarSala(sala, salas)
            sa.setBasura(25)
            
    
    def limpiarBasura(self, trabajador, sala, salas):
        
        for i in range(len(salas)):
            if sala==i:
                if salas[i].getBasura()>0:
                    trabajador.setOcupado(True)
                    self.countdown(6)
                    trabajador.setOcupado(False)
                    print("Se limpio la sala " +str(salas[i].getNumero())+" por "+ trabajador.getNombre())
                
                elif salas[i].getBasura()==0:
                    print("La sala esta limpia")
                    
        
            
    def countdown(self,num_of_secs):
        while num_of_secs:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(min_sec_format, end='/r')
            time.sleep(1)
            num_of_secs -= 1
            
        print('Countdown finished.')
    
    
            
        
    
    
    
            
    
     
            
            
            
        
        
    
    
                
                
            
    
                    
    
          
          
                
                
                
f=Funcionalidades()              
            
                        
trabajadores=f.inicializarTrabajdores()                



cliente=Cliente(10, 0, "nombre", "sexo", "edad", 0)
cliente1=Cliente(11, 0, "ke", "sexo", "edad", 0)
c=f.inicializarCartelera()

salas=f.inicializarSalas(c)
traba=f.PedirTrabajador(1, trabajadores)
print(f.limpiarBasura(traba, 1, salas))


"""        
sillas=[]
silla1=Silla(1, "Economica", "Lateral izquierdo", cliente)
sillas.append(silla1)
silla2=Silla(2, "VIP", "Central", cliente)
sillas.append(silla2)
silla3=Silla(3, "VIP", "Central", cliente)
sillas.append(silla3)
------------------------------------------------
 print(f.reportarSilla(2, 1, salas))
 print(f.reportarSilla(3, 1, salas))
 print(f.vericarSilla(1, salas))
 print(f.asiganarCliente(cliente, 2, 2, salas))
 print(f.devolucion(cliente, salas))
----------------------------------------------------------        
peli1 =  Pelicula("La caida de la casa blanca", "Roland Emmerich", 2013, 131, "Accion", "Estados unidos", "+14",20000)
peli2 =  Pelicula("Ciudad de Dios", "Fernando Meirelles", 2002, 130, "Accion", "Brasil", "+18",20000)
sala1=Sala("3D", sillas, peli1, trabajadores, 1)
sala2=Sala("2D", sillas, peli1, trabajadores, 2)
s=[]
s.append(sala1)
s.append(sala2)

print(f.asiganarCliente(cliente, 1, 1, s))

for i in range(len(s)):
    for j in range(len(s[i].getSillas())):
        print(s[i].getSillas()[j].getOcupada(),s[i].getNumero())
        if i==1:
            print()
"""
    

                
        
                
        

                
    
        
    


   
        
