
class App:

    while True:
        opcion = int(input(f"Presiona 1 para registrarse en nuestro banco"
                    f" \n presiona 2 para ingresar a tu cuenta"
                    f"\n presiona 3 para ingresar como asesor "
                    f"\n presiona 4 para salir "))


        if opcion == 1:
            print("registro persona")
        if opcion == 2:
            print("ingreso de login")
        if opcion == 3:
            print("clase asesor")
        if opcion ==4:
            print("Gracias por visitar nuestro banco")
            break
