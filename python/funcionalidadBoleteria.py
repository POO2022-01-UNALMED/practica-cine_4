from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.componentes.Cliente import Cliente
from Funcionalidades import Funcionalidades
from tkinter import messagebox as MessageBox 

class comprarBoleteria():
    clientes=[]
    def __init__(self):
        
        
        self.window = tk.Tk()
        
        self.window.title("Comprar Boleteria")
        self.frame = tk.Frame(self.window, width=480, height=320, borderwidth=10, bg='red', )
        self.frame.pack(expand=True)
        self.frame.config(bg="lightblue")
        self.titulo= Label(self.frame, text=f"Bienvenido  a tu cine", font=("Arial",32))
        self.titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
        
    
    
        
        self.nombre=StringVar()
       
        self.entryNombre = tk.Entry(self.frame, textvariable=self.nombre)
        self.entryNombre.grid(column=1, row=2, sticky='w', padx=10, pady=10)
        self.labelNombre = tk.Label(self.frame, text="Nombre", font=("Arial",14))
        self.labelNombre.grid(column=0, columnspan=1,row=2, sticky='w', padx=30, pady=10)
    
    
        self.cedula=StringVar()
        self.cedula.set("1")
        self.entrycedula = tk.Entry(self.frame, textvariable=self.cedula)
        self.entrycedula.grid(column=1, row=3, sticky='w', padx=10, pady=10)
        self.labelCedula = tk.Label(self.frame, text="Cedula", font=("Arial",14))
        self.labelCedula.grid(column=0,columnspan=1,  row=3, sticky='w', padx=30, pady=10)
    
        self.celular=StringVar()
        
        self.entryNombre = tk.Entry(self.frame, textvariable=self.celular)
        self.entryNombre.grid(column=1, row=4, sticky='w', padx=10, pady=10)
        self.labelNombre = tk.Label(self.frame, text="Celular", font=("Arial",14))
        self.labelNombre.grid(column=0, columnspan=1,row=4, sticky='w', padx=30, pady=10)
    
    
        self.sexo =StringVar()
        
        self.entrySexo  = tk.Entry(self.frame, textvariable=self.sexo )
        self.entrySexo .grid(column=1, row=5, sticky='w', padx=10, pady=10)
        self.labelSexo  = tk.Label(self.frame, text="Sexo ", font=("Arial",14))
        self.labelSexo .grid(column=0,columnspan=1,  row=5, sticky='w', padx=30, pady=10)
    
        self.edad=StringVar()
        
        self.entryEdad= tk.Entry(self.frame, textvariable=self.edad)
        self.entryEdad.grid(column=1, row=6, sticky='w', padx=10, pady=10)
        self.labelEdad = tk.Label(self.frame, text="Edad", font=("Arial",14))
        self.labelEdad.grid(column=0,columnspan=1,  row=6, sticky='w', padx=30, pady=10)
        
        
    
        self.registrar=ttk.Button(self.frame, text="Registrar", command=self.siguiente)
        self.registrar.grid(column=0, row=9, ipadx=15, ipady=5, padx=25, pady=50)
        
        
       
        self.window.mainloop()

    def siguiente(self):
        
        newCliente=Cliente(self.cedula.get(), self.celular.get(), self.nombre.get(), self.sexo.get(), self.edad.get())
        if Funcionalidades.buscarCliente(newCliente)==None:
            comprarBoleteria.clientes.append(newCliente)
            messagebox.showinfo("Mensaje", "Se ha registrado") 
        else:
            MessageBox.showinfo("Mensaje", "Cliente antiguo") 
        
        
        window = tk.Toplevel()
        window.withdraw()
        ventana2=tk.Toplevel()
        ventana2.title("Cine")
        frame = tk.Frame(ventana2, width=480, height=320, borderwidth=10, bg='red', )
        frame.pack(expand=True)
        frame.config(bg="lightblue")
            
        titulo=tk.Label(frame, text=f"Se ha registrado con exito", font=("Arial",32))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=50)

        opcion1=ttk.Button(frame, text="Selecionar Pelicula", command=Application)
        opcion1.grid(column=2, row=2, ipadx=15, ipady=5,padx=10, pady=10)
        window.mainloop()
        self.window.destroy()
        




class Application():
    
    def __init__(self):
        
        
        self.main_window = tk.Tk()
        
        self.main_window.title("Comprar Boleteria")
        self.frame = tk.Frame( self.main_window, width=480, height=320, borderwidth=10, bg='red', )
        self.frame.pack(expand=True)
        self.frame.config(bg="lightblue")
        
        
        self.labelPelicula= tk.Label(self.frame, text="¿Quires ver peliculas 3D?", font=("Arial",14))
        self.labelPelicula.grid(column=0, row=9, ipadx=15, ipady=5, padx=25, pady=50)
        
        
        
        self.combo = ttk.Combobox(self.main_window, state="readonly",values=["si", "no"])
        self.combo.place(x=80, y=120)
        
        
        
        
        self.labelVip= tk.Label(self.frame, text="¿Quires sillas Vip?", font=("Arial",14))
        self.labelVip.grid(column=0, columnspan=1,row=27, sticky='w', padx=60, pady=40)
        
        self.selecionar=ttk.Button(self.frame, text="Selecionar",command=self.show_selection)
        self.selecionar.grid(column=0, row=28, ipadx=24, ipady=5, padx=50, pady=110)
        
        self.combo2 = ttk.Combobox(self.main_window, state="readonly",values=["si", "no"])
        self.combo2.place(x=80, y=250)
        
                  
        self.main_window.mainloop()
    
    def show_selection(self):
        
        selection = self.combo.get()
        
        selection2 = self.combo2.get()
        window = tk.Toplevel()
        
        
        window.title("Login Usario")
        
        
        #mainframe
        frame = tk.Frame(window, width=480, height=320, borderwidth=10, bg='red', )
        frame.pack(expand=True)
        frame.config(bg="lightblue")
        titulo=Label(frame, text="Selecione la Pelicula", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
        
        
        
      
        
        registrar=ttk.Button(frame, text="Selecionar",command=self.d)
        registrar.grid(column=0, row=12, ipadx=15, ipady=5, padx=25, pady=50)
        
        if selection=="si":
            self.combo = ttk.Combobox(frame, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 1))
            self.combo.place(x=20, y=90)
        else:
            self.combo = ttk.Combobox(frame, state="readonly",values=Funcionalidades.peliculas(Funcionalidades.inicializarCartelera(), 2))
            self.combo.place(x=20, y=90)
        
        
        window.mainloop() 


    def d(self):
        peli=self.combo.get()[0]
        
        selection2 = self.combo2.get()
        window = tk.Toplevel()
        
        
        window.title("Login Usario")
        
        
        #mainframe
        frame = tk.Frame(window, width=480, height=320, borderwidth=10, bg='red', )
        frame.pack(expand=True)
        frame.config(bg="lightblue")
        titulo=tk.Label(frame, text="Selecione la silla", font=("Arial",14))
        titulo.grid(column=0,columnspan=4, row=0, padx=10, pady=50)
        
        
        
      
        
        registrar=ttk.Button(frame, text="Finalizar",command=self.finalizar)
        registrar.grid(column=0, row=12, ipadx=15, ipady=5, padx=25, pady=50)
        
        if selection2=="si":
            self.combo2 = ttk.Combobox(frame, state="readonly",values=Funcionalidades.buscarSillaLibre(int(peli), 2,Funcionalidades.inicializarSalas()))
            self.combo2.place(x=20, y=120)
        else:
            self.combo2 = ttk.Combobox(frame, state="readonly",values=Funcionalidades.buscarSillaLibre(int(peli), 1,Funcionalidades.inicializarSalas())+Funcionalidades.buscarSillaLibre(int(peli), 3,Funcionalidades.inicializarSalas()))
            self.combo2.place(x=20, y=120)
    
        window.mainloop()
    def finalizar(self):
        peli=self.combo.get()[0]
        a=self.combo2.get()
        b=(a[len(a)-2]+a[len(a)-1])
        silla=Funcionalidades.buscarSilla(int(b), Funcionalidades.inicializarSalas())
        cliente=comprarBoleteria.clientes[len(comprarBoleteria.clientes)-1]
        print(Funcionalidades.asiganarCliente(cliente, int(peli), silla, Funcionalidades.inicializarSalas()))        
        MessageBox.showinfo("Mensaje", f"Se ha comprado la entrada de {cliente.getNombre()}")
        self.main_window.destroy()



if __name__ == "__main__":
   comprarBoleteria()
  
