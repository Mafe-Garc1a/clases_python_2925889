# fastapi es para crear apis

from fastapi import FastAPI #LLAMANDO A FAST API
from pydantic import BaseModel

app=FastAPI() #un objeto clase FastAPI
    
# un objeto creado d ela clase fast api con un metodo que recibe una ruta (get) y recibe parametros(rutas{'/'})
# dentro de funcion es logica
# esto es una api
class Item(BaseModel):
    name:str
    price:float
    estate:bool
    


@app.get('/')
def inicio():
    message="Hello World"
    name="Mafe Garcia"
    return{
        'message' :message,
        'name' :name
    }
    
@app.get('/suma')
# recibe los numeros con parametros                                                                    
def suma(num1:int , num2:int):
    
    resultado=num1+num2
    return{
        f"message : sumar , {num1} y {num2}",
        f"resultado : {resultado}"
    }
@app.get('/cubo')
def cubo():
    num1=30
    resultado=num1*num1*num1
    return{
        f"meesage : {num1} al cubo",
        f"resultado : {resultado}"
    }
# rutas puede llevar -  pero las funciones no
@app.post('/guardar-producto')
def guardar_producto(producto:Item , cuantity:int ):
    total=producto.price*cuantity
    return {
        f'message : almacenado con exito',
        f"name : {producto.name}"
        f"price : {producto.price}"
        f"cantidad{cuantity}"
        f"estate: {producto.estate}"
        f"total{total}"
    }
# crear una lista de diccionario vacia fuera de todo para que quede global
# crear un esquema que se llame aprendiz y va a pedir el nombre , la edad , correo eletronico ,ficha
# crear en enpoit que reciba ese esquema  , lo almacene en la lista de diccionaros vacia y que retorne la lista de todos los que ah ido guardado