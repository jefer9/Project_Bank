#from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Persona import Persona, personas

class Asesor(Producto, Persona):

    def __init__(self):
        pass

    def crear_persona(self):
        persona_1 = Persona(None,None,None,None,None,None,None)
        persona_1.crear_persona()
    def crear_producto(self):
        producto = Producto(None, None, None, None, None, None, None, None, None,None)
        super().crear_producto()
        return producto

