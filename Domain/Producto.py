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

    #metodos propios
    def crear_producto(self):
        self._id_producto = int(input("id producto: "))
        self.nombre_producto = input("nombre producto: ")
        self.productos[self._id_producto] = self.nombre_producto
        print("\n\tCreación del producto")
        producto = int(input("\nSelecciona el tipo de cuenta:\n"
                             "1. Ahorros:\n"
                             "2. Corriente: "))

        if producto == 1:
            self.producto = "Ahorros"
            datos_persona["Producto"] = self.producto
        elif producto == 2:
            self.producto = "Corriente"
            datos_persona["Producto"] = self.producto
        else:
            print("Opción no válida")

    def mostrar_producto(self):
        for i in self.productos.items():
            print(i)



