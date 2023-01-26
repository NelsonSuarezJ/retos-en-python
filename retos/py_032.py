"""
Defina una función que pueda imprimir un diccionario donde las claves son números
entre 1 y 3 (ambos incluidos) y los valores son cuadrados de las claves.
"""

def cuadrados():
    '''Devuelve un diccionario con los cuadrados de sus claves'''
    lista_cuadrados={}
    for numero in range(1,4):
        lista_cuadrados[numero]=numero*numero
    return lista_cuadrados

print(cuadrados())
