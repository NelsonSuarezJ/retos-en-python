'''
Defina una función que pueda aceptar un número entero como entrada e imprima el "Es un número par"
si el número es par, de lo contrario imprima "Es un número impar".
'''


def par_impar(numero):
    '''Imprime par o impar'''
    resultado = 'Es un numero par' if numero % 2 == 0 else 'Es un numero impar'
    print(resultado)


par_impar(3)
par_impar(4)
