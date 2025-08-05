# Crear un pequeño software con 3 clases (estudiantes, profesores y notas) en los 3 debe de estar el metodo constructor
# en estudiantes debe de haber un metodo para cambiar al estudiante de activo a inactivo (true or false)
# en la clase estudiante debe d haber un atributo de asignaturas tipo lista
# en estudiante debe de haber un metodo "agregar asignatura del estudiante"
# -----------------------------------------------------------------
# en la clase profesor debe de haber un metodo calificar 
# en las clases notas debe de haber un metodo que resiba la asignatura y la nota,y q confirme si aprobo o no aprobo
# en las clases notas debe de haber un metodo para imprimir todas las notas del estudiante en todas las asignaturas
# y si aprobo o no, utilizando el metodo anterior, las notas solo pueden ser de 0 a 5
#  donde se imprimien todas las notas debe de salir quien califico



# Self solo funciona con los atributos de una clase/objeto, si yo llamo a una clase/objeto
# como parametro NO es necesario llamarlo con self, seria solo llamar al parametro y decirle que 
# quiero sacarle como por ejemplo: Asignatura.nombre

from datetime import datetime
from typing import List 

class Asignatura:
    def __init__(self, codigo_asignatura: int, nombre_asignatura: str): 
        self.cod = codigo_asignatura
        self.nombre = nombre_asignatura
        print("Ya ingrese una asignatura humana")

class Estudiante: 
    def __init__ (self, nombre_aprendiz: str, apellido_aprendiz: str, documento_aprendiz: str, estado_aprendiz: bool): 
        self.nombre = nombre_aprendiz
        self.apellido = apellido_aprendiz
        self.documento = documento_aprendiz
        self.lista_asignaturas: List[dict]=[]
        self.estado = estado_aprendiz

    def agregar_asignatura(self, id_asignatura: Asignatura ) -> str: 
        item = {
            'cod': id_asignatura.cod, 
            'nombre': id_asignatura.nombre
        }
        self.lista_asignaturas.append(item)
        return f'Señor usuario ha sido inscrito exitosamente en la asigantura {id_asignatura.nombre}'
    
    def cambiar_de_estado(self, cambio_estado: bool) -> bool: 
        if self.estado != cambio_estado: 
            self.estado = cambio_estado
            return True
        return False 
    
    def obtener_certificado(self) -> str:
        resumen = f"Nombre: {self.nombre}, apellido: {self.apellido}, documento: {self.documento} \n"
        for item in self.lista_asignaturas: 
            codigo = item["cod"] # si no es variable siempre debe de ir en comillas al ser de lista
            nombre = item["nombre"]

            resumen += f"codigo asignatura: {codigo} - {nombre} "
        return resumen

class Profesor: 
    def __init__(self, nombre_profesor: str, apellido_profesor: str, documento_profesor: str, asignatura_profesor: Asignatura): 
        self.nombre = nombre_profesor
        self.apellido = apellido_profesor
        self.documento = documento_profesor
        self.asignatura_dada = asignatura_profesor.nombre
        print("Ya ingrese un profe, calmate")



class Notas: 
    def __init__(self, id_notas: int): 
        self.id_notas = id
        self.lista_estudiantes_notas: List[dict] = []
    
    def ingresar_notas(self, profesor: Profesor, estudiante: Estudiante, nota: float) -> str: 
        if nota < 0 or nota > 5: 
            return "Señor usuario, la nota sobrepasa los estándares"

        item2 = { 
            "nota": nota, 
            "estudiante": estudiante.nombre, 
            "profesor": profesor.nombre
        }
        self.lista_estudiantes_notas.append(item2) # nunca colocar el append debajo de un return q sea de su misma función
        # porque el return para todo entonces por ejemplo, esto estaria mal: 
        # else: 
        #     if nota >= 3 and nota <=5: 
        #         return "Estudiante aprobado"
        #     else: 
        #         return "Estudiante desaprobado" -- es q aqui pararia todo y no se agregaria al arreglo
        #         en cambio si el append va arriba se va a ejecutar
            
        #     item2 = {
        #         "nota": nota, 
        #         "estudiante": estudiante.nombre, 
        #         "profesor": profesor.nombre
        #     }

        if nota >= 3:
            return "Estudiante aprobado"
        else:
            return "Estudiante desaprobado"

        




angelina = Estudiante("Angelina", "Ocampo", "1088828178", True)
print(angelina.cambiar_de_estado(False))

# esto no se puede hacer, si es constructor no (Adicional a esto un constructor no puede retornar datos
# el solo inicializa el ojeto, puede imprimir cosas na mas)
# print(asig1 = Asignatura(12345, "Mates"))

asig1 = Asignatura(12345, "Mates")
prof1 = Profesor("Vicente", "Nuñez", "1234567891", asig1)
print (angelina.agregar_asignatura(asig1))
print(angelina.obtener_certificado())

nota1 = Notas(1)
print(nota1.ingresar_notas(prof1, angelina, 2))


