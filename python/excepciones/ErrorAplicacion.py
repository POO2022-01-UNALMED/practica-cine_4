
class ErrorAplicacion(Exception):

    def __init__(self,mensaje):
        self.mensajeError = "Manejo de errores de la aplicacion:"+ mensaje
        super().__init__(self.mensajeError)