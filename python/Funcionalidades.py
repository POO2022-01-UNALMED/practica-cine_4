import random
import time
import pickle
from gestorAplicacion.componentes.Cliente import Cliente
from gestorAplicacion.componentes.Cartelera import Cartelera
from gestorAplicacion.componentes.Sala import Sala
from gestorAplicacion.componentes.Pelicula import Pelicula
from gestorAplicacion.componentes.Trabajador import Trabajador






class Funcionalidades(object):

    # DESERIALIZACION DE DATOS
    #picklefile = open("./baseDeDatos/clienten","rb")
    #picklefile2=open("./baseDeDatos/Peliculas", "rb")
    #picklefile3=open("./baseDeDatos/Trabajadores", "rb")

    #Cliente.setclientes(pickle.load(picklefile))
    #Pelicula.setPeliculas(pickle.load(picklefile2))
    #Trabajador.setTabajadores(pickle.load(picklefile3))
    #picklefile.close()
    #picklefile2.close()
    
    
    
#--------------------------------------------------------------------------------      
    #Con esta funcion creamos las salas
    @staticmethod
    def inicializarSalas():
        cartelera=Funcionalidades.inicializarCartelera()
        varNumeroSalas=Sala.totalSalas
        salas=[  ]
        peliculas=cartelera.getPeliculas()
        
        for i in range(0,varNumeroSalas):
            if i>0 and i<5:
                sala=Sala("3D", [], peliculas[i], Trabajador.getTrabajadores(), i)
                salas.append(sala)
            else:
                sala=Sala("2D", [], peliculas[i], Trabajador.getTrabajadores(), i)
                salas.append(sala)
        return salas
        
     
        
     
        
     
        
     
    
#--------------------------------------------------------------------------------    
    #creamos las peliculas que van a estar disponible
    @staticmethod
    def inicializarCartelera():
           
        cartelera=Cartelera(Pelicula.getPeliculas() )
        return cartelera

    
   
    
   
#-----------------------------------------------------------------------------------
    #Este metodo nos mostrara por pantalla la lista de peliculas 
    @staticmethod    
   
    def peliculas(cartelera, tipo):
        a=[]
        
        pelicula=cartelera.getPeliculas()
        
        if tipo==1:
            for i in range(0,len(pelicula)-5):
                b=str(i+1)+":  "+pelicula[i].toString()
                a.append(b)
        else:
            for i in range(5,len(pelicula)):
                b=str(i)+":  "+pelicula[i].toString()
                a.append(b)
        for i in a:
            return a
    
    
    
 #-----------------------------------------------------------------------------------
     #Este metodo se encargara de danar una silla aletoriamente
     
    @staticmethod   
    
    def danarSilla(sala, salas):
 
        lista=list(range(1,Sala.totalSillas))
        n=random.choice(lista)
        sal=Sala(0, [], 0, 0, 0)
        
      
        for i in range(1,len(salas)):
            
            if sala==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
            
            if i==n:
                
                sal.getSillas()[i].setDanada(True)
    
    
    
#-----------------------------------------------------------------------------------
    #Con este metodo reportaremos una silla que este dañada
    
    @staticmethod        
    def reportarSilla(silla,sala, salas):
           
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        
        for i in range(len(sal.getSillas())):
            if i==silla and sal.getNumero()==sala:
                if sal.getSillas()[i].getDanada()==False:
                    sal.getSillas()[i].setDanada(True)
                    return "La silla: "+str(silla)+" esta en mantenimiento"
               
            
            
            
#-----------------------------------------------------------------------------------
    #Con este metodo nos entregara un trabajador depediendo el cargo
    
    @staticmethod       
  
    def PedirTrabajador( tipo):
        tra = Trabajador(0, 0, "Na", "M", 0, "Na")
        for i in Trabajador.trabajadores:
            if i.getCargo()=="Administrador" and tipo ==1:
                tra=i
                
            elif i.cargo != "Administrador" and tipo>1:
                tra=i
        
        return tra
    
    
#-----------------------------------------------------------------------------------
    #Con esta funcion arreglaremos una silla(le cambiaremos su atributo)
    
    @staticmethod    
    
    def arreglarSilla( sala,silla, trabajador, salas):
        
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
                       
        
            
            
                
            
        
#-----------------------------------------------------------------------------------
    #con este funcion veremos el estado de la silla(si esta dañada o no)
    
    @staticmethod                    
            
    def vericarSilla(sala, salas):
        b=None
        sal=Sala(0, [], 0, 0, 0)
     
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
            if sal.getSillas()[i].getDanada()==True:
                b="La silla "+str(sal.getSillas()[i].getNumero())+" en la sala "+str(sala)+" esta en dañada"
                print(b)
            
        if b==None:
            return "Las sillas estan bien"
        
    
   
        
        
        
        
#-----------------------------------------------------------------------------------
    #con este funcion le haremos la devolucion a un cliente en cuestion
    
    @staticmethod            
        
    def devolucion(self, cliente,  salas):
        a=""
        encontrado=False
        for i in range(1,len(salas)):
            
            
            for j in range(len(salas[i].getSillas())):
                
               
                
                if cliente.getCedula() == salas[i].getSillas()[j].getClientes().getCedula():
                    a=Funcionalidades.pagoPelicula(i, salas)
                    encontrado=True
                    if salas[i].getSillas()[j].getDanada()==True:
                        salas[i].getSillas()[j].getClientes().setCosto(2000)
                                   
                    a= "se le hizo la devolucion a "+ salas[i].getSillas()[j].getClientes().getNombre()+" Total a pagar: "+str(salas[i].getSillas()[j].getClientes().getCosto()+a)
                elif encontrado==False:
                    a="No ha comprado"
        
        return a              
                           
#-----------------------------------------------------------------------------------
    #con este funcion buscaremos una silla que este disponible, atre vez de una determinada cuestion
    
    @staticmethod    
    
    def buscarSilla( silla,  salas):
        
        for i in range(1,len(salas)):
            
            
            for j in range(len(salas[i].getSillas())):
                if salas[i].getSillas()[j].getNumero()==silla:
                    return salas[i].getSillas()[j]
                            
    
    
#-----------------------------------------------------------------------------------
    #Con esta funcion le asignaremos a la silla un cliente
    
    @staticmethod    
    
    def asiganarCliente(cliente, sala, silla,salas):
        lista=list(range(1,6))
        n=random.choice(lista)
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
           
            if sal.getSillas()[i].getNumero()==silla.getNumero():
                sila=sal.getSillas()[silla.getNumero()]
                if sila.getOcupada()==False:
                    sila.setClientes(cliente)
                    sila.setOcupada(True)
                    sal.setBasura(n)
                    Cliente.clientes.append(cliente)
                   
                    
            
                
            
    
    
    
    
#-----------------------------------------------------------------------------------
    #con esta funcion buscaremos una silla mediante la ubicacion de la silla(central, arriba o abajo)
    
    @staticmethod        
    def buscarSillaLibre(sala, ubica, salas):
        c=0
        a=""
        l=[]
        
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        for i in range(0,Sala.totalSillas):
            if ubica==1:
                if i>=1 and i<=int(Sala.totalSillas/2):
                    if sal.getSillas()[i].getOcupada()==False:
                        c+=1
                        a="Silla numero: "+str(sal.getSillas()[i].getNumero())
                        l.append(a)
            elif ubica==2:
                if i>int(Sala.totalSillas/2) and i<= int(Sala.totalSillas/2)+Sala.sillasVIP:
                    if sal.getSillas()[i].getOcupada()==False:
                        c+=1
                        a="Silla numero: "+str(sal.getSillas()[i].getNumero())
                        l.append(a)
                
                
            else:
                if i>int(Sala.totalSillas/2)+Sala.sillasVIP and i<=Sala.totalSillas:
                    if sal.getSillas()[i].getOcupada()==False:
                        c+=1
                        a="Silla numero: "+str(sal.getSillas()[i].getNumero())
                        l.append(a)
        
        return l
    
    
    
#-----------------------------------------------------------------------------------
    #Esta funcion nos dara el nivel de basura de una sala determinada
    
    @staticmethod        
    
    def nivelBasura( sala, salas):
        
        for i in range(1,len(salas)):
                if sala==i:
                    return salas[i].getBasura()
                
                
#-----------------------------------------------------------------------------------                
    #nos dara el pago de la pelicula
    @staticmethod                
    def pagoPelicula(self, sala,salas):
        
        for i in range(1,len(salas)):
                if sala==i:
                    return salas[i].getPelicula().getPrecio()

    
#-----------------------------------------------------------------------------------
    #Con esta funcion buscaremos una determinada sala
    
    @staticmethod        
    def buscarSala(sala,salas):
        for i in range(len(salas)):
            if sala==1:
                return salas[i]
        
    
#-----------------------------------------------------------------------------------
    #Este metodo nos dara los combos(comida) que tiene disponible la sala
    
    @staticmethod        
    def Combos(tipo,cliente,sala,salas):
        
        if tipo==1:
            cliente.setCosto(5000)
            sa=Funcionalidades.buscarSala(sala, salas)
            sa.setBasura(10)
        elif tipo==2:
            cliente.setCosto(8000)
            sa=Funcionalidades.buscarSala(sala, salas)
            sa.setBasura(15)
        elif tipo==3:
            cliente.setCosto(15000)
            sa=Funcionalidades.buscarSala(sala, salas)
            sa.setBasura(19)
        elif tipo==4:
            cliente.setCosto(20000)
            sa=Funcionalidades.buscarSala(sala, salas)
            sa.setBasura(25)
            
#-----------------------------------------------------------------------------------
    #Con esta funcion limpiaremos la sala mediante un trabajador
    
    @staticmethod        
    def limpiarBasura( trabajador, sala, salas):
        
        for i in range(len(salas)):
            if sala==i:
                if salas[i].getBasura()>0:
                    trabajador.setOcupado(True)
                    Funcionalidades.countdown(6)
                    trabajador.setOcupado(False)
                    print("Se limpio la sala " +str(salas[i].getNumero())+" por "+ trabajador.getNombre())
                
                elif salas[i].getBasura()==0:
                    print("La sala esta limpia")
                    
        
#-----------------------------------------------------------------------------------
    #Este es un cronometro
    
    @staticmethod                
    def countdown(num_of_secs):
      
        while num_of_secs:
           
            m, s = divmod(num_of_secs, 60)
            
            print(" Se esta limpiando")
            time.sleep(1)
            num_of_secs -= 1
            
        print('Ya se limpio')
    
    
#-----------------------------------------------------------------------------------
    #Con esta funcion buscaremos a un cliente en la lista de clientes(que ya hayan comprado)
    
    @staticmethod        
    def buscarCliente(cliente):
        a=""
        for i in range(len(Cliente.clientes)):
            
            if str(Cliente.clientes[i].getNombre())==cliente.getNombre() and str(Cliente.clientes[i].getCedula())==cliente.cedula:
                a=Cliente.clientes[i]
            elif Cliente.clientes[i].getNombre()!=cliente.getNombre() and Cliente.clientes[i].getCedula()!=cliente.cedula:
                a=None
        return a
    


    
    
    
    
    
        
    
    
    @staticmethod
    def salirDelSistema():
        picklefile = open("./baseDeDatos/clienten", "wb")
        picklefile2=open("./baseDeDatos/Peliculas", "wb")
        picklefile3=open("./baseDeDatos/Trabajadores", "wb")
        
        pickle.dump(Cliente.clientes, picklefile)
        pickle.dump(Pelicula.peliculas, picklefile2)
        pickle.dump(Trabajador.trabajadores, picklefile3)
        picklefile.close()
        quit()    
            
    
     
            
            

cliente=Cliente(1,1,1,1,1)          

    
    
                
                
            
    
                    
    
          
          
                













                
        

                
    
        
    


   
        
