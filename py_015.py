"""
Escriba un programa que calcule el valor de a+aa+aaa+aaaa con un dígito
dado como valor de a. Supongamos que se suministra la siguiente entrada
al programa: 9 Entonces, el resultado debe ser: 11106
"""

digito = int(input("Ingrese un digito: "))
suma=digito

for i in range(2, 5):
    num = str(digito)*i
    suma+=int(num)

print(suma)
