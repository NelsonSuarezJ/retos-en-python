"""
Escribe un programa que pueda calcular el factorial de un número dado. 
Los resultados deben imprimirse en una secuencia separada por comas en una sola línea. 
Supongamos que se suministra la siguiente entrada al programa: 8 Entonces,
la salida debería ser: 40320
"""
def factorial(fact):
    if fact==1:
        return 1
    return fact*factorial(fact-1) 

fact=int(input("introduzca el factorial: "))
print(factorial(fact))

