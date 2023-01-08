"""
Escriba un programa que calcule el importe neto de una cuenta bancaria basándose
en un registro de transacciones a partir de la entrada de la consola. El formato
del registro de transacciones se muestra de la siguiente manera: D 100 W 200
D significa depósito, mientras que W significa retiro. Supongamos que se suministra
la siguiente entrada al programa: D 300 D 300 W 200 D 100 Entonces, el resultado
debe ser: 500
"""

valores = input("Ingrese los registros: ").split(" ")
importe = 0

for imp in range(0, len(valores), 2):
    if valores[imp] == "D":
        importe += int(valores[imp+1])
    elif valores[imp] == "W":
        importe -= int(valores[imp+1])

print("El importe es: ", importe)
