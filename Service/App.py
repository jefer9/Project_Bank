from Domain.Persona import Persona, personas

class App:

    def autenticacion_login(self):
        usuario = input("ingresa Usuario")
        clave = input("ingresa la clave")

        for id, datos_persona in personas.items():
            if datos_persona["Usuario"] == usuario and clave == datos_persona["clave"]:
                return True
            else:
                print("Usuario y/o clave incorrecta")

    while True:
        print('\t\tHola soy tu asesor virtual\n')
        print(f"Presiona:"
                f"\n1 para registrarse en nuestro banco"
                f"\n2 para ingresar a tu cuenta"
                f"\n3 para ingresar como asesor ")
        opcion = int(input('4 para salir '))


        if opcion == 1:
            print("")
            print("*************************************")
            print("*****FORMULARIO DE REGISTRO**********")
            print("*************************************")
            persona1 = Persona(None, None, None, None, None, None)
            persona1.crear_persona()
            #actualizado
        if opcion == 2:
            print("ingreso de login")

        if opcion ==3:
            print("Gracias por visitar nuestro banco")
            break
