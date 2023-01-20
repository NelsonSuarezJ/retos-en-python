"""
Use una comprensión de lista para cuadrar cada número impar en una lista.
La lista se introduce mediante una secuencia de números separados por comas.
Supongamos que se suministra la siguiente entrada al programa: 1,2,3,4,5,6,7,8,9
Entonces, el resultado debe ser: 1,3,5,7,9
"""

valores = input("Ingrese numeros separados por comas: ").split(",")

impares = [n for n in valores if int(n) % 2 != 0]
print(",".join(impares))
