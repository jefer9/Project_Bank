from Domain.Titular import Titular

class Credito(Titular):
    def __init__(self, producto, clave, interes, plazo, cantidad):
        super().__init__(producto, clave)
        self.interes = interes
        self._plazo = plazo
        self._cantidad = cantidad

    #hola soy david


    @property
    def plazo(self):
        return self._plazo

    @plazo.setter
    def plazo(self, plazo):
        self._plazo = plazo

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self,_cantidad):
        self._cantidad =_cantidad




