"""
Defina una clase, que tenga un parámetro class y tenga un mismo parámetro de instancia.
"""


class Persona:
    """Clase Persona"""
    nombre = "Persona"

    def __init__(self, nombre=None) -> None:
        self.nombre = nombre


juan = Persona("Juan")
print(f"El nombre de la {Persona.nombre} es {juan.nombre}")

pedro = Persona()
pedro.nombre = "Pedro"
print(f"El nombre de la {Persona.nombre} es {pedro.nombre}")
