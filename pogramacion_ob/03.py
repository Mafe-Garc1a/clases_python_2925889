# 1. Encapsulación
# La encapsulación es uno de los pilares de la Programación Orientada a Objetos (POO).
# Consiste en ocultar los detalles internos de implementación y permitir el acceso
# solo a través de métodos definidos (interfaz pública).
# Esto ayuda a proteger los datos, mantener la integridad y facilitar el mantenimiento del código.

from datetime import datetime  # Para registrar la fecha y hora de cada transacción
from typing import List        # Para especificar que una lista contendrá elementos tipo dict


# Definimos la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        # El titular de la cuenta es público
        self.titular = titular

        # __saldo y __historial están precedidos por doble guion bajo (__) lo que los convierte en atributos *privados*
        # Esto significa que no deben ser accedidos directamente desde fuera de la clase.
        self.__saldo = saldo_inicial
        self.__historial = []

    # Método público para depositar dinero en la cuenta
    def depositar(self, cantidad: float) -> bool:
        if cantidad > 0:
            self.__saldo += cantidad  # Se actualiza el saldo
            self.__registrar_transaccion("Depósito", cantidad)  # Se registra la transacción
            return True
        return False  # No se acepta una cantidad negativa o cero

    # Método público para retirar dinero de la cuenta
    def retirar(self, cantidad: float) -> bool:
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            self.__registrar_transaccion("Retiro", cantidad)
            return True
        return False  # Rechaza el retiro si no hay suficiente saldo o la cantidad es inválida

    # Método público para consultar el saldo actual
    def consultar_saldo(self) -> float:
        return self.__saldo  # Aunque __saldo es privado, este método permite acceder de forma segura

    # Método privado para registrar los movimientos en el historial
    def __registrar_transaccion(self, tipo: str, cantidad: float):
        transaccion = {
            'fecha': datetime.now(),  # Fecha y hora actual
            'tipo': tipo,             # Tipo de transacción: Depósito o Retiro
            'cantidad': cantidad,     # Monto involucrado
            'saldo_resultante': self.__saldo  # Saldo después de la transacción
        }
        self.__historial.append(transaccion)

    # Método público para obtener el historial de transacciones
    def obtener_historial(self) -> List[dict]:
        return self.__historial.copy()  # Retorna una copia del historial para evitar que se modifique desde afuera


# ------------------ EJEMPLO PRINCIPAL DE USO ------------------

# Creamos una cuenta nueva con un saldo inicial de $1000
cuenta = CuentaBancaria("María Rodríguez", 1000)

# Realizamos un depósito de $500
cuenta.depositar(500)

# Realizamos un retiro de $200
cuenta.retirar(200)

# Consultamos el saldo actual
print(f"Saldo: ${cuenta.consultar_saldo()}")  # Saldo: $1300

# print(cuenta.__saldo)  # Esto lanzaría un error, ya que __saldo es privado y no puede accederse directamente

# ------------------ MÁS EJEMPLOS DE USO PARA PRACTICAR ------------------

# 1. Cuenta con saldo inicial cero
cuenta1 = CuentaBancaria("Juan Pérez")
cuenta1.depositar(100)
cuenta1.retirar(50)
print(f"\nSaldo de {cuenta1.titular}: ${cuenta1.consultar_saldo()}")
print("Historial:", cuenta1.obtener_historial())

# 2. Intento de retiro sin fondos suficientes
cuenta2 = CuentaBancaria("Ana Torres", 200)
exito = cuenta2.retirar(500)  # Esto debería fallar
print(f"\n¿Retiro exitoso? {exito}")
print(f"Saldo de {cuenta2.titular}: ${cuenta2.consultar_saldo()}")
print("Historial:", cuenta2.obtener_historial())

# 3. Cuenta con múltiples depósitos y retiros
cuenta3 = CuentaBancaria("Carlos Gómez", 500)
cuenta3.depositar(300)
cuenta3.retirar(200)
cuenta3.depositar(150)
cuenta3.retirar(100)
print(f"\nSaldo de {cuenta3.titular}: ${cuenta3.consultar_saldo()}")
for transaccion in cuenta3.obtener_historial():
    print(transaccion)

# 4. Acceso seguro al historial (demuestra que es una copia)
historial = cuenta3.obtener_historial()
historial.append({'tipo': 'Hackeo', 'cantidad': 99999})  # Esto no modifica el historial original
print(f"\nHistorial real de {cuenta3.titular}:")
print(cuenta3.obtener_historial())  # Se mantiene intacto
