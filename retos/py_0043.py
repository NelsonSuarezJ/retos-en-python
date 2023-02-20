"""
Escribe un programa que pueda mapear() para hacer una lista cuyos elementos 
sean cuadrados de números entre 1 y 20 (ambos incluidos).
"""

cuadrados = map(lambda n: n*n, range(1, 21))

print(list(cuadrados))
