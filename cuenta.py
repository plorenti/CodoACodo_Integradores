from persona import Persona
class Cuenta(Persona):
    def __init__(self,titular=None,cantidad=None):
        self._Persona = titular
        self._cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self._Persona.nombre} - Edad: {self._Persona.edad} - DNI: {self._Persona.dni}")
        print(f"Saldo: ${self._cantidad}")

    @property
    def persona(self):
        return self._Persona

    @persona.setter
    def persona(self,titular):
        self._Persona = titular

    @property
    def cantidad(self):
        return self._cantidad


    
    def ingresar(self,cantidad):
        saldo_anterior = self._cantidad        
        if cantidad >0:
            self._cantidad +=cantidad
            print(f"El saldo se modificó de ${saldo_anterior} a ${self.cantidad}")
        else:
            print(f"No se han realizado modificaciones el saldo es ${self._cantidad}")

    def retirar(self,cantidad):
        saldo_anterior = self._cantidad        
        if cantidad >0:
            self._cantidad -=cantidad
            print(f"El saldo se modificó de ${saldo_anterior} a ${self.cantidad}")
        else:
            print(f"No se han realizado modificaciones el saldo es ${self._cantidad}")
