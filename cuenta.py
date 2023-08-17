from persona import Persona
class Cuenta(Persona):
    def __init__(self,nombre, edad, dni ,cantidad=None):
        Persona.__init__(self, nombre, edad, dni)
        self._cantidad = cantidad

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
