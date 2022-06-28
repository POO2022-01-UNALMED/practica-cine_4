import random
import time
import pickle
from gestorAplicacion.componentes.Cliente import Cliente
from gestorAplicacion.componentes.Cartelera import Cartelera
from gestorAplicacion.componentes.Sala import Sala
from gestorAplicacion.componentes.Pelicula import Pelicula
from gestorAplicacion.componentes.Silla import Silla
from gestorAplicacion.componentes.Trabajador import Trabajador
from tkinter import messagebox as MessageBox 
from excepciones.ExceptionFormatos import ExcepcionStringNumero
from excepciones.ExceptionFormatos import ExcepcionEnteroString




class Funcionalidades(object):

    # DESERIALIZACION DE DATOS
    
    picklefile = open("./baseDeDatos/clientes","rb")
    picklefile2=open("./baseDeDatos/Peliculas", "rb")
    picklefile3=open("./baseDeDatos/trabajadores", "rb")
    picklefile4=open("./baseDeDatos/salas", "rb")

    Cliente.setclientes(pickle.load(picklefile))
    Pelicula.setPeliculas(pickle.load(picklefile2))
    Trabajador.setTabajadores(pickle.load(picklefile3))
    Sala.setSalas(pickle.load(picklefile4))
    picklefile.close()
    picklefile2.close()
    picklefile3.close()
    picklefile4.close()
    
    
     
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
        entero=sala.isnumeric()
        entero2=silla.isnumeric()

        if entero==False or entero2==False:
            try:
                raise ExcepcionStringNumero(sala)
            except ExcepcionStringNumero as e:
                MessageBox.showerror(title="Error",message=e)
                return
        else:
            sala=int(sala)
            silla=int(silla)
        a=None
        for i in range(1,len(salas)):
            if sala==i:
                sal=salas[i]
        
        
        for i in range(len(sal.getSillas())):
            if i==silla and sal.getNumero()==sala:
                if sal.getSillas()[i].getDanada()==False:
                    sal.getSillas()[i].setDanada(True)
                    a=sal.getSillas()[i]
        return a            
        
               
            
            
            
#-----------------------------------------------------------------------------------
    #Con este metodo nos entregara un trabajador depediendo el cargo
    
    @staticmethod       
  
    def PedirTrabajador(tipo):
        tra = None
        for i in Trabajador.getTrabajadores():
            if i.getCargo()=="Administrador" and tipo ==1:
                tra=i
                
            elif i.cargo != "Administrador" and tipo>1:
                tra=i
        
        return tra
    
    
#-----------------------------------------------------------------------------------
    #Con esta funcion arreglaremos una silla(le cambiaremos su atributo)
    
    @staticmethod    
    
    def arreglarSilla( sala,silla, trabajador, salas):
        entero=sala.isnumeric()

        if entero==False:
            try:
                raise ExcepcionStringNumero(sala)
            except ExcepcionStringNumero as e:
                MessageBox.showerror(title="Error",message=e)
                return
        else:
            sala=int(sala)
        
        a=None
        
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
                                    
                                a=trabajador.getNombre()+" esta reparando la silla  "+str(silla)
                            else:
                                a="La silla esta en buenas condiciones"
        return a
                       
        
            
            
                
            
        
#-----------------------------------------------------------------------------------
    #con este funcion veremos el estado de la silla(si esta dañada o no)
    
    @staticmethod                    
            
    def vericarSilla(sala,salas):
        entero=sala.isnumeric()

        if entero==False:
            try:
                raise ExcepcionStringNumero(sala)
            except ExcepcionStringNumero as e:
                MessageBox.showerror(title="Error",message=e)
                return
        else:
            sala=int(sala)
        b=None
        sal=Sala(0, [], 0, 0, 0)
     
        for i in range(1,len(salas)):
            if int(sala)==i:
                sal=salas[i]
        
        for i in range(len(sal.getSillas())):
            if sal.getSillas()[i].getDanada()==True:
                b="La silla "+str(sal.getSillas()[i].getNumero())+" en la sala "+str(sala)+" esta en dañada"
                
            
        if b==None:
            b="Las sillas estan bien"
        
        return b
   
        
        
        
        
#-----------------------------------------------------------------------------------
    #con este funcion le haremos la devolucion a un cliente en cuestion
    
    @staticmethod            
        
    def devolucion(cliente,salas):
        
        a=""
        encontrado=False
        for i in range(1,len(salas)):
            
            
            for j in range(len(salas[i].getSillas())):
                
               
                
                if cliente.getCedula() == salas[i].getSillas()[j].getClientes().getCedula():
                    Funcionalidades.pagoPelicula(i, salas)
                    encontrado=True
                    if salas[i].getSillas()[j].getDanada()==True:
                        salas[i].getSillas()[j].getClientes().setCosto(2000)
                        salas[i].getSillas()[j].setOcupada(False)           
                    a= "se le hizo la devolucion a "+ salas[i].getSillas()[j].getClientes().getNombre()+" Total a pagar: "+str(salas[i].getSillas()[j].getClientes().getCosto()+a)
                elif encontrado==False:
                    a=None
        
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
        entero=sala.isnumeric()

        if entero==False:
            try:
                raise ExcepcionStringNumero(sala)
            except ExcepcionStringNumero as e:
                MessageBox.showerror(title="Error",message=e)
                return
        else:
            sala=int(sala)
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
                    Funcionalidades.pagoPelicula(sal.getNumero(),salas)
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
    def pagoPelicula( sala,salas):
        
        for i in range(1,len(salas)):
                if sala==i:
                    return salas[i].getPelicula().getPrecio()

    
#-----------------------------------------------------------------------------------
    #Con esta funcion buscaremos una determinada sala
    
    @staticmethod        
    def buscarSala(sala,salas):
        a=None
        for i in range(len(salas)):
            if int(sala)==int(1):
                a= salas[i]
        return a
    
#-----------------------------------------------------------------------------------
    #Este metodo nos dara los combos(comida) que tiene disponible la sala
    
    @staticmethod        
    def Combos(tipo,cliente,sala):
        
        
        
        if tipo==1:
            cliente.setCosto(25000)
            
            sala.setBasura(10)
        elif tipo==2:
            cliente.setCosto(40000)
          
            sala.setBasura(15)
        elif tipo==3:
            cliente.setCosto(50000)           
            
            sala.setBasura(19)

        return cliente
        
        
            
#-----------------------------------------------------------------------------------
    #Con esta funcion limpiaremos la sala mediante un trabajador
    
    @staticmethod        
    def limpiarBasura( trabajador, sala,salas):
        a=""
        
        for i in range(len(salas)):
            if sala==str(i):
                if salas[i].getBasura()>=10:
                    trabajador.setOcupado(True)
                    Funcionalidades.countdown(6)
                    trabajador.setOcupado(False)
                    a="Se limpio la sala " +str(salas[i].getNumero())+" por "+ trabajador.getNombre()
                elif salas[i].getBasura()<10 and salas[i].getBasura() >0:
                    trabajador.setOcupado(True)
                    Funcionalidades.countdown(3)
                    trabajador.setOcupado(False)
                    a="Se limpio la sala " +str(salas[i].getNumero())+" por "+ trabajador.getNombre()
                elif salas[i].getBasura()==0:
                    a="La sala esta limpia"
        return a
                    
        
#-----------------------------------------------------------------------------------
    #Este es un cronometro
    
    @staticmethod                
    def countdown(num_of_secs):
        descripcion = MessageBox.showinfo(title = "Mensaje", message = f"Espere {num_of_secs} segundos mientras se limpia la sala",
        detail = "la sala se esta limpiando")
        while num_of_secs:
           
            m, s = divmod(num_of_secs, 60)
            
            
            time.sleep(1)
            num_of_secs -= 1
            
        descripcion = MessageBox.showinfo(title = "Mensaje", message = "Enhorabuena",
        detail = "la sala esta limpia")
    
    
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
    

#-----------------------------------------------------------------------------------
    #Con esta funcion buscaremos a un cliente en la lista de clientes(que ya hayan comprado)
    
    @staticmethod        
    def buscarClien(cedula):
        a=""
        for i in range(len(Cliente.clientes)):
            
            if str(Cliente.clientes[i].getCedula())==str(cedula):
                
                a=Cliente.clientes[i]
            elif a=="" and Cliente.clientes[i].getCedula()!=str(cedula):
                a=None
        return a

#-----------------------------------------------------------------------------------
    #Con esta funcion se cambiara la cartelera
    
    @staticmethod
    def cambiarPelicula(nombre,nuevaPelicula):
        entero=nombre.isnumeric()

        if entero==True:
            try:
                raise ExcepcionEnteroString(nombre)
            except ExcepcionEnteroString as e:
                MessageBox.showerror(title="Error",message=e)
                return                        
        
        cartelera=Funcionalidades.inicializarCartelera()
        for i, valor in enumerate(cartelera.getPeliculas()):
            if valor.getNombre()==nombre:
                cartelera.getPeliculas()[i]=nuevaPelicula
        
        return f"Se cambio la pelicula {nombre} por {nuevaPelicula.getNombre()} "
                
        

    
#---------------------------------------------------------------------------------------------------------------------
    #con esta funcion mostramos en una tabla las peliculas disponibles
    @staticmethod 
    def verCartelera(label):
        cartelera=Funcionalidades.inicializarCartelera()
        label["text"]+="\n-------------------------------------------------------------------------------------------------------------------------------------------------------"
        label["text"]+="\n"+"{0:>5} {1:>22} {2:>48} {3:>40}".format("Precio", "Ano", "Pais", "Nombre"+"\n")
        label["text"]+="----------------------------------------------------------------------------------------------------------------------------------------------------------"

        i = 0
        while i < len(cartelera.getPeliculas()):
            label["text"]+="\n"+"{0:>5} {1:>22} {2:>38} {3:>40}".format(cartelera.getPeliculas()[i].getPrecio(), cartelera.getPeliculas()[i].getAno(),cartelera.getPeliculas()[i].getPais(),cartelera.getPeliculas()[i].getNombre())
            i += 1
        label["text"]+="\n-------------------------------------------------------------------------------------------------------------------------------------------------------"
        label["text"]+="\n"

#---------------------------------------------------------------------------------------------------------------------
    @staticmethod
    #con esta funcion mostramos en una tabla de los trabajadores 
    def verTrabajadores(label):
        trabajadres=Trabajador.getTrabajadores()
        label["text"]+="\n-----------------------------------------------------------------------------------------------------------------------"
        label["text"]+="\n"+"{0:>5} {1:>13} {2:>16} {3:>20}".format("Cedula", "Cargo", "Ocupado", "Nombre"+"\n")
        label["text"]+="-------------------------------------------------------------------------------------------------------------------------"

        i = 0
        while i < len( trabajadres):
            label["text"]+="\n"+"{0:>5} {1:>25} {2:>26} {3:>30}".format( trabajadres[i].getCedula(),  trabajadres[i].getCargo(), trabajadres[i].isOcupado(), trabajadres[i].getNombre())
            i += 1
        label["text"]+="\n------------------------------------------------------------------------------------------------------------------------"
        label["text"]+="\n"

    
#---------------------------------------------------------------------------------------------------------------------
    @staticmethod
    #con esta funcion vemos el nivel de basura de las salas
    def verBasura(label):
        salas=Sala.salas
        label["text"]+="\n-----------------------------------------------------------------------------------------------------------------------"
        label["text"]+="\n"+"{0:>5} {1:>23}".format("Sala", "Nivel de basura""\n")
        label["text"]+="-------------------------------------------------------------------------------------------------------------------------"

        i = 0
        while i < len( salas):
            label["text"]+="\n"+"{0:>5} {1:>25} ".format(salas[i].getNumero(), salas[i].getBasura())
            i += 1
        label["text"]+="\n------------------------------------------------------------------------------------------------------------------------"
        label["text"]+="\n"
    
    
        
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------
    #Funcion para cuando le demos salir empiece a serializar el programa(Guarde la informacion) 
    #     
    @staticmethod
    def salirDelSistema():
        picklefile = open("./baseDeDatos/clientes", "wb")
        picklefile2=open("./baseDeDatos/Peliculas", "wb")
        picklefile3=open("./baseDeDatos/trabajadores", "wb")
        picklefile4=open("./baseDeDatos/salas", "wb")
        pickle.dump(Cliente.clientes, picklefile)
        pickle.dump(Pelicula.peliculas, picklefile2)
        pickle.dump(Trabajador.trabajadores, picklefile3)
        pickle.dump(Sala.salas, picklefile4)
        picklefile.close()
        picklefile2.close()
        picklefile3.close()
        picklefile4.close()
        quit()    
            
    
            








                
                
            
    
                    
    
          
          
                













                
        

                
    
        
    


   
        
