from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Persona import Persona, personas

class Asesor(Producto, Persona):

    def __init__(self):
        pass

    def crear_persona(self):
        persona_1 = Persona(None,None,None,None,None,None,None)
        persona_1.crear_persona()

    def buscar_persona(self):
        persona_2 = Persona(None, None, None, None, None, None, None)
        persona_2.buscar_persona()

    def modificar_persona(self):
        persona_3 = Persona(None, None, None, None, None, None, None)
        persona_3.modificar_persona()

    def eliminar_persona(self):
        persona_4 = Persona(None, None, None, None, None, None, None)
        persona_4.eliminar_persona()
    def crear_producto(self):
        producto = Producto(None, None, None, None, None, None, None, None, None,None)
        super().crear_producto()
        return producto
    def consultar_BD(self):
        titular1 = Titular(None, None, None, None, None, None, None, None, None, None)
        titular1.consultar_BD()



