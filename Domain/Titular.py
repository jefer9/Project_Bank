from Domain.Persona import Persona

class Titular(Persona):
    def __init__(self, id, nombre, apellido, correo, telefono, usuario, producto, clave):
        super().__init__(id,nombre, apellido, correo, telefono, usuario)
        self.producto = producto
        self._clave = clave

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave