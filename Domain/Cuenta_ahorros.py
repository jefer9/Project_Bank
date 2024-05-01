from Domain.Producto import Producto

class Cuenta_ahorros(Producto):
    def __init__(self, id_producto,nombre_producto, numero_cuenta, saldo, titular):
        super().__init__( id_producto, nombre_producto)
        self.numero_cuenta = numero_cuenta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def numero_cuenta(self):
        return self.numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def retirar(self):
        retiro = int(input("Ingrese el valor a retirar: "))
        if retiro > self._saldo:
            print("Fondos insuficientes")
        else:
            self._saldo -= retiro
            print("retiro completado con exito")

    def consultar_saldo(self):
        print("su saldo es: ", self._saldo)

    def consignar(self):
        transeferencia = int(input("Valor a transferir: "))
        num_cuenta_destino = int(input("Numero de cuenta de destino: "))

        if transeferencia > self._saldo:
            print("fondos insuficientes")
        else:
            # Aqui se hace la suma al numero de cuenta destinatario
            print("Transeferencia exitosa")
