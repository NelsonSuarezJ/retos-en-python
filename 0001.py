"""
Escribe un programa que encuentre todos los números divisibles por 7 pero que no sean múltiplos de 5, 
entre 2000 y 3200 (ambos incluidos). 
Los números obtenidos deben imprimirse en una secuencia separada por comas en una sola línea.
"""

list = []

for numero in range(2000, 3201):

    if numero % 7 == 0:
        if numero % 5 != 0:
            list.append(str(numero))

print(','.join(list))
