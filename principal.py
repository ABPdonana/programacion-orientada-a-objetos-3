from prestamo import Prestamo
from libro import Libro
from lector import Lector
from datetime import datetime

lector1 = Lector(0, "Ana", "Garcia")
lector2 = Lector(1, "Roberto", "Sanchez")
libro1 = Libro(0, "El camino", "Miguel Delibes", "Misco")
libro2 =Libro(1, "")
libro3 =
prestamo1 = Prestamo(lector1, libro1, datetime(2021, 2, 22))
print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')
prestamo1.devuelve_libro(datetime(2021, 4, 22))
print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')
