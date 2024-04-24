from Domain.Titular import Titular

class Producto(Titular):
    def __init__(self, id_producto, nombre_producto, producto, clave):
        super().__init__(producto, clave)
        self._id_producto = id_producto
        self.nombre_producto = nombre_producto

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto
        