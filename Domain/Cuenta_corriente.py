from Domain.Producto import Producto

class Cuenta_corriente(Producto):
    def __init__(self, id_producto, nombre_producto, numero_cuenta, saldo):
        super().__init__(id_producto, nombre_producto)
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def numero_cuenta(self):
        return self._numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
