from prestamo import Prestamo
from libro import Libro
from lector import Lector
from datetime import date, datetime

#Crear datos
lector1 = Lector(0, "Ana", "Garcia")
lector2 = Lector(1, "Roberto", "Sanchez")
libro1 = Libro(0, "El camino", "Miguel Delibes", "Misco")
libro2 = Libro(1, "Cien años de soledad", "Gabriel Garcia Marquez", "Misco")
libro3 = Libro(2, "Rayuela", "Julio Cortazar", "Misco")
prestamo1 = Prestamo(lector1, libro1, datetime(2021, 2, 22))
prestamo2 = Prestamo(lector1, libro2, datetime(2021, 2, 23))
prestamo3 = Prestamo(lector2, libro3, datetime(2021, 2, 23))

#Devolver un libro prestado con menos de 15 dias
print(f'El lector {lector2.nombre()} {lector2.apellidos()} es moroso: {lector2.moroso()}')
prestamo3.devuelve_libro(datetime(2021, 2, 24))
print(f'El lector {lector2.nombre()} {lector2.apellidos()} es moroso: {lector2.moroso()}')

#Prestar un libro ya prestado
#prestamo4 = Prestamo(lector2, libro1, datetime(2021, 2, 23))

#Devolver un libro prestrado con mas de 15 dias
print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')
prestamo1.devuelve_libro(datetime(2021, 4, 22))
print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')

#Prestar un libro devuelto
prestamo5 = Prestamo(lector2, libro1, datetime(2021, 2, 23))

#Imprimir lista de los libros alquilados
print(Prestamo.libros_prestados())
