from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Persona import Persona, personas

class Asesor(Titular, Producto):

    def __init__(self):

        pass
    #menu del asesor, permite la opcion de crear un titular y crear un producto

    def crear_titular(self, datos_personas):
        titular = Titular(None, None, None, None, None, None, None, None, None)
        super().crear_titular()
        return titular

    def crear_producto(self):
        producto = Producto(None, None)
        super().crear_producto()
        id_persona = self.id
        productos = producto.productos
        if id_persona in personas:
            personas[id_persona]["Productos"] = productos

        """print("\n\tCreación del producto")
        producto = int(input("\nSelecciona el tipo de cuenta:\n"
                             "1. Ahorros:\n"
                             "2. Corriente: "))"""


        return producto

