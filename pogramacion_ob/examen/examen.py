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
class Estudiante:
    def __init__(self,nombres:str):
        self.nombres=nombres
        self.__notas:List[float]=[]
    def agregar_notas(self,nota:float)->float:
        self.__notas.append(nota)
    def calcular_promedio(self)->str:
        suma=0
        for nota in self.__notas:
            suma=suma+nota
        promedio=suma/len(self.__notas)
        print(f"promedio : {promedio}")
        return promedio
    def estado(self)->str:
        promedio=self.calcular_promedio()
        if promedio >=3.5 :
            return f"aprobo"
        else:
            return f"reprobo"
    
        


estudiante1=Estudiante("Mafe")
estudiante1.agregar_notas(4.4)
estudiante1.agregar_notas(3.5)
print(estudiante1.calcular_promedio())
print(estudiante1.estado())


class Curso:
    def __init__(self,nombre_curso:str,instructor:str):
        self.nombre_curso=nombre_curso
        self.instructor=instructor
        self.estudiantes:List[Estudiante]=[]

    def agregar_estudiante(self , estudiante:Estudiante):
        self.estudiantes.append(estudiante)
    def mostrar_estudiantes(self)->str:
        print(f"curso{self.nombre_curso}-Instructor:{self.instructor}")
        for estudiante in self.estudiantes:
            nombre_estudiante=estudiante.nombres
            promedio=estudiante.calcular_promedio()
            estado=estudiante.estado()
            print(f"-{nombre_estudiante} |promedio : {promedio}  | estado : {estado}")


curso_python = Curso("Python Intermedio", "Sandra Ruiz")


est1 = Estudiante("Carlos")
est1.agregar_notas(4.0)
est1.agregar_notas(4.5)

est2 = Estudiante("Laura")
est2.agregar_notas(3.0)
est2.agregar_notas(3.2)

est3 = Estudiante("Mateo")
est3.agregar_notas(5.0)
est3.agregar_notas(4.9)

curso_python.agregar_estudiante(est1)
curso_python.agregar_estudiante(est2)
curso_python.agregar_estudiante(est3)
curso_python.mostrar_estudiantes()

class Persona:
    nombre=""
    documento=0
    correo=""

class Instructor(Persona):
    area_experiencia=""
    def presentarse(self):
        print(f"hola , soy {self.nombre} , instructor del area de {self.area_experiencia} ")
class EstudiantePoo(Persona):
    ficha_formacion=""
    def inscribirse(self,curso)->str:
        print(f"el estudiante {self.nombre} se ha inscrito n el curso {curso}")

instructor1 = Instructor()
instructor1.nombre="Ana Torres"
instructor1.documento="12345678"
instructor1.correo="ana@correo.com"
instructor1.area_experiencia="programacion"
instructor1.presentarse()

estudiante1 = EstudiantePoo()
estudiante1.nombre="Pepito Perez"
estudiante1.documento="87654321"
estudiante1.correo="PepitoPerez@gmail.com"
estudiante1.ficha_formacion="F123"
estudiante1.inscribirse("Python POO")

        
