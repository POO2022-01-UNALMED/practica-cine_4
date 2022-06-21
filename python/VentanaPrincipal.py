from tkinter import messagebox
import tkinter
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from Funcionalidades import Funcionalidades
from gestorAplicacion.componentes.Cartelera import Cartelera
from gestorAplicacion.componentes.Cliente import Cliente
from tkinter import messagebox as MessageBox 
from gestorAplicacion.componentes.Pelicula import Pelicula
class VentanaSecundaria(Toplevel):

    en_uso = False #Permite saber si hay una ventanaSecundaria abierta

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clientesT=[]
        self.ventanaInicio = None
        self.focus()
        self.title("Ventana de usuario")
        self.geometry("870x750")
        self.option_add('*tearOff', False)        
        self.iconbitmap('./imagenes/iconon.ico')
        

        #creamo nuestro menu
        self.menubar = Menu(self)

        self.menuArchivo = Menu(self.menubar)
        self.menuArchivo.add_command(label = "Aplicacion", command = self.descripcionApp)
        self.menuArchivo.add_command(label = "Salir", command = self.salirVentana)

        #Ponemos nuestras funcionalidades en el menu de procesos
        self.menuProceso = Menu(self.menubar)
        self.menuProceso.add_command(label = "Comprar boleteria",command=self.prueba)
        
        self.menuProceso.add_command(label = "Buscar una reserva",command=self.buscarReserva)
        
        self.menuProceso.add_command(label = "Verificar integridad de las salas",command=self.integridadSala)        
        self.menuProceso.add_command(label = "Hacer devolucion", command=self.devolucion )
        self.menuProceso.add_command(label = "Limpiar salas",command=self.limpiarSala)
        self.editarCar = Menu(self.menuProceso)
        self.menuProceso.add_cascade(menu = self.editarCar,label = "Editar la cartelera")
        self.editarCar.add_command(label= "ver cartelera",command=self.verCartelera)
        self.editarCar.add_command(label= "cambiar cartelera",command=self.editar)
        

        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Contactos", command = self.ayuda)
        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProceso)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar  




        #Para ver si una ventana esta abierta
        self.__class__.en_uso = True


        #Creamos los frame
        
        
        self.frame = Frame(self, borderwidth=15, bg='#FF420E', )
        self.frame.pack(expand=True,fill=BOTH,ipadx=5, padx=2,ipady=2,pady=2)
        self.frame.config(relief="sunken")
        

        self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
        self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
        
        self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
        self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
        
        self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
        self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

        self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)


        

       
        
     

        

    #Esta funcione es para poder comprar boleteria 
    def prueba(self):
        
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 
        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)


        #Estas entradas es para pedir los datos al usuario

        self.nombre=StringVar()
       
        self.entryNombre = tk.Entry(self.frame2, textvariable=self.nombre)
        self.entryNombre.grid(column=4, row=2, sticky='ew', padx=10, pady=10)
        self.labelNombre = tk.Label(self.frame2, text="Nombre", font=("Arial",14))
        self.labelNombre.grid(column=3, columnspan=1,row=2, sticky='ew', padx=30, pady=10)
    
    
        self.cedula=StringVar()
        self.cedula.set("1")
        self.entrycedula = tk.Entry(self.frame2, textvariable=self.cedula)
        self.entrycedula.grid(column=4, row=3, sticky='ew', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame2, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=3, row=3, sticky='ew', padx=30, pady=10)
    
        self.celular=StringVar()
        
        self.entryNombre = tk.Entry(self.frame2, textvariable=self.celular)
        self.entryNombre.grid(column=4, row=4, sticky='ew', padx=10, pady=10)
        self.labelNombre = tk.Label(self.frame2, text="Celular", font=("Arial",14))
        self.labelNombre.grid(column=3, columnspan=1,row=4, sticky='ew', padx=30, pady=10)
    
    
        self.sexo =StringVar()
        
        self.entrySexo  = tk.Entry(self.frame2, textvariable=self.sexo )
        self.entrySexo .grid(column=4, row=5, sticky='ew', padx=10, pady=10)
        self.labelSexo  = tk.Label(self.frame2, text="Sexo ", font=("Arial",14))
        self.labelSexo .grid(column=3,columnspan=1,  row=5, sticky='ew', padx=30, pady=10)
    
        self.edad=StringVar()
        
        self.entryEdad= tk.Entry(self.frame2, textvariable=self.edad)
        self.entryEdad.grid(column=4, row=6, sticky='w', padx=10, pady=10)
        self.labelEdad = tk.Label(self.frame2, text="Edad", font=("Arial",14))
        self.labelEdad.grid(column=3,columnspan=1,  row=6, sticky='w', padx=30, pady=10)
        

        #En esta parte vamos a pregunatrle a usuario si quiere ver una pelicula, y con base en eso se 
        # le saldra unas peliculas determinadas

        self.labelPelicula= Label(self.frame3, text="¿Quires ver peliculas 3D?", font=("Arial",14))
        self.labelPelicula.grid(column=1000, row=0, ipadx=0, ipady=0, padx=15, pady=0)



        self.combo = Combobox(self.frame3, state="readonly",values=["si", "no"])
        self.combo.place(x=60, y=49)




        self.labelVip= Label(self.frame4, text="¿Quires sillas Vip?", font=("Arial",14))
        self.labelVip.grid(column=0, columnspan=1,row=0,  padx=60, pady=40)



        self.combo2 = Combobox(self.frame4, state="readonly",values=["si", "no"])
        self.combo2.place(x=75, y=89)
        
        #Aqui guardamos al cliente en una lista temporal para ver luego registarlo en la lista serealizada
        def siguiente():
            newCliente=Cliente(self.cedula.get(), self.celular.get(), self.nombre.get(), self.sexo.get(), self.edad.get())
            if Funcionalidades.buscarCliente(newCliente)==None:
                self.clientesT.append(newCliente)
                messagebox.showinfo("Mensaje", "Se ha registrado") 
            else:
                MessageBox.showinfo("Mensaje", "Cliente antiguo") 
             
            #Aqui le van a salir un lista de peliculas dependiendo lo que haya selecionada antes, igual que las sillas
            self.frame2.pack_forget()
            self.frame4.pack_forget()
            self.frame3.pack_forget()
            self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
            self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

            self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
            self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

            selection = self.combo.get()        
            selection2 = self.combo2.get() 
            
            self.labelPelicula=Label(self.frame2, text="Selecione la Pelicula", font=("Arial",14))
            self.labelPelicula.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
            self.combo = Combobox(self.frame4, state="readonly",values=["si", "no"])
            self.combo.place(x=75, y=89)


            if selection=="si":
                self.combo = Combobox(self.frame2, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 1))
                self.combo.place(x=20, y=90)
            else:
                self.combo =Combobox(self.frame2, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 2))
                self.combo.place(x=20, y=90)
            
            botonSiguiente.destroy()

            #Aqui le van a salir las sillas disponibles
            def selecionar():
                titulo=tk.Label(self.frame3, text="Selecione la silla", font=("Arial",14))
                titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
                peli=self.combo.get()[0]
                if selection2=="si":
                    self.combo2 = Combobox(self.frame3, state="readonly",values=Funcionalidades.buscarSillaLibre(int(peli), 2,Funcionalidades.inicializarSalas()))
                    self.combo2.place(x=20, y=120)
                else:
                    self.combo2 =Combobox(self.frame3, state="readonly",values=Funcionalidades.buscarSillaLibre(int(peli), 1,Funcionalidades.inicializarSalas())+Funcionalidades.buscarSillaLibre(int(peli), 3,Funcionalidades.inicializarSalas()))
                    self.combo2.place(x=20, y=120)
                
                #EL boton de salir donde guardara la informacion y saldra de nuevo la pagina de inicio
                def salir():
                    self.frame2.pack_forget()
                    self.frame4.pack_forget()
                    self.frame3.pack_forget()
                    self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                    self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                    
                    self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                    self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                    
                    self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                    self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                    self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                    self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                    finalizar.destroy()

                finalizar=Button(self.frame, text="Finalizar", command=salir)
                finalizar.pack()

            botonselecionar= Button(self.frame2, text="Selecionar",command=selecionar)
            botonselecionar.grid(column=0, row=12, ipadx=15, ipady=5, padx=25, pady=50)

        botonSiguiente = Button(self.frame,text= "Siguiente",command=siguiente)
        botonSiguiente.pack(ipadx = 0, ipady =0, padx = 2, pady= 2)           


#-----------------------------------------------------------------------------------------------------------------
    #Con este metodo realizaremos una busqueda en nuestra lista de cliente ya serealizada
    #aqui realizamos los frame correspondientes a esta funcion
    def buscarReserva(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        titulo=tk.Label(self.frame2, text="Ingrse la cedula del cliente", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=20)
        self.cedula=StringVar()
        self.cedula.set("")
        self.entrycedula = tk.Entry(self.frame2, textvariable=self.cedula)
        self.entrycedula.grid(column=2, row=3, sticky='ew', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame2, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=0, row=3, sticky='ew', padx=30, pady=10)

    #aqui vamos a buscar al cliente , llamando a la funcionalidad de buscar el cliente mediante la cecula que solictamos 
    #anteriormente
        def confirmar():
                       
            cliente=Funcionalidades.buscarClien(self.cedula.get())
            self.frame3.pack_forget()
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#FFFFFF')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            if cliente!=None:
                lanombre=tk.Label(self.frame3, text="Nombre", font=("Arial",14))
                lanombre.grid(column=1,columnspan=4, row=0, padx=5, pady=5)
                nombre=tk.Label(self.frame3, text=f"{cliente.getNombre()}", font=("Arial",14))
                nombre.grid(column=1,columnspan=4, row=1, padx=5, pady=5)
                
                lacedula=tk.Label(self.frame3, text="Cedula", font=("Arial",14))
                lacedula.grid(column=5,columnspan=9, row=0, padx=58, pady=5)
                cedula=tk.Label(self.frame3, text=f"{cliente.getCedula()}", font=("Arial",14))
                cedula.grid(column=5,columnspan=9, row=1, padx=5, pady=5)
            else:
                nombre=tk.Label(self.frame3, text="No existe", font=("Arial",14))
                nombre.grid(column=1,columnspan=4, row=0, padx=10, pady=50)
            
            botonconf.destroy()
            #Aqui vamos a restaurar nuestra ventana usuario principal
            def salir2():
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget()
                self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                
                self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                
                self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                botonsalir.destroy()
            botonsalir=Button(self.frame, text="Salir", command=salir2)
            botonsalir.pack()
            
        botonconf=Button(self.frame, text="Confirmar", command=confirmar)
        botonconf.pack()

 #----------------------------------------------------------------------------------------------------------------------
    #esta funcion nos verificara el estado de nuestra silla
    #creamos los frames correspondientes
    def integridadSala(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        titulo=tk.Label(self.frame2, text="Ingrse el numero de sala", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=20)
        
        numeroSala=StringVar()
        numeroSala.set("")
        entrynumeroSala = tk.Entry(self.frame2, textvariable=numeroSala)
        entrynumeroSala.grid(column=2, row=3, sticky='ew', padx=10, pady=10)
        labelnumeroSala = tk.Label(self.frame2, text="Numero de Sala", font=("Arial",14))
        labelnumeroSala.grid(column=0, row=3, sticky='ew', padx=30, pady=10)


        #llamamos a la funcionalidad correspondiente 
        def confirmar():
            estado=Funcionalidades.vericarSilla(numeroSala.get())
            nombre=tk.Label(self.frame3, text=f"{estado}", font=("Arial",14))
            nombre.grid(column=1,columnspan=4, row=1, padx=5, pady=5)
            botonconf.destroy()
            #restaramos la ventana de usuario
            def salir2():
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget()
                self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                
                self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                
                self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                botonsalir.destroy()
            botonsalir=Button(self.frame, text="Salir", command=salir2)
            botonsalir.pack()

        botonconf=Button(self.frame, text="Confirmar", command=confirmar)
        botonconf.pack()
    

#----------------------------------------------------------------------------------------------------------
    #con este metodo vamos hacer una devolucion al cliente asigando a una determinda silla
    #si la silla esta dañada se le cobrara mas.
    def devolucion(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        
        
        titulo=tk.Label(self.frame2, text="Ingrse la cedula del cliente", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=20)
        self.cedula=StringVar()
        self.cedula.set("")
        self.entrycedula = tk.Entry(self.frame2, textvariable=self.cedula)
        self.entrycedula.grid(column=2, row=3, sticky='ew', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame2, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=0, row=3, sticky='ew', padx=30, pady=10)

        #aqui llamos a la funcionalidad correspondiente
        def confirmar():
            buscar=Funcionalidades.buscarClien(self.cedula.get())
            if buscar!=None:
                cliente=Funcionalidades.devolucion(buscar)
            else:
                cliente=None
            self.frame3.pack_forget()
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#FFFFFF')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            print(buscar)

            if cliente != None:
                lanombre=tk.Label(self.frame3, text=f"{cliente}", font=("Arial",14))
                lanombre.grid(column=1,columnspan=4, row=0, padx=5, pady=5)

            else:
                lanombre=tk.Label(self.frame3, text="No existe", font=("Arial",14))
                lanombre.grid(column=1,columnspan=4, row=0, padx=5, pady=5)
            botonconf.destroy()
            
            
            def salir2():
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget()
                self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                
                self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                
                self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                botonsalir.destroy()
            botonsalir=Button(self.frame, text="Salir", command=salir2)
            botonsalir.pack()

                

        botonconf=Button(self.frame, text="Confirmar", command=confirmar)
        botonconf.pack()
    


#-----------------------------------------------------------------------------------------------------------------
    #limpiamos la sala que este con basura, la basura se genera con registrar un cliente, y que el cliente elija un combo de comida 
    def limpiarSala(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        
        
        

        titulo=tk.Label(self.frame2, text="Ingrse el numero de sala a limpiar", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=20)
        
        numeroSala=StringVar()
        numeroSala.set("")
        entrynumeroSala = tk.Entry(self.frame2, textvariable=numeroSala)
        entrynumeroSala.grid(column=2, row=3, sticky='ew', padx=10, pady=10)
        labelnumeroSala = tk.Label(self.frame2, text="Numero de Sala", font=("Arial",14))
        labelnumeroSala.grid(column=0, row=3, sticky='ew', padx=30, pady=10)

        #llamamos a la funcionalidad correspondiente
        def confirmar():
            buscar=Funcionalidades.PedirTrabajador(1)
            
            if buscar != None:
                sala=Funcionalidades.limpiarBasura(buscar,numeroSala.get())
                nombre=tk.Label(self.frame3, text=f"{sala}", font=("Arial",14))
                nombre.grid(column=1,columnspan=4, row=1, padx=5, pady=5)
            
            botonconf.destroy()
            
            def salir2():
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget()
                self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                
                self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                
                self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                botonsalir.destroy()
            botonsalir=Button(self.frame, text="Salir", command=salir2)
            botonsalir.pack()

        botonconf=Button(self.frame, text="Confirmar", command=confirmar)
        botonconf.pack() 

#-----------------------------------------------------------------------------------------------------------------------
    #editamos la cartelera, aqui vamos a cambiar a un pelicula dependiendo si es 3d o no
    def editar(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.labelPelicula= Label(self.frame2, text="¿Quires editar peliculas 3D?", font=("Arial",14))
        self.labelPelicula.grid(column=0, row=0, ipadx=0, ipady=0, padx=15, pady=55)



        self.combo = Combobox(self.frame2, state="readonly",values=["si", "no"])
        self.combo.place(x=55, y=110)

        def siguiente():
            
            self.frame3.pack_forget()
           
            
            self.frame3 = Frame(self.frame,borderwidth=70, bg='#FFFFFF')
            self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

           
            selection = self.combo.get()        
             
            
            self.labelPelicula=Label(self.frame3, text="Selecione la Pelicula", font=("Arial",14))
            self.labelPelicula.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
            


            if selection=="si":
                self.combo = Combobox(self.frame3, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 1))
                self.combo.place(x=20, y=90)
            else:
                self.combo =Combobox(self.frame3, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 2))
                self.combo.place(x=20, y=90)


            botonconf.destroy()

            def siguiente2():
                #Realizamos esto para poder solo tener el nombre de la pelicula que vamos a cambiar y no el numero de la pelicula
                selection = self.combo.get()        
                
                a=selection.split(" ")
                a.pop(0)
                a.pop(0)
                pelicula = " ".join(a)
                
                    
                
                self.frame2.pack_forget()
                self.frame4.pack_forget()
                self.frame3.pack_forget() 

                self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
                
                self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                
                self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
                self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

                self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
                self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

                self.labelPelicula= Label(self.frame2, text="¿Ingrese los datos de la nueva pelicula?", font=("Arial",14))
                self.labelPelicula.grid(column=0, row=0, ipadx=0, ipady=0, padx=15, pady=55)

                #aqui pedimos que ingrese los atributos de la nueva pelicula para poder cambiarla con la otra
                
                nombre=StringVar()
       
                entryNombre = tk.Entry(self.frame2, textvariable=nombre)
                entryNombre.grid(column=1, row=2,  padx=10, pady=10)
                labelNombre = tk.Label(self.frame2, text="Nombre", font=("Arial",14))
                labelNombre.grid(column=0, row=2,  padx=30, pady=10)
            
            
                director=StringVar()
                director.set("")
                entrydirector = tk.Entry(self.frame2, textvariable=director)
                entrydirector.grid(column=1, row=3,  padx=10, pady=10)
                labeldirector = tk.Label(self.frame2, text="Director", font=("Arial",14))
                labeldirector.grid(column=0, row=3,   padx=30, pady=10)
            
                ano=StringVar()
                
                entryano = tk.Entry(self.frame2, textvariable=ano)
                entryano.grid(column=1, row=4, padx=10, pady=10)
                labelano = tk.Label(self.frame2, text="Ano", font=("Arial",14))
                labelano.grid(column=0, columnspan=1,row=4,  padx=30, pady=10)
            
            
                duracion =StringVar()
                
                entryduracion  = tk.Entry(self.frame2, textvariable=duracion )
                entryduracion .grid(column=1, row=5,  padx=10, pady=10)
                labelduracion  = tk.Label(self.frame2, text="Duracion ", font=("Arial",14))
                labelduracion .grid(column=0,columnspan=1,  row=5,   padx=30, pady=10)
            
                genero=StringVar()
                
                entrygenero= tk.Entry(self.frame2, textvariable=genero)
                entrygenero.grid(column=1, row=6,  padx=10, pady=10)
                labelgenero = tk.Label(self.frame2, text="Genero", font=("Arial",14))
                labelgenero.grid(column=0,columnspan=1,  row=6,  padx=30, pady=10)

                pais=StringVar()
                
                entrypais= tk.Entry(self.frame2, textvariable=pais)
                entrypais.grid(column=1, row=7,  padx=10, pady=10)
                labelpais = tk.Label(self.frame2, text="Pais", font=("Arial",14))
                labelpais.grid(column=0,columnspan=1,  row=7, padx=30, pady=10)

                calificacion=StringVar()
                
                entrycalificacion= tk.Entry(self.frame2, textvariable=calificacion)
                entrycalificacion.grid(column=1, row=8,  padx=10, pady=10)
                labelcalificacion = tk.Label(self.frame2, text="Calificacion", font=("Arial",14))
                labelcalificacion.grid(column=0,columnspan=1,  row=8,  padx=30, pady=10)

                precio=StringVar()
                
                entryprecio= tk.Entry(self.frame2, textvariable=precio)
                entryprecio.grid(column=1, row=9,  padx=10, pady=10)
                labelprecio = tk.Label(self.frame2, text="Precio", font=("Arial",14))
                labelprecio.grid(column=0,columnspan=1,  row=9,  padx=30, pady=10)
                botonSigueinte.destroy()
                
                #aqui finalmente cambiamos la pelicula, llamando a la funcionalidad 
                def siguiente3():               
                     
                    peliculaNueva=Pelicula(nombre.get(), director.get(),ano.get(),duracion.get(),genero.get(), pais.get(),calificacion.get(),precio.get())
                    cambio=Funcionalidades.cambiarPelicula(pelicula,peliculaNueva)
                    descripcion = MessageBox.showinfo(title = "Mensaje", message = "Se ha cambiado exitosamente",
                    detail = f"{cambio}")
                    
                    botonSigueinte2.destroy()
                    def salir2():
                        self.frame2.pack_forget()
                        self.frame4.pack_forget()
                        self.frame3.pack_forget()
                        self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
                        self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
                        
                        self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
                        self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
                        
                        self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
                        self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

                        self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
                        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
                        botonsalir.destroy()

                
                    botonsalir=Button(self.frame, text="Salir", command=salir2)
                    botonsalir.pack(ipadx = 0, ipady =0, padx = 0, pady= 0)
                
                botonSigueinte2=Button(self.frame, text="Confirmar", command=siguiente3)
                botonSigueinte2.pack() 

            botonSigueinte=Button(self.frame, text="Confirmar", command=siguiente2)
            botonSigueinte.pack() 

        botonconf=Button(self.frame, text="Confirmar", command=siguiente)
        botonconf.pack()

    #con este metodo vamos a imprimir la lista de peliculas que hay en el cine
    def verCartelera(self):
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame3.pack_forget() 

        self.frame2 = tk.Frame(self.frame, borderwidth=10, bg='#F98866' )
        
        self.frame2.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        
        self.frame3 = Frame(self.frame,borderwidth=70, bg='#F98866')
        self.frame3.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)

        self.frame4 = Frame(self.frame, borderwidth=10, bg='#F98866' )
        self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
        self.labelPelicula= Label(self.frame2, font=("Arial",14))
        self.labelPelicula.grid(column=0, row=0, ipadx=0, ipady=0, padx=15, pady=55)
        l=Funcionalidades.verCartelera(self.labelPelicula)

        #restauramos la ventana de usuario
        def salir2():
            self.frame2.pack_forget()
            self.frame4.pack_forget()
            self.frame3.pack_forget()
            self.frame2 = Frame(self.frame,width=970, height=600, bg="#F98866")
            self.frame2.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
            
            self.label =Label(self.frame2,text= "¡¡Bievenido!!\n Al administrador del cine", font = ("Segoe UI", 32),fg = "black", bg = "#F98866")
            self.label.pack(ipadx = 0, ipady =0, padx = 5, pady= 5)
            
            self.frame3 = Frame(self.frame,width=102, height=102, bg='#F98866')
            self.frame3.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)

            self.frame4 = Frame(self.frame, width=1870, height=1750, borderwidth=10, bg='#F98866' )
            self.frame4.pack(expand=True,fill="x",ipadx = 2, ipady =0, padx = 2, pady= 2)
            botonsalir.destroy()

    
        botonsalir=Button(self.frame, text="Salir", command=salir2)
        botonsalir.pack(ipadx = 0, ipady =0, padx = 0, pady= 0)
        



        

        


#--------------------------------------------------------------------------------------------------------------
    #este metodo muestra una breve descripcion de la app

    def descripcionApp(self):
        descripcion = messagebox.showinfo(title = "Mensaje", message = "Administrador de Cine",
        detail = "El prigrama permite hacer varias funcionalidades de como administar un cine.")

#--------------------------------------------------------------------------------------------------------------
    # Retorna a la Ventana de Inicio del programa.

    def salirVentana(self):
        self.__class__.en_uso = False
        self.ventanaInicio.deiconify()
        return super().destroy()

    

#-------------------------------------------------------------------------------------------------------------------------------------
    # Muestra un Message Box con los nombres de los autores de la aplicación.
    def ayuda(self):
        ayudaPopUp = messagebox.showinfo(title = "Mensaje", message = "Contactos: \n\n Kevin Prieto peña: \n kprietop@unal.edu.co\n Simon Lopez Gu \n silopezg@unal.edu.co")



VentanaSecundaria1=VentanaSecundaria()
VentanaSecundaria1.mainloop()


