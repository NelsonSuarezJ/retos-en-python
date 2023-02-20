"""
Escriba un programa que acepte una cadena como entrada para imprimir "Yes" 
si la cadena es "yes" o "YES" o "Yes", de lo contrario imprima "No".
"""

entrada = input("Ingrese la palabra: ").lower()

if entrada == "yes":
    print("Yes")
else:
    print("No")
