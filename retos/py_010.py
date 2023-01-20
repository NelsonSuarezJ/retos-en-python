"""
Escriba un programa que acepte una secuencia de palabras separadas por espacios
en blanco como entrada e imprima las palabras después de eliminar todas las palabras
duplicadas y ordenarlas alfanuméricamente. Supongamos que se suministra la siguiente
entrada al programa: mundo hola mundo, Entonces, el resultado debe ser: hola mundo
"""

palabras = input("Ingrese palabras separadas por espacio: ").split()
order_words = list(set(palabras))
order_words.sort()

print(" ".join(order_words))
