import mysql.connector


class ConexionBD:
    def __init__(self, host, port, user, passwd, database):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connection = None

    def connect(self):
    #al utilizar este metodo se debe de poner el host y el port de la bd que estemos utilizando
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                passwd=self.passwd,
                database=self.database
            )
            # print("Conexión a la base de datos Exitosa")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos", err)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            # print("Conexion cerrada")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            # print("Consulta ejecutada exitosamente")
            if query.lower().startswith('select'):
                result = cursor.fetchall()
                return result
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta", err)
            return None
        finally:
            cursor.close()
