from VentanaPrincipal import VentanaSecundaria
from tkinter import messagebox as MessageBox, ttk 
from tkinter import *
from Funcionalidades import Funcionalidades
import tkinter as tk

class ventanaInicio(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
                
        # Editamos nuestra ventana 
        self.geometry("875x565")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.iconbitmap('./imagenes/iconon.ico')
        
       

        #variables para la descriop de los desarolladores
        self.var1 = tk.StringVar()
        self.var1.set("Los Super Desaroolladores")
        self.var2 =tk.StringVar()
        
        

        #crearemos nuestros frames.
        
        #frame del texto de bievenidatextoHDV
        self.frame1 = tk.Frame(self, width=400, height=500,borderwidth=15, bg="Black")
        self.frame1.pack(side="left", expand=True)
        
        self.frame1.config(relief="sunken")
        self.frame2 = tk.Frame(self.frame1, width=400, borderwidth=5,height=150, bg="sandy brown")
        self.frame2.grid(row=0, column=0) 
        self.frame2.config(relief="ridge")       
        self.etiquetaBienvenida = Label(self.frame2, text="¡¡HOLA!!\n Bienvenido al administrador \nde tu Cine\n""☻", font=("Segoe UI", 18))
        self.etiquetaBienvenida.place(x=200, y=75, anchor="center")
        self.etiquetaBienvenida.config(fg="black", bg="sandy brown")
        
        self.labelDesa = Label(self.frame2, font=("Segoe UI", 0))
        self.labelDesa.place(x=200, y=120, anchor="center") 
        self.labelDesa.config(fg="black", bg="sandy brown")


        self.frame3 = tk.Frame(self.frame1, width=400, height=380, bg="yellow")
        self.frame3.grid(row=1, column=0)
        
        self.frame4 = tk.Frame(self, width=400, height=500,borderwidth=15, bg="black")
        self.frame4.pack(side="right")
        self.frame4.config(relief="sunken")
        
        
        self.frame5 = tk.Frame(self.frame4, width=400, height=160,borderwidth=5, bg="sandy brown")
        self.frame5.grid(row=0, column=0)
        self.frame5.config(relief="ridge")
        self.textoDescripcion = Label(self.frame5, textvariable=self.var1, font = ("Segoe UI", 8))
        self.textoDescripcion.bind('<ButtonPress-1>', self.cambioDescripcion)
        self.textoDescripcion.place(x=200, y=75, anchor="center")
        
        self.frame6 = tk.Frame(self.frame4, width=400,borderwidth=5, height=350, bg="black")
        self.frame6.grid(row = 1, column = 0)
        self.frame6.config(relief="ridge")           
        
        
        
        


         #creamos nuestro menu
        self.menubar = tk.Menu(self)
        self.menuInicio = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Inicio", menu=self.menuInicio)
        self.menuInicio.add_command(label="Salir",command=self.salir)
        self.menuInicio.add_command(label="Descripcion",command=self.desno)
        self["menu"] = self.menubar
        


        #creamos los frames donde vamos a colocar las fotos
        self.frameFoto1 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto1.place(x=0, y=0)
        self.frameFoto2 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto2.place(x=208, y=0)
        self.frameFoto3 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto3.place(x=0, y=168)
        self.frameFoto4 = tk.Frame(self.frame6, width=200, height=170,bg="black")
        self.frameFoto4.place(x=208, y=168)
        

        
        
        #guardaremos las fotos, para luego cargarlas con un for
        self.fotosDesarolla = ['./imagenes/K1.png', './imagenes/K2.png', './imagenes/K3.png', './imagenes/K4.png','./imagenes/S1.png', './imagenes/S2.png', './imagenes/S3.png', './imagenes/S4.png', './imagenes/U1.png', './imagenes/U2.png', './imagenes/U3.png', './imagenes/U4.png']
        self.listaFotos = []
        

        for i in self.fotosDesarolla:
            imagen = PhotoImage(file=i)
            
            self.listaFotos.append(imagen)

        self.p1 = Label(self.frameFoto1)
        self.p2 = Label(self.frameFoto2)
        self.p3 = Label(self.frameFoto3)
        self.p4 = Label(self.frameFoto4)


        self.p1["image"] = self.listaFotos[8]
        
        self.p1.pack()
        self.p2["image"] = self.listaFotos[9]
        self.p2.pack()
        
        self.p3["image"] = self.listaFotos[10]
        self.p3.pack()
        
        self.p4["image"] = self.listaFotos[11]
        self.p4.pack()
        self.contador = 0

        #vamos a recorer la lista de la imagines de lapp, para luego cargarlas y guardarlas en una lista
        self.fotosApp = ['./imagenes/p1.png', './imagenes/p2.png', './imagenes/p3.png','./imagenes/p4.png']
        self.listaFotosApp = []
        for i in self.fotosApp:
            imagen = PhotoImage(file=i)
            self.listaFotosApp.append(imagen)

        #creamos el boton para abrir la ventana de usuario
        
        
        self.botonCambioa = Button(self.frame3, image=self.listaFotosApp[0],command=self.abrirVentanaSecundaria)
        self.botonCambioa.pack()
        self.botonCambioa.bind('<Enter>', self.cambio)

        
        self.acumulador = 0
        self.numClicks = 0
        
    #informacion de la app
    def desno(self):
        descripcion = MessageBox.showinfo(title = "Mensaje", message = "Aministrador de Cine",
        detail = "Version 1, Gracias a esta app logaras administar tu cine de la mejor manera\n !!Lo MEJEOR PARA LO MEJOR!!")
        
    
    def cambioDescripcion(self,cont):
        self.numClicks += 1
        if (self.numClicks == 1):
            self.var1.set("Nombre: Kevin Prieto Peña \n"" Le gustan los deportes \n""Ingeniero de sistemas e informatica\n""Vive en Medellin\n")
            self.evento(12)
        elif (self.numClicks == 2):
            self.var1.set("Nombre: Simon Lopez Guarin \n"" Le gustan las menores \n""Estadistico\n""Vive en Medellin\n")
            self.evento(12)
       
            self.numClicks = 0

    #PROVOCA LA APERTURA DE LAS IMAGENES DE CADA DESARROLLADOR SEGUN SU IDENTIFICADOR POSICIONAL
    def evento(self,cont):
        foto1 = 0
        foto2 = 0
        foto3 = 0
        foto4 = 0
        self.contador += 1
        if self.contador == 1:
            foto1 = self.contador - 1
            foto2 = self.contador
            foto3 = self.contador + 1
            foto4 = self.contador + 2
        elif self.contador == 2:
            foto1 = self.contador + 2
            foto2 = self.contador + 3
            foto3 = self.contador + 4
            foto4 = self.contador + 5
        
        self.p1.config(image=self.listaFotos[foto1])
        self.p2.config(image=self.listaFotos[foto2])
        self.p3.config(image=self.listaFotos[foto3])
        self.p4.config(image=self.listaFotos[foto4])
        if self.contador == 2:
            self.contador = 0

    #con esta funcion cambiamos las imagenes
    def cambio(self,conts):
        self.acumulador += 1
        if self.acumulador == 4:
            self.acumulador = 0
        self.botonCambioa.config(image=self.listaFotosApp[self.acumulador])
    
    #con este metodo abrimos la ventana de usario, la cual se abre por medio de un evento
    def abrirVentanaSecundaria(self):
         if not VentanaSecundaria.en_uso:
            self.ventanaUsuario = VentanaSecundaria()
            self.ventanaUsuario.ventanaInicio = self
            self.iconify()

    #con esto nos salimos y guardamos lo que tenemos
    def salir(self):
        Funcionalidades.salirDelSistema()
        return super().destroy()


