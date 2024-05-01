from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Persona import Persona, personas

class Asesor(Titular, Producto, Persona):

    def __init__(self):

        pass
    #menu del asesor, permite la opcion de crear un titular y crear un producto

    def crear_titular(self, datos_personas):
        titular = Titular(None, None, None, None, None, None, None, None, None)
        super().crear_titular()
        return titular

    def crear_producto(self):
        producto = Producto(None, None)
        producto.crear_producto()



        producto.id_titular = self.id

        if self.id in personas:

            productos_titular = personas[self.id].get("Productos", {})
            productos_titular[producto.id_producto] = producto.nombre_producto
            personas[self.id]["Productos"] = productos_titular
            print("Producto creado exitosamente.")
        else:
            print("Error: No se pudo encontrar el titular asociado al producto en la base de datos.")

        return producto

