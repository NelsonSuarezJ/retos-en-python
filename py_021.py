"""
Un robot se mueve en un plano a partir del punto original (0,0). El robot puede
moverse hacia UP, DOWN, LEFT y RIGHT con pasos determinados. El rastro
del movimiento del robot se muestra de la siguiente manera:
UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ Los números después de la dirección son pasos.
Por favor, escriba un programa para calcular la distancia desde la posición actual
después de una secuencia de movimiento y punto original. Si la distancia es flotante,
simplemente imprima el entero más cercano. Ejemplo: Si se dan las siguientes tuplas como
entrada al programa: UP 5 DOWN 3 LEFT 3 RIGHT 2 Entonces, la salida del
programa debe ser: 2
"""
from math import sqrt

xy = [0, 0]
while True:
    coordenada = input("Ingrese la coordenada:")
    if not coordenada:
        break
    coordenada = coordenada.split(" ")
    if coordenada[0] == "UP":
        xy[1] += int(coordenada[1])
    elif coordenada[0] == "DOWN":
        xy[1] -= int(coordenada[1])
    elif coordenada[0] == "RIGHT":
        xy[0] += int(coordenada[1])
    elif coordenada[0] == "LEFT":
        xy[0] -= int(coordenada[1])

hipotenusa = round(sqrt(xy[0]**2+xy[1]**2))
print("La distancia desde (0,0) es", hipotenusa)
