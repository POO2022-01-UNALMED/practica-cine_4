from tkinter import messagebox
import tkinter
from tkinter.ttk import Combobox
from tkinter import *
import tkinter as tk
from Funcionalidades import Funcionalidades
from gestorAplicacion.componentes.Cliente import Cliente
from tkinter import messagebox as MessageBox 
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
        self.menuProceso.add_command(label = "Editar la cartelera")
        self.menuProceso.add_command(label = "Buscar una reserva")
        self.menuProceso.add_command(label = "Inicializar Cine")
        self.menuProceso.add_command(label = "Verificar integridad de las salas")        
        self.menuProceso.add_command(label = "Hacer devolucion" )
        self.menuProceso.add_command(label = "Limpiar salas")

        

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


