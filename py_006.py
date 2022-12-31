"""
Escriba un programa que calcule e imprima el valor de acuerdo con la fórmula
dada: Q = Raíz cuadrada de [(2 * C * D)/H] Los siguientes son los valores fijos
de C y H: C es 50. H es 30. D es la variable cuyos valores deben introducirse en
el programa en una secuencia separada por comas.
Ejemplo Supongamos que se le da al programa la siguiente secuencia de entrada
separada por comas: 100,150,180 La salida del programa debe ser: 18,22,24.
Sugerencias: Si la salida recibida está en forma decimal, debe redondearse a su
valor más cercano (por ejemplo, si la salida recibida es 26.0, debe imprimirse como 26)
"""
from math import sqrt

valores = input("Ingrese valores separados por coma y sin espacio: ")
lista_valores = valores.split(",")
lista = []

for valor in lista_valores:
    q = sqrt((2*50*int(valor))/30)
    lista.append(str(round(q)))

print(",".join(lista))
