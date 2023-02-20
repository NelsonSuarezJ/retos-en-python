"""
Escriba un programa que pueda filtrar números pares en una lista utilizando la función de filtro. 
La lista es: [1,2,3,4,5,6,7,8,9,10].
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)
