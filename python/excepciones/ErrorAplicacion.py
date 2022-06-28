
class ErrorAplicacion(Exception):

    def __init__(self,mensaje):
        self.mensajeErrores = "Manejo de errores de la aplicacion:"+ mensaje
        super().__init__(self.mensajeErrores)