from lector import Lector
from libro import Libro
from datetime import datetime, timedelta

class Prestamo():

    __libro_prestamos = {}

    def __init__(self, lector, libro, fecha_prestamo):
        if libro.codigo() in Prestamo.__libro_prestamos:
            raise NameError("Libro ya alquilado")
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = None
        Prestamo.__libro_prestamos[self.__libro.codigo()] = self.__libro.titulo()

    def lector(self):
        return self.__lector

    def libro(self):
        return self.__libro

    def fecha_prestamo(self):
        return self.__fecha_prestamo

    def devuelve_libro(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion
        if self.__fecha_prestamo + timedelta(15) < self.__fecha_devolucion:
            self.__lector.set_moroso()
        del Prestamo.__libro_prestamos[self.__libro.codigo()]
