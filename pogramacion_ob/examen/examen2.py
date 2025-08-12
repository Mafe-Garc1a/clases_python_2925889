from datetime import datetime #importante cuando se va a trabajar con fechas y horas (de esta clase importar ste objeto{paquetes de python})
from typing import List
# galpones
roles=[]
tareas=[]
usuarios = []

class Tareas:
    def __init__(self,id_tarea:int ,descripcion:str):
        self.id_tarea=id_tarea
        self.descripcion=descripcion
        if self.id_tarea not in tareas:
            nueva_tarea={
                'id_tarea':self.id_tarea,
                'descripcion':self.descripcion
            }
            tareas.append(nueva_tarea)
class Roles:
    def __init__(self,id_rol:int,nombre_rol:str):
        self.id_rol=id_rol
        self.nombre_rol=nombre_rol
        if self.id_rol not in roles:
            nuevo_rol={
                'id_rol':self.id_rol,
                'nombre_rol':self.nombre_rol
            }
            roles.append(nuevo_rol)

    def ver_roles(self):
        for rol in roles:
            print(f'id_rol : {rol['id_rol']} | nombre_rol : {rol['nombre_rol']}')
class Usuario(Roles):
    def __init__(self, id_rol:int, nombre_rol:str , documento_usuario:int , nombre_usuario:str,email:str,telefono:int):
        super().__init__(id_rol, nombre_rol)
        self.__documento_usuario=documento_usuario
        self.__nombre_usuario=nombre_usuario
        self.__email=email
        self.__telefono=telefono
        if self.__documento_usuario not in usuarios:
            for rol in roles:
                if self.id_rol ==rol['id_rol']:
                    nuevo_usuario={
                        'documento_usuario':self.__documento_usuario,
                        "id_rol":self.id_rol,
                        'nombre_usuario':self.__nombre_usuario,
                        'email':self.__email,
                        'telefono':self.__telefono,
                        'tareas':[],
                    }
                    usuarios.append(nuevo_usuario)
    def resumen_usuario(self)->str:
        print(f'docuemnto: {self.__documento_usuario} | nombre : {self.__nombre_usuario} | email:{self.__email}|telfono:{self.__telefono} |cargo {self.nombre_rol}')
    def asignar_tarea(self,id_tarea:int):
         for usuario in usuarios:
            if usuario['documento_usuario'] == self.__documento_usuario:
                for tarea in tareas:
                    if id_tarea==tarea['id_tarea']:
                        if id_tarea not in usuario['tareas']:
                            nueva_tarea={
                                "id_tarea":id_tarea,
                                "descripcion_tarea":tarea['descripcion'],
                                "hora_inicio":datetime.now(),
                                "estado":'pendiente',
                                "hora_fin":None
                            }
                            usuario['tareas'].append(nueva_tarea)
                        else:

                            print("la tarea ya existe")
                            return
                    
        
            
    def tarea_finalizada(self,id_tarea ):
        for usuario in usuarios:
            if usuario['documento_usuario'] == self.__documento_usuario:
                for tarea in usuario['tareas']:
                    for tarea_validacion in tareas:
                        if tarea_validacion['id_tarea']==id_tarea:
                            if tarea['id_tarea'] == id_tarea and tarea['estado'] == 'pendiente' :
                                tarea['estado'] = 'finalizado'
                                tarea['hora_fin'] = datetime.now()
                            print(f"Tarea {id_tarea} finalizada.")
                            return
                print("Tarea no encontrada o ya finalizada.")
                return
        print("Usuario no registrado.")

    def mostrar_tareas(self):
        for usuario in usuarios:
            if usuario['documento_usuario'] == self.__documento_usuario:
                for tarea in usuario['tareas']:
                    print(f"id_tarea: {tarea['id_tarea']} | Descripción: {tarea['descripcion_tarea']} | Estado: {tarea['estado']} | Inicio: {tarea['hora_inicio']} | Fin: {tarea['hora_fin']}")
    def tareas_pendientes(self):
        for usuario in usuarios:
            if usuario['documento_usuario']==self.__documento_usuario: 
                for tarea in usuario['tareas']:
                    if tarea['estado']=="pendiente":
                        print(f"tarea pendiente {tarea['id_tarea']}")
                        print(f"id_tarea: {tarea['id_tarea']} | Descripción: {tarea['descripcion_tarea']} | Estado: {tarea['estado']} | Inicio: {tarea['hora_inicio']} | Fin: {tarea['hora_fin']}")
                        
                    else:
                        if tarea['estado']!="pendiente":
                            print(f"la tarea {tarea['id_tarea']} ya esta realizada")
    
# Crear roles
rol1 = Roles(1, "Administrador")
rol2 = Roles(2, "Técnico")
rol3 = Roles(3, "Supervisor")

print(" Roles registrados:")
rol1.ver_roles()

tarea1=Tareas(1, "Pago Nomina")
tarea2 = Tareas(2, "Inspección de galpón A")
tarea3 = Tareas(3, "Limpieza de filtros")
tarea4 = Tareas(4, "Control de temperatura")


usuario1 = Usuario(1, "Administrador", 1, "Alice", "alice@mail.com", 3001111111)
usuario2 = Usuario(2, "Técnico", 2, "Bob", "bob@mail.com", 3002222222)
usuario3 = Usuario(3, "Supervisor", 3, "Carol", "carol@mail.com", 3003333333)


usuario1.resumen_usuario()

usuario1.asignar_tarea(1)  
usuario2.asignar_tarea(2) 
usuario3.asignar_tarea(3)  

usuario2.asignar_tarea(1)  
usuario3.asignar_tarea(2)  

usuario1.mostrar_tareas()


usuario2.tarea_finalizada(1) 
usuario3.tarea_finalizada(3) 

usuario2.mostrar_tareas()

usuario1.tareas_pendientes()


usuario2.tareas_pendientes()


usuario3.tareas_pendientes()

