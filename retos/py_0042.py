"""
Escribe un programa que pueda filtrar() para hacer una lista cuyos elementos 
sean pares entre 1 y 20 (ambos incluidos).
"""

pares = filter(lambda n: n % 2 == 0, range(1, 21))

print(list(pares))
