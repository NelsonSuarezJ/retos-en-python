"""
Escriba un programa que acepte una secuencia de palabras separadas por comas como entrada
e imprima las palabras en una secuencia separada por comas después de ordenarlas
alfabéticamente. Supongamos que se suministra la siguiente entrada al programa: sin,
hola, bolso, mundo Entonces, el resultado debe ser: bolso, hola, sin, mundo
"""

palabras=input("Ingrese palabras separadas por coma: ").split(",")
palabras.sort()

print(",".join(palabras))
