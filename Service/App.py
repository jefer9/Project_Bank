from Domain.Persona import Persona

from Domain.Titular import Titular

class App(Titular):

    while True:
        opcion = int(input("\nBienvenido a tu sucursal virtual\n"# MODIFIQUE ESTE MENU - JUEVES
                           "\n\tElige una de las opciones\n"
                           "1 para registrarse en nuestro banco:\n"
                           "2 para ingresar a tu cuenta:\n"
                           "3 para salir de nuestro banco: "))

        if opcion == 1:
            print("\n\t*************************************")
            print("\t***** FORMULARIO DE REGISTRO ********")
            print("\t*************************************")
            persona1 = Persona(None, None, None, None,
                               None, None, None)
            persona1.crear_persona()

        elif opcion == 2:
            if persona1.autenticacion_login():
                titular_1 = Titular(None, None, None, None, None, None,
                                    None, None)
                titular_1.menu_titular(persona1.obtener_datos_persona())
            else:
                print("Autenticación fallida. Por favor, inténtelo de nuevo.")
        elif opcion == 3:
            print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
            break
