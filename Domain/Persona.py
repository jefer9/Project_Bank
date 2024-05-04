from Domain.ConnexionBD import ConexionBD

class Persona:

    def __init__(self, id, nombre, apellido, correo, telefono, usuario, contrasena):

        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono
        self._usuario = usuario
        self._contrasena = contrasena

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
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    def crear_persona(self):
        print("FORMULARIO DE REGISTRO")
        print("Ingresa los siguientes datos: ")
        self._id = input("ID: ")
        self._nombre = input("Nombre: ")
        self._apellido = input("Apellido: ")
        self._correo = input("Correo: ")
        self._telefono = input("Telefono: ")
        self._usuario = input("Usuario: ")
        self._contrasena = input("Contraseña: ")

        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()
            query = "INSERT INTO Persona (id, nombre, apellido, correo, telefono, usuario, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (
            self._id, self._nombre, self._apellido, self._correo, self._telefono, self._usuario, self._contrasena)
            db.execute_query(query, values)
            db.connection.commit()  # Confirmar la transacción
            print("Persona agregada exitosamente")
        except Exception as e:
            print("Error al agregar persona:", e)
        finally:
            db.disconnect()

    def autenticacion_login(self):
        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            while True:
                usuario = input("\nIngresa el usuario: ")
                contrasena = input("Ingresa la contraseña: ")

                query = "SELECT * FROM Persona WHERE usuario = %s AND contraseña = %s"
                values = (usuario, contrasena)
                result = db.execute_query(query, values)

                if result:
                    print("¡Bienvenido al banco!")
                    return True
                else:
                    print("\nUsuario y/o Contraseña incorrecta\n")

        except Exception as e:
            print("Error en la autenticación:", e)
        finally:
            db.disconnect()

    def buscar_persona(self):
        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            id = input("Ingresa el ID de la persona que deseas buscar: ")

            query = "SELECT * FROM Persona WHERE id = %s"
            values = (id,)
            result = db.execute_query(query, values)

            if result:
                print("Persona encontrada:")
                for row in result:
                    print(row)  # Imprime cada fila de datos
            else:
                print("Persona no encontrada")

        except Exception as e:
            print("Error al buscar la persona:", e)
        finally:
            db.disconnect()

    def modificar_persona(self):
        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            id = input("Ingresa el ID de la persona que deseas modificar: ")

            query_select = "SELECT * FROM Persona WHERE id = %s"
            values_select = (id,)
            result_select = db.execute_query(query_select, values_select)

            if result_select:
                print("Persona encontrada. Ingresa los nuevos datos:")

                nuevo_correo = input("Nuevo correo: ")
                nuevo_telefono = input("Nuevo telefono: ")

                # Verifica si los datos no están vacíos antes de actualizarlos
                if nuevo_correo:
                    query_update_correo = "UPDATE Persona SET correo = %s WHERE id = %s"
                    values_update_correo = (nuevo_correo, id)
                    db.execute_query(query_update_correo, values_update_correo)

                if nuevo_telefono:
                    query_update_telefono = "UPDATE Persona SET telefono = %s WHERE id = %s"
                    values_update_telefono = (nuevo_telefono, id)
                    db.execute_query(query_update_telefono, values_update_telefono)

                print("Datos actualizados exitosamente")
            else:
                print("ID no encontrado")

        except Exception as e:
            print("Error al modificar la persona:", e)
        finally:
            db.disconnect()

    def eliminar_persona(self):
        try:
            db = ConexionBD(host="localhost", port="3306", user="root", passwd="", database="projectbank")
            db.connect()

            id = input("Ingresa el ID de la persona que deseas eliminar: ")

            query_select = "SELECT * FROM Persona WHERE id = %s"
            values_select = (id,)
            result_select = db.execute_query(query_select, values_select)

            if result_select:
                confirmacion = input("¿Estás seguro de que deseas eliminar esta persona? (S/N): ")
                if confirmacion.upper() == "S":
                    query_delete = "DELETE FROM Persona WHERE id = %s"
                    values_delete = (id,)
                    db.execute_query(query_delete, values_delete)
                    print("Persona eliminada exitosamente")
                else:
                    print("Operación cancelada")
            else:
                print("ID no encontrado")

        except Exception as e:
            print("Error al eliminar la persona:", e)
        finally:
            db.disconnect()

    # Cree un nuevo metodo para retornar los datos
    def obtener_datos_persona(self, datos_persona):
        return datos_persona

    def __str__(self):
        return f"""
        id: {self._id},
        nombre: {self._nombre},
        apellido: {self._apellido},
        correo: {self._correo},
        telefono: {self._telefono},
        """

personas = {}
