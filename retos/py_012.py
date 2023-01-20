"""
Escriba un programa, que encontrará todos esos números entre 1000 y 3000
(ambos incluidos) de modo que cada dígito del número sea un número par.
Los números obtenidos deben imprimirse en una secuencia separada por comas
en una sola línea.
"""

list_number = []

def espar(num):
    """Retorna True si el numero es par"""
    return int(num) % 2 == 0


for numero in range(1000, 3001):
    c = str(numero)
    if espar(c[0]) and espar(c[1]) and espar(c[2]) and espar(c[3]):
        list_number.append(c)

print(",".join(list_number))
