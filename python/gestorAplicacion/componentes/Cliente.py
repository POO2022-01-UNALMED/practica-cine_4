from gestorAplicacion.componentes.Persona import Persona

class Cliente(Persona):
    
    clientes=[]
    def __init__(self,cedula,celular,nombre, sexo, edad):
        super().__init__(cedula, celular, nombre, sexo, edad)
        self.costo=0
        
    def getCosto(self):
        return self.costo
    def setCosto(self,costo):
        self.costo+=costo
     
    @staticmethod
    def getclientes():
         return Cliente.clientes

    @staticmethod
    def setclientes(cliente):
        Cliente.clientes = cliente


   
        
