from typing import List, Dict

# Diccionarios originales (SE MANTIENEN TAL CUAL)
cursos = [
    {
        "id": 1,
        "nombre_curso": "python Basico",
        "instructor": "sanda ruiz",
        "estudiantes": ["Carlos", "Diana", "Mateo"]
    },
    {
        "id": 2,
        "nombre_curso": "Algoritmos",
        "instructor": "sanda ruiz",
        "estudiantes": ["Laura", "Mateo"]
    },
]

notas = {
    "python Basico": {
        'Carlos': [4.8, 3.5, 4.2],
        'Diana': [3.0, 3.9, 4.0],
        'Mateo': [5.0, 4.8, 4.9],
    },
    "Algoritmos": {
        'Laura': [3.5, 3.2, 3.7],
        'Mateo': [4.5, 4.6, 4.7],
    }
}

# Nuevos diccionarios reutilizables para registros
estudiantes = {}  # documento: objeto Estudiante
instructores = {}  # documento: objeto Instructor

# ---------------- Clases ------------------

class Persona:
    def __init__(self, nombre: str, documento: str, correo: str):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo


class Instructor(Persona):
    def __init__(self, nombre, documento, correo, area_experiencia=""):
        super().__init__(nombre, documento, correo)
        self.area_experiencia = area_experiencia

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, instructor del área de {self.area_experiencia}")


class Estudiante(Persona):
    def __init__(self, nombre, documento, correo, ficha_formacion):
        super().__init__(nombre, documento, correo)
        self.ficha_formacion = ficha_formacion

    def inscribirse(self, nombre_curso):
        for curso in cursos:
            if curso["nombre_curso"] == nombre_curso:
                if curso["instructor"] == "":
                    print("No se puede inscribir. El curso no tiene instructor.")
                    return
                if self.nombre not in curso["estudiantes"]:
                    curso["estudiantes"].append(self.nombre)
                    print(f"{self.nombre} se ha inscrito en el curso {nombre_curso}")
                    return
                else:
                    print("Ya estás inscrito.")
                    return
        print("Curso no encontrado.")


class Notas:
    @staticmethod
    def agregar_nota(nombre_curso, nombre_estudiante, documento_instructor, nota):
        curso = next((c for c in cursos if c["nombre_curso"] == nombre_curso), None)
        if not curso:
            print("Curso no existe.")
            return
        if curso["instructor"] != instructores.get(documento_instructor, {}).nombre:
            print("Instructor no autorizado.")
            return
        if nombre_estudiante not in curso["estudiantes"]:
            print("Estudiante no está inscrito.")
            return
        if nombre_curso not in notas:
            notas[nombre_curso] = {}
        if nombre_estudiante not in notas[nombre_curso]:
            notas[nombre_curso][nombre_estudiante] = []
        notas[nombre_curso][nombre_estudiante].append(nota)
        print("Nota agregada correctamente.")

    @staticmethod
    def promedio_estudiante_curso(nombre_curso, nombre_estudiante):
        if nombre_curso in notas and nombre_estudiante in notas[nombre_curso]:
            calificaciones = notas[nombre_curso][nombre_estudiante]
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"{nombre_estudiante} | Promedio en {nombre_curso}: {promedio:.2f}")
            return promedio
        print("No hay notas registradas.")
        return 0

    @staticmethod
    def reporte_estudiante(nombre_estudiante):
        print(f"\n--- Reporte de {nombre_estudiante} ---")
        for curso_nombre, estudiantes_notas in notas.items():
            if nombre_estudiante in estudiantes_notas:
                promedio = Notas.promedio_estudiante_curso(curso_nombre, nombre_estudiante)
                estado = "Aprobó" if promedio >= 3.5 else "Reprobó"
                print(f"{curso_nombre} | Promedio: {promedio:.2f} | Estado: {estado}")

    @staticmethod
    def aprobados_por_curso():
        print("\n--- Aprobados por Curso ---")
        for curso_nombre, estudiantes_notas in notas.items():
            print(f"\nCurso: {curso_nombre}")
            for estudiante, calificaciones in estudiantes_notas.items():
                promedio = sum(calificaciones) / len(calificaciones)
                if promedio >= 3.5:
                    print(f"  - {estudiante}: Aprobó con {promedio:.2f}")

# ---------------- Funciones auxiliares ------------------

def mostrar_cursos():
    print("\n--- Cursos Disponibles ---")
    for curso in cursos:
        print(f"ID: {curso['id']} | Curso: {curso['nombre_curso']} | Instructor: {curso['instructor']}")
        print(f"Estudiantes inscritos: {curso['estudiantes']}")

def buscar_curso_por_estudiante(nombre_estudiante):
    cursos_encontrados = []
    for curso in cursos:
        if nombre_estudiante in curso["estudiantes"]:
            cursos_encontrados.append(curso["nombre_curso"])
    return cursos_encontrados

# ---------------- Prueba completa ------------------

# Registrar instructor
instructor1 = Instructor("Sandra Ruiz", "111", "sandra@gmail.com", "Programación")
instructores[instructor1.documento] = instructor1

# Registrar estudiantes
est1 = Estudiante("Carlos", "001", "carlos@gmail.com", "F123")
est2 = Estudiante("Diana", "002", "diana@gmail.com", "F123")
est3 = Estudiante("Mateo", "003", "mateo@gmail.com", "F123")
estudiantes[est1.documento] = est1
estudiantes[est2.documento] = est2
estudiantes[est3.documento] = est3

# Inscribir estudiantes a cursos existentes
est1.inscribirse("python Basico")
est3.inscribirse("Algoritmos")

# Agregar notas con control de instructor
Notas.agregar_nota("python Basico", "Carlos", "111", 4.0)
Notas.agregar_nota("python Basico", "Carlos", "111", 4.5)
Notas.agregar_nota("Algoritmos", "Mateo", "111", 4.7)

# Mostrar información
mostrar_cursos()
Notas.reporte_estudiante("Carlos")
Notas.reporte_estudiante("Mateo")
Notas.aprobados_por_curso()

print("\nCursos de Mateo:")
print(buscar_curso_por_estudiante("Mateo"))
0