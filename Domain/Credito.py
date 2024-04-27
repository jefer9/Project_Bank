
class Credito:
    def __init__(self,plazo, cantidad, cuota):
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
    def solicitar_credito(self, CREDITOa):
        self._cantidad = float(input("Ingrese el monto para crédito: "))
        datos_persona["Cantidad credito"] = self._cantidad

        self._plazo = int(input("Ingrese el plazo en meses para el crédito: "))
        datos_persona["Plazo"] = self._plazo

        # Calcular la tasa de interés periódica (mensual en este caso)
        tasa_periodica = self.interes / 12

        # Calcular el número total de pagos (n)
        n = self._plazo

        # Calcular la cuota mensual utilizando la fórmula de cuota fija
        cuota_mensual = (self._cantidad * tasa_periodica * (1 + tasa_periodica) ** n) / ((1 + tasa_periodica) ** n - 1)

        # Formatear la cuota mensual para imprimir solo dos decimales
        cuota_mensual_formateada = "{:.2f}".format(cuota_mensual)

        # Agregar la cuota mensual al diccionario
        datos_persona["Cuota Mensual"] = cuota_mensual_formateada

        print(f"La cuota mensual es: ${cuota_mensual_formateada}")
        print(datos_persona)











