from Domain.Persona import Persona,personas
from Service.Asesor import Asesor
from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Credito import Credito
from Domain.Cuenta_ahorros import Cuenta_ahorros #----------REVISAR


class App:
    persona = Persona(None, None, None, None,
                      None, None, None)
    titular = Titular(None, None, None, None, None, None,
                      None, None, None)
    producto = Producto(None,None, None)
    asesor = Asesor()

    # cuenta_Ahorros = Cuenta_ahorros(None, None, None, None) #----------REVISAR


    while True:
        opcion = int(input("\nBienvenido a tu sucursal virtual\n"
                           "\n\t---------------\n"
                           "1 para registrarse en nuestro banco:\n"
                           "2 para ingresar a tu cuenta:\n"
                           "3 para salir de nuestro banco: "))

        if opcion == 1:
            print("\n\t*************************************")
            print("\t***** FORMULARIO DE REGISTRO ********")
            print("\t*************************************")

            asesor.crear_titular(personas)
        elif opcion == 2:
            if persona.autenticacion_login():
                while True:
                    print("\n\tMenu Titular\n")
                    print(f"Hola que deseas hacer hoy?")
                    opcion = int(input("\n1. Solicitar crédito:\n"
                                       "2. Para crear producto:\n"
                                       "3. lista de usuarios:\n"
                                       "4. Para salir del aplicativo:\n"
                                       "5. Consignar: "))

                    if opcion == 1:
                        credito_1 = Credito(None, None, None)
                        credito_1.solicitar_credito(personas)
                        print(personas)
                    elif opcion == 2:
                        asesor.crear_producto()
                    elif opcion == 3:
                        print(personas)
                    elif opcion == 4:
                        print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
                        break
                    elif opcion == 5:
                        producto_consignar = Producto(None, None, None)
                        # Llamar al método consignar en la instancia creada
                        producto_consignar.consignar()
                        # producto.consignar()
            else:
                print("Autenticación fallida. Por favor, inténtelo de nuevo.")
        elif opcion == 3:
            print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
            break
