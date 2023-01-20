"""
Escriba un programa que acepte una secuencia de números binarios de 4 dígitos
separados por comas como entrada y luego verifique si son divisibles por 5 o no.
Los números que son divisibles por 5 deben imprimirse en una secuencia separada
por comas. Ejemplo: 0100,0011,1010,1001 Entonces la salida debe ser: 1010
"""

valores = input("Ingrese numeros binarios separados por coma: ").split(",")
divfive = []

for numero in valores:
    if int(numero, 2) % 5 == 0:
        divfive.append(numero)

print(",".join(divfive))
