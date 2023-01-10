"""
Debe escribir un programa para ordenar las tuplas (nombre, edad, altura) por orden
ascendente donde el nombre es cadena, la edad y la altura son números. Las tuplas son
introducidas por consola. El criterio de clasificación es: 1: Ordenar según el nombre;
2: Luego ordene según la edad; 3: Luego ordena por puntuación. La prioridad es que el
nombre > la edad > puntuación. Si se dan las siguientes tuplas como entrada al programa:
Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Entonces, la salida del programa
debe ser: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]
"""

list_datos = []
while True:
    datos = input("Ingrese datos: ")
    if not datos:
        break
    list_datos.append(tuple(datos.split(",")))

print(sorted(list_datos))
