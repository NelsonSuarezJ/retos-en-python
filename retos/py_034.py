"""
Defina una función que pueda generar e imprimir una lista donde los valores
sean cuadrados de números entre 1 y 20 (ambos incluidos).
"""


def lista_cuadrados():
    '''Imprime una lista con cuadrados de 1 al 20'''
    lista = [n**2 for n in range(1, 21)]
    print(lista)


lista_cuadrados()
