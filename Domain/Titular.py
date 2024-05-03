from Domain.Persona import Persona, personas
from Domain.Credito import Credito


class Titular(Persona):

    def __init__(self, id, nombre, apellido, correo, telefono, usuario, contrasena, producto, clave):
        super().__init__(id, nombre, apellido, correo, telefono, usuario, contrasena)
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
        self._producto = producto

    #creacion de metodos

    """def crear_titular(self,):
        super().crear_persona()
        valor = int(input("Selecciona 1. Ahorros || 2. corriente"))
        self.producto = producto.productos[valor]
        self._clave = int(input("Ingresa la clave: "))
        self.personas[self._id] = self.nombre, self.apellido, self.correo, self.telefono, self.usuario, self._clave, self.producto"""

    def crear_titular(self):
        super().crear_persona()
        self._clave = input("Ingresa la nueva clave: ")
        id_persona = self.id
        if id_persona in personas:
            personas[id_persona]["Clave"] = self._clave
        else:
            print("Error: No se pudo encontrar la persona creada en la base de datos.")

def __str__(self):
        return f"{super().__str__()} producto: {self.producto}"

