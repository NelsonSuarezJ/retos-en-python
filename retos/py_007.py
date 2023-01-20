"""
Escriba un programa que tome 2 dígitos, X, Y como entrada y genere una matriz de 2 dimensiones.
El valor del elemento en la i-ésima fila y j-ésima columna de la matriz debe ser i*j.
Nota: i=0,1.., X-1; j=0,1,¡Y-1. Ejemplo Supongamos que se dan las siguientes entradas al
programa: 3,5 Entonces, la salida del programa debe ser: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4],
[0, 2, 4, 6, 8]]
"""

matriz = input("Ingrese la matriz separada por coma: ").split(",")
int_matriz = list(map(int, matriz))
x = int_matriz[0]
y = int_matriz[1]
lista = [[0 for col in range(y)] for row in range(x)]

for fila in range(x):
    for columna in range(y):
        lista[fila][columna] = fila*columna

print(lista)
