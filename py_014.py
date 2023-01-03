"""
Escriba un programa que acepte una oración y calcule el número de letras
mayúsculas y minúsculas. Supongamos que se suministra la siguiente entrada al
programa: ¡Hola mundo! Entonces, el resultado debe ser: MAYÚSCULAS 1 MINÚSCULAS 8
"""

frase = input("Ingrese una frase: ")
contador = dict(mayus=0, minus=0)

for letra in frase:
    if letra.islower():
        contador["minus"]+=1
    elif letra.isupper():
        contador["mayus"]+=1

print("MAYUSCULAS", contador["mayus"])
print("MINUSCULAS", contador["minus"])
