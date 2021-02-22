class Lector():

    def __init__(self, numero, nombre, apellidos):
        self.__numero = numero
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__moroso = False

    def numero(self):
        return self.__numero

    def nombre(self):
        return self.__nombre

    def apellidos(self):
        return self.__apellidos

    def moroso(self):
        return self.__moroso

    def set_moroso(self):
        self.__moroso = True
