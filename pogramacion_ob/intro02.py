class usuario:
    # atributo de clase compartido por todas las instancias
    plataforma="MiApp 1.0"
    #METODO CONSTRUCTOR - SE UTILIZA CUANDO SE CREA EL OBJETO
    # se ejecuta al instanciar una clase
    def __init__ (self,nombre,email): #METODO
        # atributos de instancia
        self.nombre=nombre
        self.email=email
        self.activo=True
    def saludar(self):
        return f"hola, soy{self.nombre}" #return es la forma correcta
    
    def desactivar (self):
        self.activo=False
        return f"usuario  :  {self.nombre} desactivado"
    
# crear otros objetos(instancias)
usuario1 = usuario("Ana Garcia","ana@gmail.com")
usuario2 = usuario("Carlos Lopez","Carlos@gmail.com")
usuario3= usuario("Diego Legarda " , "dflegarda@gmail.com")
print(usuario1.saludar())
print(usuario2.plataforma)
 

respuesta=usuario1.saludar()
print(usuario2.plataforma)