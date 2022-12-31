"""
Defina una clase que tenga al menos dos métodos: getString: para obtener una cadena
de la entrada de la consola printString: para imprimir la cadena en mayúsculas.
También incluya una función de prueba simple para probar los métodos de clase.
"""


class Py005:
    """Clase con 3 funciones"""

    def __init__(self) -> None:
        self.entrada = ""

    def get_string(self):
        """Metodo que solicita una cadena por consola"""
        self.entrada = input("Ingrese una cadena: ")

    def print_string(self):
        """Metodo que convierte la cadena a mayusculas"""
        print(self.entrada.upper())


def prueba(str_obj):
    """Funcion que prueba los metodos de la clase"""
    str_obj.get_string()
    str_obj.print_string()


Objeto = Py005()
prueba(Objeto)
