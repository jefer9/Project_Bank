from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Persona import Persona


class Asesor(Titular, Producto):

    def __init__(self):
        pass
    #menu del asesor, permite la opcion de crear un titular y crear un producto

    def crear_titular(self):
        titular = Titular(None, None, None, None, None, None, None, None, None)
        super().crear_titular()
        return titular

    def crear_producto(self):
        producto = Producto(None, None)
        super().crear_producto()
        return producto
