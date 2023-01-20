"""
Escriba una funcion que calcule el cuadrado de un numero y muestre su documentacion.
"""


def cuadrado(numero):
    """Retorna el cuadrado de un numero"""
    return numero**2


print(cuadrado(4))
print(cuadrado(6))
print(cuadrado.__doc__)
