from gestorAplicacion.Persona import Persona

class Cliente(Persona):
    def __init__(self,cedula,celular,nombre, sexo, edad,costo):
        super().__init__(cedula, celular, nombre, sexo, edad)
        self.costo=costo
        
    def getCosto(self):
        return self.costo
    def setCosto(self,costo):
        self.costo+=costo


   
        
