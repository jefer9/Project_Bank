from Domain.Persona import Persona, personas

class Titular(Persona):
    def __init__(self, id, nombre, apellido, correo, telefono, usuario, contraseña, producto, clave=5):
        super().__init__(id, nombre, apellido, correo, telefono, usuario, contraseña)
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

    def crear_titular(self):
        print("Creación del producto")
        producto = int(input("1. Cuenta de ahorros\n"
                             "2. Cuenta corriente\n"
                             "Selecciona el tipo de cuenta: "))

        if producto == 1:
            self.producto = "Cuenta de ahorros"
            personas["Producto"] = self.producto
        elif producto == 2:
            self.producto = "Cuenta corriente"
            personas["Producto"] = self.producto
        else:
            print("Opción no válida")

        self._clave = input("Ingresa la clave: ")
        personas["Clave"] = self._clave
        print(personas)

    def __str__(self):
        return f"{super().__str__()} producto: {self.producto}"



    def menu_titular(self):
        while True:
            print("\n\tMenu Titular\n")
            print(f"Hola {personas['Nombre']} presiona alguna de las opciones")
            opcion = int(input("1. Solicitar crédito:\n"
                               "2. Para crear producto:\n"
                               "3. Para salir del aplicativo: "))

            if opcion == 1:
                print("Lógica para la solicitud del crédito")
            elif opcion == 2:
                self.crear_titular()
            elif opcion == 3:
                print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
                break
