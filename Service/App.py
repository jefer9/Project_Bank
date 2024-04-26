from Domain.Persona import Persona

from Domain.Titular import Titular


class App:
    persona = Persona(None, None, None, None,
                      None, None)
    titular = Titular(None, None, None, None, None, None,
                      None, None)

    #primer menu, inicia el programa, permite registrar un usuario y ingresar al sistema
    while True:
        opcion = int(input("\n\t Bienvenido a tu sucursal virtual\n"
                           "\nPresiona 1 para registrarse en nuestro banco:"
                           "\nPresiona 2 para ingresar a tu cuenta:"
                           "\nPresiona 3 para salir del programa: "))

        if opcion == 1:
            print("\n\t*************************************")
            print("\t***** FORMULARIO DE REGISTRO ********")
            print("\t*************************************")

            persona.crear_persona()

        elif opcion == 2:
            persona.autenticacion_login()

            titular.menu_titular()
        elif opcion == 3:
            print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
            break
