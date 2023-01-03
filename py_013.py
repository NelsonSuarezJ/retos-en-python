"""
Escribe un programa que acepte una oración y calcula el número de letras y dígitos.
Supongamos que se suministra la siguiente entrada al programa: ¡Hola mundo! 123.
Entonces, el resultado debe ser: LETRAS 9 DÍGITOS 3
"""

frase = input("Ingrese una frase: ")
cuenta_letras, cuenta_digitos = 0,0

for i in frase:
    if i.isalpha():
        cuenta_letras += 1
    elif i.isdecimal():
        cuenta_digitos += 1

print(f"LETRAS {cuenta_letras} DIGITOS {cuenta_digitos}")
