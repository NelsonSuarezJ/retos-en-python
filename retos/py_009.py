"""
Escriba un programa que acepte la secuencia de líneas como entrada e imprima
las líneas después de poner en mayúscula todos los caracteres de la oración.
Supongamos que se suministra la siguiente entrada al programa: Hola mundo La práctica
hace al maestro Entonces, el resultado debe ser: HOLA MUNDO LA PRÁCTICA HACE AL MAESTRO
"""

list_words = []
while True:
    word = input("ingrese una palabra: ")
    if word:
        list_words.append(word.upper())
    else:
        break

print("La oracion es:", " ".join(list_words))
