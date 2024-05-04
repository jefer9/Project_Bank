from Domain.Producto import Producto
from Domain.ConnexionBD import ConexionBD


class Titular(Producto):

    def consignar(self, ):
        num_cuenta = int(input("Numero de cuenta de destino: "))
        consignacion = int(input("Valor a consignar: "))

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()
            query = "UPDATE Producto SET saldo = saldo + %s WHERE id_producto = %s"
            values = (consignacion, num_cuenta)
            db.execute_query(query,values)
            db.connection.commit()
            print("Consignación exitosa")
        except Exception as e:
            print("Error al consignar", e)
        finally:
            db.disconnect()


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


