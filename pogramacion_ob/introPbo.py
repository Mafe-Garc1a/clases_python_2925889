# git remote add origin https://github.com/Mafe-Garc1a/clases_python.git
# git branch -M main
# git push -u origin main
# crear persona
# siempre 1 letra en mayuscula
class Persona:
    # lista atributos(de clase)
    tipoId=''
    numId=''
    nombres=''
    apellidos=''
    correo=''
    # este metodo esta dentro de una clase y por eso se llama clase
    # self->propio\coja ese objeto que esta activo
    # siempre utilizar elf ya que es el objeto quese eszta llamando
    def ver_datos(self):
        print(f"Mi nombre es: {self.nombres } mi apellido es: {self.apellidos} ")
    
    def actualizar_datos(self,new_nombre,new_email=None):
        self.nombres=new_nombre
        if new_email is not None :
            self.correo=new_email   
        print(f"mi nombr actualizado : {self.nombres} correo : {self.correo}")
        
#  creando mi primer objeto
Persona1=Persona()
# asignar sus atributos
Persona1.tipoId='CC'
Persona1.numId='23442455'
Persona1.nombres='Pepe'
Persona1.apellidos='Perez'
Persona1.correo='pepe@gmail.com'
# creando segundo objeto
Persona2=Persona()
# asignar sus atributos
Persona2.tipoId='TI'
Persona2.numId='37402456'
Persona2.nombres='Sofia'
Persona2.apellidos='Plus'
Persona2.correo='sofplus4k@gmail.com'

Persona1.ver_datos()
Persona2.ver_datos()

Persona1.actualizar_datos("pepito","pepi123@gmail.com")
Persona1.ver_datos()

print(Persona1.correo)
persona2=Persona() #instancia de una clase
print('**********   ')
#SE CREA UNA CLASE CON HERENCIAS
class Aprendiz(Persona):
    nom_carrera=""
    cod_ficha=0
    nota=0
    def descargar_certificado(self):
        print('-----------------------------------------')
        print(f"programa  en curso :  {self.nom_carrera}")
        print(f"codigo de ficha:  {self.cod_ficha}")
        print(f"Aprendiz:  {self.nombres}  {self.apellidos}")

Aprendiz1=Aprendiz()
Aprendiz1.tipoId="ti"
Aprendiz1.numId="123568057"
Aprendiz1.nombres="Maria fernanda"
Aprendiz1.correo="maria123@gmail.com"
Aprendiz1.nom_carrera="ADSO"
Aprendiz1.cod_ficha=2925889
# descargar certificado
Aprendiz1.descargar_certificado()
Aprendiz2=Aprendiz()
Aprendiz2.tipoId="cc"
Aprendiz2.numId="123568057"
Aprendiz2.nombres="juan david"
Aprendiz2.correo="juanDa@gmail.com"
Aprendiz2.nom_carrera="ADSO"
Aprendiz2.cod_ficha=2925889
# descargar certificado
Aprendiz2.descargar_certificado()


# crear clase intructor y 2 ejemplos
# analizar una clase animal con a clase , gato , perro delfin,serpiente piton (atributosgenerales de todoslos aniimales y una clase perro que herede de animales lo que se enga que heredar y que tenga metodos y atrubutos esppeciales , minimo 2 por cada clase)
# juegode la ufc ->luchadores  metodos :patiar ,
# disminuir vida , caracteristicas
class Instructor(Persona):
    especialidad=""
    tipo_contrato=""
    caificacion=0
    def descargar_certificado(self):
        print('-----------------------------------------')
        print(f"especialidad :  {self.especialidad}")
        print(f"tipo contrato:  {self.tipo_contrato}")
        print(f"Instructor:  {self.nombres}  {self.apellidos}")
        print(f"Contacto:  {self.correo}")

Instructor1=Instructor()
Instructor1.tipoId="cc"
Instructor1.numId="123568057"
Instructor1.nombres="Maria fernanda"
Instructor1.correo="maria123@gmail.com"
Instructor1.especialidad="ADSO"
Instructor1.tipo_contrato="planta"
Instructor1.descargar_certificado()


print("-*******ANIMALES********")
class Animal :
    nombre=""
    genero=""
    edad=""
    tipo_animal=""
    peso=0
    altura=0

class perro(Animal):
    raza_perro=""
    def descargar_p(self):
        print('-----------------------------------------')
        print(f"nombre:  {self.nombre}")
        print(f"tipo animal:  {self.tipo_animal}")
        print(f"raza:{self.raza_perro}")
        print(f"edad y genero:  {self.edad}  {self.genero}") 
        print(f"peso:  {self.peso} altura:  {self.altura}") 


class gato(Animal):
    raza_gato=""
    def descargar_g(self):
        print('-----------------------------------------')
        print(f"nombre:  {self.nombre}")
        print(f"tipo animal:  {self.tipo_animal}")
        print(f"raza:{self.raza_gato}")
        print(f"edad y genero:  {self.edad}  {self.genero}") 
        print(f"peso:  {self.peso} altura:  {self.altura}") 
        
class delfin(Animal):
    tipo_delfin=""
    def descargar_g(self):
        print('-----------------------------------------')
        print(f"nombre:  {self.nombre}")
        print(f"tipo animal:  {self.tipo_animal}")
        print(f"raza:{self.raza_gato}")
        print(f"edad y genero:  {self.edad}  {self.genero}") 
        print(f"peso:  {self.peso} altura:  {self.altura}") 


        
# ----------------------------------------------------------------