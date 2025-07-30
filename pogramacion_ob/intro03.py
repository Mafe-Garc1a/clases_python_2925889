from datetime import datetime #importante cuando se va a trabajar con fechas y horas (de esta clase importar ste objeto{paquetes de python})
from typing import List
class Producto :
    # str ->imprime todo lo que hay dentro del objeto
    def __init__(self,id_producto:int,nombre:str , precio:float ,stock:int):
        self.id_producto=id_producto
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        self.fecha_creacion=datetime.now()

    def reducir_stock(self,cantidad:int)->bool: #booleano es true-false
        if self.stock>=cantidad:
            self.stock-=cantidad  # -=   esto es que disminuya lo que ya hay
            return True
        return False
    #el return es hasta donde llega la funcion
    def aumento_stock(self,cantidad:int):
        self.stock+=cantidad
        return int


    def __str__(self):
        return f"{self.nombre} - ${self.precio}(stock: {self.stock}) -fecha creacion : {self.fecha_creacion}"
print("-----PRODUCTOS------")
# producto1 = Producto(id_producto=1,nombre="Laptop",precio=150.00,stock=10)
# print(producto1)
# producto2 = Producto(id_producto=2,nombre="Monitor LG",precio=200.00,stock=20)
# print(producto2)
# print("--------------")
# # disminuir stock
# exito= producto1.reducir_stock(3)
# print("reduccion exitosa?" , exito)
# print(producto1)
# print("-------------------")
# exito2= producto1.aumento_stock(3)
# print("reduccion exitosa?" , exito2)
# print(producto1)

# una clase pueede ser un tipo de dato (producto:Producto)
class CarritoCompras:
    # cuando cree un producto tiene que manar esto datos
    def __init__(self , usuario_id :int):
        self.usuario_id=usuario_id
        self.productos:List[dict]=[]
        self.fecha_creacion=datetime.now()
    def agregar_producto(self ,producto:Producto, cantidad:int)->bool:
        if producto.stock>=cantidad:
            item ={
                'producto':producto,
                'cantidad':cantidad,
                'precio_unitario':producto.precio,
            }
            self.productos.append(item)
            return True
        return False
    def calcular_total(self)->float:
        total=0
        for item in self.productos:
            total+=item['precio_unitario']*item['cantidad']
        return total
    def obtener_resumen(self)->str:
        resumen=f"carrito del usuario {self.usuario_id}:\n"
        for item in self.productos:
            producto=item["producto"]
            cantidad=item["cantidad"]
            subtotal=item["precio_unitario"]*cantidad
            resumen+=f"{producto.nombre}x{cantidad}={subtotal}\n"
        resumen+=f"total : ${self.calcular_total():.2f}"
        return resumen
    def confirmar_compra(self):
        for item in self.productos:
            producto =item['producto']
            cantidad =item['cantidad']
        producto.reducir_stock(cantidad)
    
# crear productos
producto1=Producto(1,"laptop",1500.0,10)
producto2=Producto(2,"mouse",25.0,50)
producto3=Producto(3,"teclado",45.0,30)
# creando un objeto 
carrito=CarritoCompras(usuario_id=1001)
carrito.agregar_producto(producto1,1)
carrito.agregar_producto(producto2,5)
carrito.agregar_producto(producto3,4)

carrito.confirmar_compra()
print(producto1)
print(producto2)
print(producto3)
print(f"{carrito.obtener_resumen()}")
total=carrito.calcular_total()
print(f"total carrito: ${total:.2f}")



# 2f->es para que saque el dat con 2 decimales
