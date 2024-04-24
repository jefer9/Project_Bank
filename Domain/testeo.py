from Domain.Credito import Credito
from Domain.Cuenta_ahorros import Cuenta_ahorros
from Domain.Cuenta_corriente import Cuenta_corriente
from Domain.Persona import Persona
from Domain.Producto import Producto
from Domain.Titular import Titular

class testeo:

    # instanciamiento de metodos para testear
    persona_1 = Persona(None, None, None, None, None, None)

    persona_1.crear_persona()

    id_persona = input("eliminar id")
    persona_1.eliminar_persona(id_persona)

