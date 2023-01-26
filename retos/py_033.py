"""
Defina una función que pueda generar un diccionario donde las claves sean números entre 1 y 20
(ambos incluidos) y los valores sean cuadrados de claves. La función solo debe imprimir los valores.
"""


def cuadrados():
    '''Devuelve los valores del diccionario'''
    diccionario = {}
    for numero in range(1,21):
        diccionario[numero]=numero**2

    valores=diccionario.values()
    return list(valores)


print(cuadrados())
