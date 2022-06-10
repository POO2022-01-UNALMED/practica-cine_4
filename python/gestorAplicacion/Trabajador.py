from gestorAplicacion.Persona import Persona

class Trabajador(Persona):
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
        
    


   
        
