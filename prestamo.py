from lector import Lector
from libro import Libro
from datetime import datetime, timedelta

class Prestamo():

    def __init__(self, lector, libro, fecha_prestamo):
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = None

    def lector(self):
        return self.__lector

    def libro(self):
        return self.__libro

    def fecha_prestamo(self):
        return self.__fecha_prestamo

    def devuelve_libro(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion
        if self.__fecha_prestamo + timedelta(15) > self.__fecha_devolucion:
            self.__lector.set_moroso()
