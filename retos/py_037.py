"""
Defina una función que pueda generar e imprimir una tupla donde el valor sea cuadrado
de números entre 1 y 20 (ambos incluidos).
"""

def genera_cuadrados():
    '''Imprime una tupla de cuadrados'''
    lista = []
    for numero in range(1, 21):
        lista.append(numero**2)
    print(tuple(lista))

genera_cuadrados()
