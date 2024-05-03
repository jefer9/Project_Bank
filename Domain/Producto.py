from Domain.Persona import Persona
import random

class Producto(Persona):
    def __init__(self, id_producto, nombre_producto, id, nombre, apellido, correo, telefono,usuario,contrasena):
        super().__init__(id, nombre, apellido, correo, telefono, usuario, contrasena)
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._saldo = 0

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

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    productos = {}

    # Métodos propios
    def crear_producto(self):
        self._id_producto = random.randint(1000,99999)

        #logica para ingresar tabla producto

    def mostrar_producto(self):
        for i in self.productos.items():
            print(i)

    # **************** crear movimientos ****************



    def consignar(self, ):
        consignacion = int(input("Valor a consignar: "))
        total = self._saldo + consignacion
        print("Consignación exitosa. Nuevo saldo:", total)
        # self.productos[self._id_producto] = {'Saldo' : total}

    def retirar(self):
        retiro = int(input("Ingrese el valor a retirar: "))
        if retiro > self._saldo:
            print("Fondos insuficientes")
        else:
            self._saldo -= retiro
            print("retiro completado con exito")

    def consultar_saldo(self):
        print("su saldo es: ", self._saldo)

    def transferir(self):
        transeferencia = int(input("Valor a transferir: "))
        num_cuenta_destino = int(input("Numero de cuenta de destino: "))

        if transeferencia > self._saldo:
            print("fondos insuficientes")
        else:
            # Aqui se hace la suma al numero de cuenta destinatario
            print("Transeferencia exitosa")