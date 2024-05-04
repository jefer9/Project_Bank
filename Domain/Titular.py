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
        num_cuenta = int(input("Ingrese número de cuenta: "))
        retiro = int(input("Ingrese el valor a retirar: "))

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            # Consulta para obtener el saldo actual del producto
            consulta_saldo = "SELECT saldo FROM Producto WHERE id_producto = %s"
            saldo = db.execute_query(consulta_saldo, (num_cuenta,))

            if not saldo:
                print("Número de cuenta no válido.")
                return

            saldo_actual = saldo[0][0]

            # Verificar si el saldo es suficiente para el retiro
            if retiro > saldo_actual:
                print("Fondos insuficientes")
            else:
                # Consulta para actualizar el saldo en la base de datos
                query = "UPDATE Producto SET saldo = saldo - %s WHERE id_producto = %s"
                values = (retiro, num_cuenta)
                db.execute_query(query, values)
                db.connection.commit()
                print("Retiro completado con éxito")
        except Exception as e:
            print("Error en el retiro:", e)
        finally:
            db.disconnect()

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


