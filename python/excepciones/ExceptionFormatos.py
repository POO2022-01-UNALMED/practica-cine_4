from ErrorAplicacion import ErrorAplicacion


class ErrorTipoDato(ErrorAplicacion):

    def __init__(self, mensaje):
        self.mensajeErrores = " Error tipo de dato " + mensaje 
        super().__init__(self.mensajeError)

class ExcepcionStringNumero(ErrorTipoDato):
    def __init__(self,entrada):
        self.mensajeErrores = "la entrada es un String, Por favor vuelva a intentarlo de nuevo."
        super().__init__(self.mensajeErrores)


class ExcepcionVacias(ErrorTipoDato):
    def __init__(self,entrada):
        self.mensajeErrores = "Entrada vacia, Por favor ingrese el tipo de dato especifico"
        super().__init__(self.mensajeErrores)


class ExcepcionEnteroString(ErrorTipoDato):
    def __init__(self,entrada):
        self.mensajeErrores="La entrada es un entero, Por favor vuelva a intentarlo de nuevo." 
        super().__init__(self.mensajeErrores)

class ExcepcionEnteroFloat(ErrorTipoDato):

    def __init__(self,entrada):
        self.mensajeErrores="La entrada es un float, por favor vuelva a intentarlo de nuevo."
        super().__init__(self.mensajeErrores)

