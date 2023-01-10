"""
Escriba un programa para calcular la frecuencia de las palabras de la entrada.
La salida debe salir después de ordenar la clave alfanuméricamente. Supongamos
que se suministra la siguiente entrada al programa: Nuevo en Python o eligiendo
entre Python 2 y Python 3? Lea Python 2 o Python 3. Entonces, el resultado debe
ser: 2:2 3.:1 3?:1 Nuevo:1 Python:5 Lea:1 y:1 entre:1 eligiendo:1 o:2 en:1
"""
contador = []
frase = input("Ingrese una frase: ").split(" ")

for palabra in set(frase):
    par = [palabra, frase.count(palabra)]
    contador.append(par)

contador.sort()

for word in contador:
    print(f"{word[0]}:{word[1]}",end=" ")
