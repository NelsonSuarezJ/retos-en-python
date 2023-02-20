"""
Escribe un programa que pueda mapear() para hacer una lista cuyos elementos sean 
cuadrados de elementos en [1,2,3,4,5,6,7,8,9,10].
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda n: n*n, numeros))

print(cuadrados)
