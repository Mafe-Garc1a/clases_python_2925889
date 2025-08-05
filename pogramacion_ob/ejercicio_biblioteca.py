Ejercicio: Sistema de Biblioteca Simple
Crea un sistema para registrar libros prestados a usuarios. Cada libro tiene un título y un autor. Cada usuario puede prestar varios libros.

Clases que vamos a usar:
Libro
Usuario
Biblioteca

from typing import List
from datetime import datetime


class Biblioteca:
    def __init__(self):
        self.__libros_disponibles: List[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.__libros_disponibles.append(libro)
        print(f"Libro agregado: {libro.info_L()}")

    def mostrar_libros(self):
        print("Libros disponibles en la biblioteca:")
        for libro in self.__libros_disponibles:
            print("  -", libro.info_L())
class Libro:
    def __init__(self, titulo: str, autor: str):
        self.__titulo = titulo         # Encapsulado
        self.__autor = autor           # Encapsulado

    def info_L(self) -> str:
        return f"{self.__titulo} por {self.__autor}"


class Usuario:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__libros_prestados: List[Libro] = []  # Lista de libros

    def prestar_libro(self, libro: Libro):
        self.__libros_prestados.append(libro)
        print(f"{self.__nombre} ha prestado: {libro.info_L()} ,el dia {datetime.now()}")

    def ver_libros(self):
        print(f"Libros prestados a {self.__nombre}:")
        if not self.__libros_prestados:
            print("  - Ningún libro prestado")
        else:
            for libro in self.__libros_prestados:
                print("  -", libro.info_L())

# INGRESAR NFO
# Crear biblioteca
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro("1984", "George Orwell")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.mostrar_libros()

# Crear usuario
usuario1 = Usuario("Laura")

# Prestar libros
usuario1.prestar_libro(libro1)
usuario1.prestar_libro(libro3)

# Ver libros prestados
usuario1.ver_libros()
    

