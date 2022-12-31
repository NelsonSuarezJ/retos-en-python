"""
Escriba un programa que acepte una secuencia de números separados por comas desde
la consola y genere una lista y una tupla que contenga cada número.
Supongamos que se proporciona la siguiente entrada al programa: 34,67,55,33,12,98 Entonces,
la salida debería ser:

['34', '67', '55', '33', '12', ' 98'] ('34', '67', '55', '33', '12', '98')
"""

numeros=input("Ingrese numeros separados por coma y sin espacios: ")

lista=numeros.split(",")
tupla=tuple(lista)

print(lista,tupla)
