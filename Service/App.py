from Domain.Persona import Persona,personas
from Service.Asesor import Asesor
from Domain.Titular import Titular
from Domain.Producto import Producto
from Domain.Credito import Credito
from Domain.Cuenta_ahorros import Cuenta_ahorros #----------REVISAR

class App:
    persona = Persona(None, None, None, None,
                      None, None, None)
    #titular = Titular(None, None, None, None, None, None,
                      #None, None, None)
    producto = Producto(None,None,
                        None, None,None,None, None,None,None, None)
    asesor = Asesor()

    # cuenta_Ahorros = Cuenta_ahorros(None, None, None, None) #----------REVISAR

    while True:
        opcion = int(input("\nBienvenido a tu sucursal virtual\n"
                           "\n\t---------------\n"
                           "1. Asesor virtual\n"
                           "2. Iniciar sesion\n"
                           "3 Salir. "))

        if opcion == 1:
            while True:
                opc = int(input("\nBienvenido a tu sucursal virtual\n"
                                "1. Registrarse\n"
                                "2. Crear Producto\n"
                                "3. Buscar Usuario\n"
                                "4. Modificar Usuario\n"
                                "5. Eliminar Usuario\n"
                                "6. Salir\n"))
                if opc == 1:
                    asesor.crear_persona()
                if opc == 2:
                    asesor.crear_producto()
                if opc == 3:
                    asesor.buscar_persona()
                if opc == 4:
                    asesor.modificar_persona()
                if opc == 5:
                    asesor.eliminar_persona()
                if opc == 6:
                    print("\n Gracias por visitar nuestra asesoria virtual")
                    break


        elif opcion == 2:
            if persona.autenticacion_login():
                while True:
                    print("\n\tMenu Titular\n")
                    print(f"¿Hola que deseas hacer hoy?")
                    opcion = int(input("\n1. Solicitar crédito:\n"
                                       "2. Crear producto:\n"
                                       "3. Operaciones de cuenta\n"
                                       "4. Para salir del aplicativo:\n"))

                    if opcion == 1:
                        credito_1 = Credito(None, None, None,None)
                        credito_1.solicitar_credito()
                        print(personas)
                    elif opcion == 2:
                        asesor.crear_producto()
                    elif opcion == 3:
                        while True:
                            print("\nEscoge la operacion de la cuenta\n")
                            opc = int(input(
                                            "1. Consignar\n"
                                            "2. Retirar\n"
                                            "3. Consultar saldo\n"
                                            "4. Transferir"))
                            if opc == 1:
                                titular1 = Titular(None, None, None, None, None, None, None, None, None, None)
                                titular1.consignar()
                            if opc == 2:
                                titular2 = Titular(None, None, None, None, None, None, None, None, None, None)
                                titular2.retirar()
                            if opc == 3:
                                titular3 = Titular(None, None, None, None, None, None, None, None, None, None)
                                titular3.consultar_saldo()
                            if opc == 4:
                                titular4 = Titular(None, None, None, None, None, None, None, None, None, None)
                                titular4.transferir()
                    elif opcion == 4:
                        print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
                        break

            else:
                print("Autenticación fallida. Por favor, inténtelo de nuevo.")
        elif opcion == 3:
            print("\n\tGracias por visitar nuestra sucursal virtual, hasta pronto!")
            break
