from Domain.Producto import Producto

class Cuenta_ahorros(Producto):
    def __init__(self,nombre,apellido, id_producto, numero_cuenta, saldo):
        super().__init__(nombre, apellido, id_producto)
        self.numero_cuenta = numero_cuenta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo