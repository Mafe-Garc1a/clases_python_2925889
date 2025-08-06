from typing import List

# 1️⃣ CLASE ESTUDIANTE
class Estudiante:
    def __init__(self, nombre: str):
        self.nombre = nombre                 # nombre del estudiante
        self.__notas: List[float] = []       # lista privada de notas

    def agregar_nota(self, nota: float):
        self.__notas.append(nota)            # agrega una nota a la lista

    def calcular_promedio(self) -> float:
        if len(self.__notas) == 0:
            return 0                         # evita división por cero
        suma = sum(self.__notas)             # suma todas las notas
        return round(suma / len(self.__notas), 1)  # promedio con 1 decimal

    def estado(self) -> str:
        promedio = self.calcular_promedio()
        return "Aprobado" if promedio >= 3.5 else "Reprobado"  # devuelve el estado
# 2️⃣ CLASE CURSO
class Curso:
    def __init__(self, nombre: str, instructor: str):
        self.nombre = nombre                # nombre del curso
        self.instructor = instructor        # nombre del instructor
        self.estudiantes: List[Estudiante] = []  # lista de estudiantes

    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)  # agrega un estudiante al curso

    def mostrar_estudiantes(self):
        print(f"Curso: {self.nombre} - Instructor: {self.instructor}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            promedio = estudiante.calcular_promedio()
            estado = estudiante.estado()
            print(f"- {estudiante.nombre} | Promedio: {promedio} | Estado: {estado}")
# 3️⃣ SIMULACIÓN DEL USO
# Creamos el curso
curso_python = Curso("Python Intermedio", "Sandra Ruiz")

# Creamos estudiantes
est1 = Estudiante("Carlos")
est1.agregar_nota(4.0)
est1.agregar_nota(4.5)

est2 = Estudiante("Laura")
est2.agregar_nota(3.0)
est2.agregar_nota(3.2)

est3 = Estudiante("Mateo")
est3.agregar_nota(5.0)
est3.agregar_nota(4.9)

# Agregamos estudiantes al curso
curso_python.agregar_estudiante(est1)
curso_python.agregar_estudiante(est2)
curso_python.agregar_estudiante(est3)

# Mostramos los estudiantes del curso
curso_python.mostrar_estudiantes()
