"""
Defina una clase con un generador que pueda iterar los números,
que son divisibles por 7, entre un rango dado 0 y n
"""


def divisibles(limite):
    """Retorna los numeros divisibles por 7 con un generador"""
    for numero in range(limite):
        if numero % 7 == 0:
            yield numero


for n in divisibles(100):
    print(n)
