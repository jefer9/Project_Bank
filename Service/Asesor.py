from Domain.Titular import Titular
from Domain.Producto import Producto

class Asesor(Titular, Producto):

    titular = Titular(None,None,None,None,None,None,None,None,None)
    producto = Producto(None,None)

    #menu del asesor, permite la opcion de crear un titular y crear un producto

    def crear_titular(self, datos_persona):
        super().crear_titular(datos_persona)

    def crear_producto(self):
        super().crear_producto()






