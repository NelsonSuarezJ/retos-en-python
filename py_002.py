"""
Escribe un programa que pueda calcular el factorial de un número dado.
Los resultados deben imprimirse en una secuencia separada por comas en una sola línea.
Supongamos que se suministra la siguiente entrada al programa: 8 Entonces,
la salida debería ser: 40320
"""


def factorial(fact):
    """Calcula el factorial"""
    if fact == 1:
        return 1
    return fact*factorial(fact-1)


facto = int(input("introduzca el factorial: "))
print(factorial(facto))
