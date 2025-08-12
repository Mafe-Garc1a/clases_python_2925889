# --------------PRUEBA DESEMPEÑO PYTHON----------------
# MARIA FERNANDA GARCIA CARVAJAL
# FICHA:2925889  - ANALISIS Y DESARROLLO DE SOFTWARE
from typing import List

# 1-registro y consltas de cursos
cursos =[
    {
        "id":1,
        "nombre_curso":"python Basico",
        "instructor":"sanda ruiz",
        "estudiantes":["Carlos", "Diana","Mateo"]
    },
    {
        "id":2,
        "nombre_curso":"Algoritmos",
        "instructor":"sanda ruiz",
        "estudiantes":["Laura", "Mateo"]
    },
]

def mostrar_cursos(cursos)->str:
    print("hello")
    for item in cursos :
        id=item["id"]
        nombre_curso=item['nombre_curso']
        instructor=item['instructor']
        estudiantes=item['estudiantes']
        print (f"id curso :{id} -nombre curso : {nombre_curso} , -instructor{instructor}")
        print(f"numero de estudiantes {len(estudiantes)}")


print(mostrar_cursos(cursos))


def buscar_curso_estudiante(nombre_estudiante:str ,cursos)->str:
    contador=[]
    for item in cursos:
        estudiantes=item['estudiantes']
        nombre_curso=item['nombre_curso']
        for estudiante in  estudiantes:
            if estudiante == nombre_estudiante:
                contador.append(nombre_curso)
    return contador
    
        
print(buscar_curso_estudiante("Mateo",cursos))


# 2-registro calificaciones

notas={
        "python Basico":{
            'Carlos':[4.8,3.5,4.2],
            'Diana':[3.0,3.9,4.0],
            'Mateo':[5.0,4.8,4.9],
        },
        "Algoritmos":{
            'Laura':[3.5,3.2,3.7],
            'Mateo':[4.5,4.6,4.7],
        }
}

agregar_curso:List[dict]=[]

def promedio_estudiante_curso(nombre_curso:str,nombre_estudiante:str,notas)->str:
    suma=0
    for curso , estudiantes in notas.items():
        if curso==nombre_curso: 
         print(f"Materia: {curso}")
        for estudiante, calificaciones in estudiantes.items():
            if estudiante==nombre_estudiante:
                print(estudiante)
                for calificacion in calificaciones:
                    print(calificacion)
                    suma=(suma+calificacion)
                return f"promedio : {suma/len(calificaciones)}"       
         
print(promedio_estudiante_curso("python Basico","Carlos",notas))



def aprobados_por_curso(notas)->str:
        for curso , estudiantes in notas.items():
            print(f"Materia: {curso}")
            for estudiante, calificaciones in estudiantes.items():
                suma=0
                print(estudiante)
                for calificacion in calificaciones:
                    suma=(suma+calificacion)
                promedio_general=suma/len(calificaciones)
                if promedio_general >=3.5 :
                    print("APROBO")
                    print(f"nombre estudiante: {estudiante} promedio:{promedio_general}")
print(aprobados_por_curso(notas))

def reporte_estudiantes(nombre_estudiante ,notas)->str:
    for curso , estudiantes in notas.items():
        for estudiante, calificaciones in estudiantes.items():
            suma=0
            promedio=0
            if estudiante==nombre_estudiante:
                print(f"reporte :{estudiante}")
                for calificacion in calificaciones:
                    suma=(suma+calificacion)
                promedio=suma/len(calificaciones)
                if promedio >3.5 :
                    estado="aprobo"
                else:
                    estado="reprobo"
                print( f"curso:{curso} | promedio:{promedio} |estado :{estado}")
            


print(reporte_estudiantes("Mateo",notas))

print("*******************************")
# class EstudianteEj:
#     def __init__(self,nombres:str):
#         self.nombres=nombres
#         self.__notas:List[float]=[]
#     def agregar_notas(self,nota:float)->float:
#         self.__notas.append(nota)
#     def calcular_promedio(self)->float:
#         suma=0
#         for nota in self.__notas:
#             suma=suma+nota
#         promedio=suma/len(self.__notas)
#         print(f"promedio : {promedio}")
#         return promedio
#     def estado(self)->str:
#         promedio=self.calcular_promedio()
#         if promedio >=3.5 :
#             return f"aprobo"
#         else:
#             return f"reprobo"
    
        


# estudiante1=EstudianteEj("Mafe")
# estudiante1.agregar_notas(4.4)
# estudiante1.agregar_notas(3.5)
# print(estudiante1.calcular_promedio())
# print(estudiante1.estado())


# class CursoEj:
#     def __init__(self,nombre_curso:str,instructor:str):
#         self.nombre_curso=nombre_curso
#         self.instructor=instructor
#         self.estudiantes:List[Estudiante]=[]

#     def agregar_estudiante(self , estudiante:EstudianteEj):
#         self.estudiantes.append(estudiante)
#     def mostrar_estudiantes(self)->str:
#         print(f"curso{self.nombre_curso}-Instructor:{self.instructor}")
#         for estudiante in self.estudiantes:
#             nombre_estudiante=estudiante.nombres
#             promedio=estudiante.calcular_promedio()
#             estado=estudiante.estado()
#             print(f"-{nombre_estudiante} |promedio : {promedio}  | estado : {estado}")


# curso_python = CursoEj("Python Intermedio", "Sandra Ruiz")


# est1 = EstudianteEj("Carlos")
# est1.agregar_notas(4.0)
# est1.agregar_notas(4.5)

# est2 = EstudianteEj("Laura")
# est2.agregar_notas(3.0)
# est2.agregar_notas(3.2)

# est3 = EstudianteEj("Mateo")
# est3.agregar_notas(5.0)
# est3.agregar_notas(4.9)

# curso_python.agregar_estudiante(est1)
# curso_python.agregar_estudiante(est2)
# curso_python.agregar_estudiante(est3)
# curso_python.mostrar_estudiantes()


print("*******************************")
print("***********UNIFICACION***********")

# creo dos diccionarios para guardar toda la informacion de estudiantes y instructores para luego hacer cambios o acceder a esos datos de manera independiente(por ejemplo si un estudiante se quiere inscrbir a otrom curso)y si se cambian datos se deben actualizar en todo si no existiera esto
estudiantes = {} 
instructores = {}  
class Persona:
    def __init__(self ,documento:int ,nombre:str ,correo:str ):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

# Clase Instructor
class Instructor(Persona):
    def __init__(self, documento:int, nombre:str, correo:str, area_experiencia:str):
        super().__init__(documento, nombre, correo)
        self.area_experiencia = area_experiencia

# Clase Estudiante
class Estudiante(Persona):
    def __init__(self, documento:int, nombre:str, correo:str, ficha_formacion:str):
        super().__init__(documento, nombre, correo)
        self.ficha_formacion = ficha_formacion

    def inscribirse(self, nombre_curso:str):
        for curso in cursos:
            if curso["nombre_curso"] == nombre_curso:
                if self.documento not in curso["estudiantes"]:
                    curso["estudiantes"].append(self.documento)
                    return print( f"{self.documento} | {self.nombre} se ha inscrito en el curso {nombre_curso}")
                else:
                    return print( f"El estudiante {self.nombre} ya está inscrito en el curso")
        return print("El curso no existe")

    

class Curso:
    def __init__(self, id:int, nombre_curso:str, documento_instructor:int):
        if documento_instructor in instructores:
            if nombre_curso not in  cursos:
                instructor = instructores[documento_instructor]
                nuevo_curso = {
                    "id": id,
                    "nombre_curso": nombre_curso,
                    "instructor": instructor.nombre,
                    "estudiantes": []
                }
                cursos.append(nuevo_curso)
                print(f"Curso '{nombre_curso}'  | el instructor {instructor.nombre}")
            else:
                return print(f"ese curso ya esta registrado")
        else:
            return print(f"EL INSTRUCTOR NO SE ENCUENTRA EN NUESTRA BASE DE DATOS")

        
class Notas:
    def __init__(self, nombre_curso: str, documento_estudiante: int, documento_instructor: int):
        self.nombre_curso = nombre_curso
        self.documento_estudiante = documento_estudiante
        self.documento_instructor = documento_instructor

    def agregar_notas(self, nota: float):
        for curso in cursos:
            if curso['nombre_curso'] == self.nombre_curso:
                if curso['instructor'] == instructores[self.documento_instructor].nombre:
                    if self.documento_estudiante in curso['estudiantes']:
                        if self.nombre_curso not in notas:
                            notas[self.nombre_curso] = {}

                        if self.documento_estudiante not in notas[self.nombre_curso]:
                            notas[self.nombre_curso][self.documento_estudiante] = []

                        notas[self.nombre_curso][self.documento_estudiante].append(nota)
                        print("Nota agregada correctamente.")
                        return
                    else:
                        print("El estudiante no se encuentra registrado en este curso")
                        return
                else:
                    print(f"Instructor no autorizado para calificar este curso: {self.nombre_curso}")
                    return
        print("El curso no está registrado")

    def promedio_estudiante_curso(self, nombre_curso, documento_estudiante) -> float:
        if nombre_curso in notas and documento_estudiante in notas[nombre_curso]:
            suma = sum(notas[nombre_curso][documento_estudiante])
            promedio = suma / len(notas[nombre_curso][documento_estudiante])
            print(f"{documento_estudiante} | Promedio en {nombre_curso}: {promedio:.2f}")
            return promedio
        print("No hay notas registradas.")
        return 0.0

    def reporte_estudiante(self, documento_estudiante):
        print(f"\n--- Reporte de {documento_estudiante} ---")
        for curso_nombre, estudiantes_notas in notas.items():
            if documento_estudiante in estudiantes_notas:
                promedio = self.promedio_estudiante_curso(curso_nombre, documento_estudiante)
                estado = "Aprobó" if promedio >= 3.5 else "Reprobó"
                print(f"{curso_nombre} | Promedio: {promedio:.2f} | Estado: {estado}")

    
    def aprobados_por_curso(notas_dict) -> str:
        for curso, estudiantes in notas_dict.items():
            print(f"Materia: {curso}")
            for estudiante, calificaciones in estudiantes.items():
                promedio_general = sum(calificaciones) / len(calificaciones)
                if promedio_general >= 3.5:
                    print(f"APROBÓ | Estudiante: {estudiante} | Promedio: {promedio_general:.2f}")




def mostrar_cursos():
    print("\n--- Cursos Disponibles ---")
    for curso in cursos:
        print(f"ID: {curso['id']} | Curso: {curso['nombre_curso']} | Instructor: {curso['instructor']}")
        print(f"Estudiantes inscritos: {curso['estudiantes']}")



instructor2 = Instructor(222, "Laura Sánchez", "laura@correo.com", "Bases de Datos")
instructores[instructor2.documento] = instructor2

est4 = Estudiante(104, "Luis", "luis@correo.com", "F124")
est5 = Estudiante(105, "Valentina", "valentina@correo.com", "F124")
estudiantes[est4.documento] = est4
estudiantes[est5.documento] = est5

nuevo_curso_bd = Curso(4, "Bases de Datos", 222)

est4.inscribirse("Bases de Datos")
est5.inscribirse("Bases de Datos")

notas_luis = Notas("Bases de Datos", 104, 222)
notas_valentina = Notas("Bases de Datos", 105, 222)

notas_luis.agregar_notas(4.0)
notas_luis.agregar_notas(4.2)

notas_valentina.agregar_notas(3.0)
notas_valentina.agregar_notas(3.4)

notas_luis.promedio_estudiante_curso("Bases de Datos", 104)
notas_valentina.promedio_estudiante_curso("Bases de Datos", 105)

notas_luis.reporte_estudiante(104)
notas_valentina.reporte_estudiante(105)

Notas.aprobados_por_curso(notas)

