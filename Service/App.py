from Domain.Persona import Persona

from Domain.Titular import Titular

class App:


    while True:
        opcion = int(input("Presiona 1 para registrarse en nuestro banco"
                           "\nPresiona 2 para ingresar a tu cuenta"
                           "\nPresiona 3 para salir de nuestro banco: "))

        if opcion == 1:
            print("\n*************************************")
            print("***** FORMULARIO DE REGISTRO ********")
            print("*************************************")
            persona1 = Persona(None, None, None, None,
                               None, None, None)
            persona1.crear_persona()

        elif opcion == 2:
            persona1.autenticacion_login()
            titular_1 = Titular(None, None,None,None,None,None,
                                None,None)
            titular_1.menu_titular()
        elif opcion == 3:
            print("Gracias por visitar nuestro banco")
            break


