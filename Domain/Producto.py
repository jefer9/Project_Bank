from Domain.Titular import Titular

class Producto:
    def __init__(self, id_producto, nombre_producto):
        self._id_producto = id_producto
        self.nombre_producto = nombre_producto

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto

    @property
    def nombre_producto(self):
        return self.nombre_producto

    @nombre_producto.setter
    def nombre_producto(self,nombre_producto):
        self.nombre_producto = nombre_producto

    productos = {}

    def crear_producto(self):
        self._id_producto = int(input("id producto: "))
        self.nombre_producto = input("nombre producto: ")
        self.productos[self._id_producto] = self.nombre_producto

    def mostrar_producto(self):
        for i in self.productos.items():
            print(i)
