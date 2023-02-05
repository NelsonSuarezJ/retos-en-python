"""
Defina una función que pueda generar una lista donde los valores sean cuadrados de números entre
1 y 20 (ambos incluidos). Luego, la función debe imprimir los últimos 5 elementos de la lista.
"""


def cuadrados():
    '''Imprime los ultimos 5 cuadrados de una lista de 20'''
    lista_cuadrados = [n**2 for n in range(1, 21)]
    print(lista_cuadrados[-5:])

cuadrados()
