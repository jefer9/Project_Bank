from Domain.Persona import Persona
import random
from Domain.ConnexionBD import ConexionBD

class Producto(Persona):
    def __init__(self, id_producto, nombre_producto, id, nombre, apellido, correo, telefono,usuario,contrasena, saldo):
        super().__init__(id, nombre, apellido, correo, telefono, usuario, contrasena)
        self._id_producto = id_producto
        self._nombre_producto = nombre_producto
        self._saldo = saldo

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
        print("Presiona alguna de las opcionesn\n"
              "1. Ahorros\n"
              "2. Corriente")
        valor = int(input())
        if valor == 1:
            self.nombre_producto = "Ahorros"
        if valor == 2:
            self.nombre_producto = "Corriente"
        self._id_producto = random.randint(1000,99999)
        self.saldo = 0

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()
            query = "INSERT INTO Producto (id_producto, nombre_producto,saldo) VALUES (%s, %s, %s)"
            values = (self._id_producto, self._nombre_producto, self._saldo)
            db.execute_query(query,values)
            db.connection.commit()
            print(f"Tipo cuenta: {self.nombre_producto}\n"
                  f"su numero de cuenta es: {self._id_producto}\n"
                  f"su saldo es: ${self.saldo}")
        except Exception as e:
            print("Error al agregar producto: ",e)
        finally:
            db.disconnect()

        #logica para ingresar tabla producto

    def mostrar_producto(self):
        for i in self.productos.items():
            print(i)
