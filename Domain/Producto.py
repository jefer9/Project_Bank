from Domain.Titular import Titular
import random

class Producto:
    def __init__(self, id_producto, nombre_producto, id_titular=None):
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._id_titular = id_titular

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto

    @property
    def nombre_producto(self):
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        self._nombre_producto = nombre_producto

    @property
    def id_titular(self):
        return self._id_titular

    @id_titular.setter
    def id_titular(self, id_titular):
        self._id_titular = id_titular

    productos = {}

    # Métodos propios
    def crear_producto(self):
        self._id_producto = random.randint(1000,99999)
        self._nombre_producto = input("Nombre producto: ")
        self.productos[self._id_producto] = self._nombre_producto


    def mostrar_producto(self):
        for i in self.productos.items():
            print(i)
