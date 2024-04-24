from Domain.Persona import Persona

class Titular(Persona):
    def __init__(self, id, nombre, apellido, correo, telefono, usuario, producto, clave):
        super().__init__(id,nombre, apellido, correo, telefono, usuario)
        self._producto = producto
        self._clave = clave

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, producto):
        self.producto = _producto

    #creacion de metodos

    def crear_persona(self, producto):
        super().crear_persona()
        valor = int(input("Selecciona 1. Ahorros || 2. corriente"))
        self.producto = producto.productos[valor]
        self._clave = int(input("Ingresa la clave: "))
        self.personas[self._id] = self.nombre, self.apellido, self.correo, self.telefono, self.usuario, self._clave, self.producto

    def __str__(self, producto):
        print = f"""
        {super().__str__()}
        producto: {self.producto}
    
        """
