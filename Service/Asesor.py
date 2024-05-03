from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Persona import Persona, personas

class Asesor(Titular, Producto, Persona):

    def __init__(self):
        pass

    def crear_titular(self, datos_personas):
        titular = Titular(None, None, None, None, None, None, None, None, None)
        super().crear_titular()
        return titular

    def crear_producto(self):
        producto = Producto(None, None, None)
        producto.crear_producto()

        producto.id_titular = self.id

        if self.id in personas:

            productos_titular = personas[self.id].get("Productos", {})
            productos_titular["Nombre Producto"] = producto.nombre_producto
            productos_titular["Id producto:"] = producto.id_producto
            productos_titular["Saldo: "] = producto.saldo
            personas[self.id]["Productos"] = productos_titular

            # Actualizar el ID del producto en la instancia
            producto.id_producto = productos_titular["Id producto:"]
            print("Producto creado exitosamente.")
        else:
            print("Error: No se pudo encontrar el titular asociado al producto en la base de datos.")

        return producto
