from Domain.Producto import Producto
from Domain.ConnexionBD import ConexionBD
from fpdf import FPDF

class Titular(Producto):

    def consignar(self):
        num_cuenta = int(input("Numero de cuenta de destino: "))
        consignacion = int(input("Valor a consignar: "))

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()
            query = "UPDATE Producto SET saldo = saldo + %s WHERE id_producto = %s"
            values = (consignacion, num_cuenta)
            db.execute_query(query, values)
            db.connection.commit()
            print("Consignación exitosa")
        except Exception as e:
            print("Error al consignar", e)
        finally:
            db.disconnect()

        # *********** Imprimir PDF ***********

        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()

        try:
            db.connect()

            query_info_cuenta = "SELECT id_producto, saldo FROM Producto WHERE id_producto = %s"
            values_info_cuenta = (num_cuenta,)
            cuenta_info = db.execute_query(query_info_cuenta, values_info_cuenta)

            if cuenta_info:
                num_cuenta = cuenta_info[0][0]
                saldo = cuenta_info[0][1]

                pdf.image(
                'C:\\Users\\Mauricio\\Desktop\\Python_desde_cero\\Project_Bank\\Domain\\imprimir_pdf\\logo4.jpg',
                x=70, y=6,
                w=70, h=70)

                pdf.set_font('Arial', '', 20)
                pdf.text(x=72, y=70, txt='Sucursal virtual BANK')
                pdf.text(66, 90, f'Número de cuenta: {num_cuenta}')
                pdf.text(62, 120, f'Consignacion:      $ {consignacion}')
                pdf.text(62, 130, f'Saldo disponible:  $ {saldo:.0f}')
                pdf.text(x=48, y=200, txt='Gracias por preferirnos, hasta pronto!')

                print("Información de cuenta agregada al PDF.")
            else:
                print("No se encontró información de la cuenta.")

        except Exception as e:
            print("Error al obtener información de la cuenta:", e)
        finally:
            db.disconnect()

        # Guardar el PDF
        pdf.output('consginacion.pdf')

        #---------------------------------------------------------------------------------------------

    def retirar(self):
        num_cuenta = int(input("Ingrese el numero de cuenta: "))
        retiro = int(input("Ingrese el valor a retirar: "))

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            # Se obtiene el saldo actual del producto
            query_saldo_actual = "SELECT saldo FROM Producto WHERE id_producto = %s"
            values_saldo_actual = (num_cuenta,)
            saldo_actual = db.execute_query(query_saldo_actual, values_saldo_actual)

            if saldo_actual:
                saldo_actual = saldo_actual[0][0]  # Almacenamos el saldo encontrado en la variable (saldo_actual)

                # Verificacion de fondos suficientes para el retiro
                if retiro > saldo_actual:
                    print("Fondos insuficientes.")
                else:
                    # Se actualiza el saldo después del retiro
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
                saldo_actual = saldo_actual[0][0]
                print(f"Su saldo actual es: {saldo_actual:.0f}")
            else:
                print("Producto no encontrado.")

        except Exception as e:
            print("Error al consultar el saldo:", e)
        finally:
            db.disconnect()

    def transferir(self):
        num_cuenta_remitente = int(input("Ingrese el numero de cuenta remitente: "))
        num_cuenta_destino = int(input("Numero de cuenta de destino: "))
        transeferencia = int(input("Valor a transferir: "))


        print("Transeferencia exitosa")

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            query_saldo_actual = "SELECT saldo FROM Producto WHERE id_producto = %s"
            values_saldo_actual = (num_cuenta_remitente,)
            saldo_actual = db.execute_query(query_saldo_actual, values_saldo_actual)

            if saldo_actual:
                saldo_actual = saldo_actual[0][0]

                if transeferencia > saldo_actual:
                    print("Fondos insuficientes.")
                else:
                    nuevo_saldo = saldo_actual - transeferencia
                    query_actualizar_saldo = "UPDATE Producto SET saldo = %s WHERE id_producto = %s"
                    values_actualizar_saldo = (nuevo_saldo, num_cuenta_remitente)
                    db.execute_query(query_actualizar_saldo, values_actualizar_saldo)
                    db.connection.commit()

                    query = "UPDATE Producto SET saldo = saldo + %s WHERE id_producto = %s"

                    values = (transeferencia, num_cuenta_destino)
                    db.execute_query(query, values)
                    db.connection.commit()
                    print("Transferencia exitosa")

                    print(f'Nuevo saldo: ${saldo_actual:.0f}')
            else:
                print("Producto no encontrado.")

        except Exception as e:
            print("Error al realizar el retiro:", e)
        finally:
            db.disconnect()

    def consultar_BD(self):
        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            query = "SELECT * FROM Persona"
            results = db.execute_query(query)

            print('\n\t\t\t ********* Base de datos *********\n')
            for result in results:
                nombre = result[1]
                apellido = result[2]
                correo = result[3]
                telefono = result[4]
                usuario = result[5]
                contrasena = result[6]
                print(
                    f"Nombre: {nombre} Apellido: {apellido} Correo: {correo} Telefono: {telefono} Usuario: {usuario} Contraseña: {contrasena}")

        except Exception as e:
            print("No hay usuarios registrados en la base de datos:", e)
        finally:
            db.disconnect()
