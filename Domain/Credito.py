from Domain.ConnexionBD import ConexionBD
from Domain.Producto import Producto
class Credito:
    def __init__(self,plazo, cantidad, cuota, id_credito):
        self.id_credito = id_credito
        self.interes = 0.03
        self._plazo = plazo
        self._cantidad = cantidad
        self._cuota = cuota

    @property
    def plazo(self):
        return self._plazo

    @plazo.setter
    def plazo(self, plazo):
        self._plazo = plazo

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    # Métodos
    def solicitar_credito(self):
        self.id_credito = input("Ingrese id credito: ")
        self._cantidad = float(input("Ingrese el monto para crédito: "))

        self._plazo = int(input("Ingrese el plazo en meses para el crédito: "))

        # Calcular la tasa de interés periódica (mensual en este caso)
        tasa_periodica = self.interes / 12

        # Calcular el número total de pagos (n)
        n = self._plazo

        # Calcular la cuota mensual utilizando la fórmula de cuota fija
        cuota_mensual = (self._cantidad * tasa_periodica * (1 + tasa_periodica) ** n) / ((1 + tasa_periodica) ** n - 1)

        # Formatear la cuota mensual para imprimir solo dos decimales
        cuota_mensual_formateada = "{:.0f}".format(cuota_mensual)



        print(f"La cuota mensual es: ${cuota_mensual_formateada}")

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()
            query = "INSERT INTO Credito(id_credito, interes, plazo, cantidad) VALUES (%s, %s, %s, %s)"
            values = (self.id_credito, self.interes, self._plazo, self.cantidad)
            db.execute_query(query,values)
            db.connection.commit()
            print("Credito Aprobado")
        except Exception as e:
            print("Error al solicitar credito")
        finally:
            db.disconnect()
