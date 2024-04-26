from Domain.Persona import Persona
from Service.Asesor import Asesor
from Domain.Titular import Titular
from Domain.Producto import Producto


class App:
    persona = Persona(None, None, None, None,
                      None, None, None)
    titular = Titular(None, None, None, None, None, None,
                      None, None, None)
    producto = Producto(None,None)


    while True:
        opcion = int(input("\nBienvenido a tu sucursal virtual\n"  # MODIFIQUE ESTE MENU - JUEVES
                           "\n\t---------------\n"
                           "1 para registrarse en nuestro banco:\n"
                           "2 para ingresar a tu cuenta:\n"
                           "3 para salir de nuestro banco: "))

        if opcion == 1:
            print("\n\t*************************************")
            print("\t***** FORMULARIO DE REGISTRO ********")
            print("\t*************************************")

            asesor = Asesor()
            asesor.crear_titular()

        elif opcion == 2:
            if persona.autenticacion_login():

                titular.menu_titular(persona.obtener_datos_persona())
                #agregar menu despues de que inicie sesion correctamente

            else:
                print("Autenticación fallida. Por favor, inténtelo de nuevo.")
        elif opcion == 3:
            print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
            break
