from excepciones.ErrorAplicacion import ErrorAplicacion


class ErrorTipoDato(ErrorAplicacion):

    def __init__(self, mensaje):
        self.mensajeErrores = f" Error tipo de dato { mensaje}" 
        super(ErrorAplicacion,self).__init__(self.mensajeErrores)

class ExcepcionStringNumero(ErrorTipoDato):
    def __init__(self,entrada):
        self.mensajeErrores = "la ingresaste un String, Por favor vuelva a intentarlo de nuevo."
        super(ErrorTipoDato, self).__init__(self.mensajeErrores)


class ExcepcionVacias(ErrorTipoDato):
    def __init__(self,entrada):
        self.mensajeErrores = "Entrada vacia, Por favor ingrese el tipo de dato especifico"
        super().__init__(self.mensajeErrores)


class ExcepcionEnteroString(ErrorTipoDato):
    def __init__(self,entrada):
        self.mensajeErrores="La ingresaste un entero, Por favor vuelva a intentarlo de nuevo." 
        super().__init__(self.mensajeErrores)

class ExcepcionEnteroFloat(ErrorTipoDato):

    def __init__(self,entrada):
        
        self.mensajeErrores=" La ingresaste un float, por favor vuelva a intentarlo de nuevo."
        super().__init__(self.mensajeErrores)

