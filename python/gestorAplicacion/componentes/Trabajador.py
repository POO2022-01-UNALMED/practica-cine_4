from gestorAplicacion.componentes.Persona import Persona

class Trabajador(Persona):
    trabajadores=[]
    def __init__(self,cedula,celular,nombre, sexo, edad,cargo):
        super().__init__(cedula, celular, nombre, sexo, edad)
        self.cargo=cargo
        self.ocupado=False
        
    def getCargo(self):
        return self.cargo
    
    def setCargo(self,cargo):
        self.cargo=cargo
    
    def isOcupado(self):
        return self.ocupado
    
    def setOcupado(self,ocupado):
        self.ocupado=ocupado

    @staticmethod
    def getTrabajadores():
         return Trabajador.trabajadores

    @staticmethod
    def setTabajadores(trbajador):
        Trabajador.trabajadores=trbajador

    @staticmethod
    def despedirTrabajador(self, cedula):
        for i in Trabajador.trabajadores:
            if i.getCedula()==cedula:
                   Trabajador.trabajadores.remove(i)
    


   
        
