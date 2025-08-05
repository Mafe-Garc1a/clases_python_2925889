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
            self.estado=estado_cambio
            print("cambio")
            return True
        return False
    def asignar_asignatura(self , asignaturas:Asignaturas ,codigo_asignatura:int):
        if self.asignaturas.codigo!=codigo_asignatura:
            print("si")
            item={
                'codigo':asignaturas.codigo,
                'nombre_asignatura':asignaturas.nombre_asignatura,
            }
            self.asignaturas.append(item)

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
    def __init__(self , documento_profesor:int , nombres:str , apellidos:str , codigo_asignatura:int , asignaturas_dispo:Asignaturas):
        self.documento_profesor=documento_profesor
        self.nombres=nombres
        self.apellidos=apellidos
        if codigo_asignatura==asignaturas_dispo:
            self.codigo_asignatura=codigo_asignatura
        else:
            print("lo sentimos , esta asignatura no esta registrada en nuestro sistema")
    

class Notas:
    def __init__(self , nota_id:int):
            self.nota_id=nota_id
            self.lista_estudiantes_notas: List[dict] = []

    def calificar(self,nota_id:int , nota:float , estudiante:Estudiante , profesor:Profesor)->str:
        if nota < 5 and nota >0 :
            item={
                'nota':nota,
                'nombre_estudiante':estudiante.nombres,
                'profesor':profesor.nombres
            }
            self.lista_estudiantes_notas.append(item)
            if nota >3 :
                print("estudiante aprobo")
            else:
                if nota <3:
                    print("estudiante reprobo")
    def todas_notas(self)->str:
        for item in self.lista_estudiantes_notas:
            estudiante=item['nombre_estudiante']
            profesor=item['profesor']
            nota=item¨['nota']
            return f"estudiante : {estudiante} , profesor:{profesor},nota:{nota}"

   
        
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
# self , documento_estudiante:int ,nombres:str ,apellidos:str , estado:bool
estudiante1=Estudiante(123,"Angelina" ,"Ocampo",True)
estudiante1.estado_cambio(False)
prof1 = Profesores("Vicente", "Nuñez", "1234567891", asig1)
print (angelina.agregar_asignatura(asignatura1))
print(angelina.todas_notas())

nota1 = Notas(1)
print(nota1.calificar(prof1, angelina, 2))