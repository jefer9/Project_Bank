class Persona:
    def __init__(self, id, nombre, apellido, correo, telefono, usuario, contraseña):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono
        self._usuario = usuario
        self._contraseña = contraseña

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self,_usuario):
        self._usuario =_usuario

    def crear_persona(self):
        print("Ingresa los siguientes datos: ")
        self._id = input("ID: ")
        self._nombre = input("Nombre: ")
        self._apellido = input("Apellido: ")
        self._correo = input("Correo: ")
        self._telefono = input("Telefono: ")
        self._usuario = input("Usuario: ")
        self._contraseña = input("contraseña: ")
        print("Persona creada exitosamente")

        datos_persona = {"id": self._id,
                        "Nombre": self._nombre,
                         "Apellido": self._apellido,
                         "Correo": self._correo,
                         "Telefono": self._telefono,
                         "Usuario": self._usuario,
                         "Contraseña": self._contraseña
        }

        personas[datos_persona["id"]]= datos_persona

    def autenticacion_login(self):
        usuario = input("Ingresa Usuario: ")
        contraseña = input("Ingresa la Clave: ")

        for id, datos_persona in personas.items():
            if datos_persona["Usuario"] == usuario and datos_persona["Contraseña"] == contraseña:
                print("¡Bienvenido al banco!")
                return True
        print("Usuario y/o clave incorrecta")
        return False
    def buscar_persona(self,id):
        if id in personas:
            print("Persona encontrada")
            print(personas[id])
        else:
            print("persona no encontrada")

    def modificar_persona(self,id):
        if id in personas:
            print("Ingrese los datos que deseas modificar y/o oprima enter si desea dejarlos como estan")
            nuevo_correo = input("Correo: ")
            nuevo_telefono = input("Telefono: ")
            nuevo_usuario = input("Usuario: ")

            #Verifica si los datos no estan vacios antes de actualizarlos
            if nuevo_correo:
                personas[id]["Correo"] = nuevo_correo
            if nuevo_telefono:
                personas[id]["Telefono"] = nuevo_telefono
            if nuevo_usuario:
                personas[id]["Usuario"] = nuevo_usuario

            print("Datos actualizados exitosamente")
        else:
            print("Id no encontrado")

    def eliminar_persona(self, id):
        if id in personas:
            personas.pop(id)
            print("Persona eliminada Exitosamente")
        else:
            print("persona no encontrada")

    def __str__(self):
        print = f"""
        id: {self._id},
        nombre: {self._nombre},
        apellido: {self._apellido},
        correo: {self._correo},
        telefono: {self._telefono},
        usuario: {self._usuario}
        """


#diccionario con las usuarios registrados
personas= {}





#holaaaaa
# hola de nuevo


# MODIFICACION MAURICIO
#HOLA DE NUEVO











