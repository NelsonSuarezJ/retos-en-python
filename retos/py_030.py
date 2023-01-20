'''
Defina una función que pueda aceptar dos cadenas como entrada e imprima la cadena con la longitud
máxima en la consola. Si dos cadenas tienen la misma longitud, entonces la función debe imprimir
todas las cadenas línea por línea.
'''


def long_cadena(cad1, cad2):
    '''Imprime la cadena mas larga'''
    len_cad1 = len(cad1)
    len_cad2 = len(cad2)
    if len_cad1 > len_cad2:
        print(cad1)
    elif len_cad2 > len_cad1:
        print(cad2)
    else:
        print(cad1)
        print(cad2)


long_cadena('hola', 'mundo')
long_cadena('longitud', 'largo')
long_cadena('uno', 'dos')
