# 1-crear software con 3 clases(estudiantes,profesores,notas)->asignautas falto
# 2-en los 3 deben estar el metodo constructor para llenar la informacion
# 3-en esstudiante un metodo para cambiar el estado del estudiante(activo-inactivo{true,false})
# 4-en la clase estudiante debe aver un atributo de asignaturas tpo lista
# 5-en estudiantes debe aver u metodo agregar asignatura
# 6-en la clase profesor debe aver un metodo calificar
# 7-en la clase notas debe aver un metodo que reciba la asignaruta y la nota y diga si aprobo o no aprobo
# 8-en la clase notas debe aver un metodo para imprimir  todas las notas del estudiante con sus asignaturas y si aprobo o no 
# las notas solo pueden ser de 0 a 5
# donde se imprime todas las notas debe salir quien califico(profesor)

# SOFTWARE NOTAS
from datetime import datetime #importante cuando se va a trabajar con fechas y horas (de esta clase importar ste objeto{paquetes de python})
from typing import List

class Estudiante:
    def __init__(self , documento_estudiante:int ,nombres:str ,apellidos:str , estado:bool):
        self.documento_estudiante=documento_estudiante
        self.nombres=nombres
        self.apellidos=apellidos
        self.estado=estado
        self.asignaturas:List[dict]=[]
    
    def cambio_estado(self,estado_cambio:bool)->bool:
        if self.estado!=estado_cambio:
            self.estado==estado_cambio
            return True
        return False
    
    # def ingresar_asignaturas(self ,asignaturas:Asignarutas ,codigo_asignatura:int ):
    #     if(self.documento_estudiante!=documento_estudiante ):
    #         if(self.asignaruta.codigo!=codigo_asignatura)
    #         self.asignaturas.append(asignatura)
    #         else:
    #             print("la asignarura con este usuario ya esta registrado")

class Asignatura:
    def __init__(self , codigo:int, nombre_asignatura:str):
            self.codigo=codigo
            self.nombre_asignatura=nombre_asignatura 
    def imprimir(self)->str:
        print(f"CODIGO : {self.codigo}")
        print(f"NOMBRE : {self.nombre_asignatura}")

class Asignaturas():
    def __init__(self):
        self.asignaturas:List[dict]=[]
    def agegar_A(self , asignaturas:Asignatura):


        item={
            'codigo':asignaturas.codigo,
            'nombre':asignaturas.nombre_asignatura,
        }
        self.asignaturas.append(item)
        


    def ver_disponibles(self )->str:
        print("estas son asignaturas disponibles")
        for item in self.asignaturas:
           print(item)
            
 
class Profesores:
    def __init__(self , documento_profesor:int , nombres:str , apellidos:str , codigo_asignatura):
        self.documento_profesor=documento_profesor
        self.nombres=nombres
        self.apellidos=apellidos
        self.codigo_asignatura=codigo_asignatura

class Notas:
    def __init__(self , nota:int , documento_estudiante:int):
        if nota<=5 and nota>=0:
            self.documento_estudiante=documento_estudiante
            self.nota=nota
        return print('nota fuera de rango')
    def agregar_notas(self , estudiante:Estudiante ,profesor:Profesores ):
        item ={
            'documento_estudiante':estudiante.documento_estudiante,
            'nombre':estudiante.nombres,
            'apellidos':estudiante.apellidos,
        }
        item2={
            'documento_profesor':profesor.documento_profesor,
            'nombres':profesor.nombres,
            'apellidos':profesor.apellidos,
            'asignatura':profesor.codigo_asignatura

        }
        
# -------ingreso info-----------

asignatura1=Asignatura(1,'matematicas')
asignatura2=Asignatura(2,'español')
asignatura3=Asignatura(3,'sociales')
# asignatura1.imprimir()
materias=Asignaturas()
materias.agegar_A(asignatura1)
materias.agegar_A(asignatura2)
materias.agegar_A(asignatura3)
materias.ver_disponibles()