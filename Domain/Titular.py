from Domain.Persona import Persona, personas

class Titular(Persona):
    def __init__(self, id, nombre, apellido, correo, telefono, usuario, contrasena, producto, clave=5):
        super().__init__(id, nombre, apellido, correo, telefono, usuario, contrasena)
        self._producto = producto

        return nombre
    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, producto):
        self._producto = producto

    #creacion de metodos

    """def crear_titular(self,):
        super().crear_persona()
        valor = int(input("Selecciona 1. Ahorros || 2. corriente"))
        self.producto = producto.productos[valor]
        self._clave = int(input("Ingresa la clave: "))
        self.personas[self._id] = self.nombre, self.apellido, self.correo, self.telefono, self.usuario, self._clave, self.producto"""

    def crear_titular(self, datos_persona):
        print("\n\tCreación del producto")
        producto = int(input("\nSelecciona el tipo de cuenta:\n"
                             "1. Ahorros:\n"
                             "2. Corriente: "))

        if producto == 1:
            self.producto = "Ahorros"
            datos_persona["Producto"] = self.producto
        elif producto == 2:
            self.producto = "Corriente"
            datos_persona["Producto"] = self.producto
        else:
            print("Opción no válida")

        self._clave = input("Ingresa la clave: ")
        datos_persona["Clave"] = self._clave
        # print(datos_persona)
        # Agregue la logica para imprimir el diccionario con los nuevos datos obtenidos en este metodo y la informacion necesaria "creo yo"
        print('\n\t***Datos del usuario***')
        print(
            f"\nTipo de cuenta: {datos_persona['Producto']} \nClave: {datos_persona['Clave']}\nNombre: {datos_persona['Nombre']} {datos_persona['Apellido']}\nDocumento: {datos_persona['id']}")

    def __str__(self):
        return f"{super().__str__()} producto: {self.producto}"

    def menu_titular(self, datos_persona):
        while True:
            print("\n\tMenu Titular\n")
            print(f"Hola {datos_persona['Nombre']} que deseas hacer hoy?")
            opcion = int(input("\n1. Solicitar crédito:\n"
                               "2. Para crear producto:\n"
                               "3. Para salir del aplicativo: "))

            if opcion == 1:
                print("Lógica para la solicitud del crédito")
            elif opcion == 2:
                self.crear_titular(datos_persona)# Le pase los datos de la persona como parametro
            elif opcion == 3:
                print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
                break
