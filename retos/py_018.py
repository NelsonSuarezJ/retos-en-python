"""
Un sitio web requiere que los usuarios ingresen el nombre de usuario y la
contraseña para registrarse. Escriba un programa para verificar la validez de
la entrada de contraseña por parte de los usuarios. Los siguientes son los criterios
para verificar la contraseña:

Al menos 1 letra entre [a-z]
Al menos 1 número entre [0-9]
Al menos 1 letra entre [A-Z]
Al menos 1 carácter de [$#@]
Longitud mínima de la contraseña de transacción: 6
Longitud máxima de la contraseña de transacción: 12
Su programa debe aceptar una secuencia de contraseñas separadas por comas y las
verificará de acuerdo con los criterios anteriores. Las contraseñas que coincidan
con los criterios deben imprimirse, cada una separada por una coma. Ejemplo Si se
proporcionan las siguientes contraseñas como entrada al programa: ABd1234@1,a F1#,2w3E*,
2We3345 Entonces, la salida del programa debe ser: ABd1234@1
"""
import re
pw_correct_sin = []
pw_correct_con = []


def sin_regex(word):
    """Retorna lista de contraseñas que cumplen los criterios sin usar Regex"""
    mayus, minus, num, char = 0, 0, 0, 0
    for letter in word:
        if letter.isupper():
            mayus += 1
        elif letter.islower():
            minus += 1
        elif letter.isdigit():
            num += 1
        elif letter in ("#", "$", "@"):
            char += 1
        else:
            pass

    if mayus > 0 and minus > 0 and num > 0 and char > 0:
        pw_correct_sin.append(word)


def con_regex(word):
    """Retorna lista de contraseñas que cumplen los criterios usando Regex """
    if not re.search("[a-z]", word):
        return
    if not re.search("[A-Z]", word):
        return
    if not re.search("[0-9]", word):
        return
    if not re.search("[$#@]", word):
        return
    pw_correct_con.append(word)


passwords = input("Ingrese contraseñas separadas por coma:").split(",")

for pw in passwords:
    lon = len(pw)
    if lon < 6 or lon > 12:
        continue
    sin_regex(pw)
    con_regex(pw)

print("Sin REGEX:", ",".join(pw_correct_sin))
print("Con REGEX:", ",".join(pw_correct_con))
