from tkinter import messagebox
import tkinter
from tkinter.ttk import Combobox
from tkinter import *

from Funcionalidades import Funcionalidades

class VentanaSecundaria(Toplevel):

    en_uso = False #Permite saber si hay una ventanaSecundaria abierta

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
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
        self.menuProceso.add_command(label = "Comprar boleteria")
        self.menuProceso.add_command(label = "Editar la cartelera")
        self.menuProceso.add_command(label = "Buscar una reserva")
        self.menuProceso.add_command(label = "Inicializar Cine")
        self.menuProceso.add_command(label = "Verificar integridad de las salas")
        self.menuProceso.add_command(label = "Comprar tiquete para un vuelo por destino y fecha")
        self.menuProceso.add_command(label = "Hacer devolucion" )
        self.menuProceso.add_command(label = "Limpiar salas")

        

        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Contactos", command = self.ayuda)

        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProceso)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar
        


        
        self.__class__.en_uso = True

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






