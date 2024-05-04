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
        num_cuenta = int(input("Ingrese el numero de cuenta: "))
        retiro = int(input("Ingrese el valor a retirar: "))

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            # Obtener el saldo actual del producto
            query_saldo_actual = "SELECT saldo FROM Producto WHERE id_producto = %s"
            values_saldo_actual = (num_cuenta,)
            saldo_actual = db.execute_query(query_saldo_actual, values_saldo_actual)

            if saldo_actual:
                saldo_actual = saldo_actual[0][0]  # Seleccionamos el saldo de la lista de resultados

                # Verificar si hay fondos suficientes para el retiro
                if retiro > saldo_actual:
                    print("Fondos insuficientes.")
                else:
                    # Actualizar el saldo después del retiro
                    nuevo_saldo = saldo_actual - retiro
                    query_actualizar_saldo = "UPDATE Producto SET saldo = %s WHERE id_producto = %s"
                    values_actualizar_saldo = (nuevo_saldo, num_cuenta)
                    db.execute_query(query_actualizar_saldo, values_actualizar_saldo)
                    db.connection.commit()
                    print("Retiro exitoso.")
                    print(f'Nuevo saldo: $ {nuevo_saldo}')
            else:
                print("Producto no encontrado.")

        except Exception as e:
            print("Error al realizar el retiro:", e)
        finally:
            db.disconnect()

    def consultar_saldo(self):
        num_cuenta = int(input("Ingrese el numero de cuenta: "))

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            query_saldo_actual = "SELECT saldo FROM Producto WHERE id_producto = %s"
            values_saldo_actual = (num_cuenta,)
            saldo_actual = db.execute_query(query_saldo_actual, values_saldo_actual)

            if saldo_actual:
                saldo_actual = saldo_actual[0][0]  # Seleccionamos el saldo de la lista de resultados
                print(f"Su saldo actual es: {saldo_actual:.0f}")
            else:
                print("Producto no encontrado.")

        except Exception as e:
            print("Error al consultar el saldo:", e)
        finally:
            db.disconnect()




    def transferir(self):
        transeferencia = int(input("Valor a transferir: "))
        num_cuenta_destino = int(input("Numero de cuenta de destino: "))

        if transeferencia > self._saldo:
            print("fondos insuficientes")
        else:
            # Aqui se hace la suma al numero de cuenta destinatario
            print("Transeferencia exitosa")
