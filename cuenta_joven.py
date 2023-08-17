from cuenta import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self,nombre, edad, dni, cantidad, bonificacion):
        Cuenta.__init__(self,nombre,edad,dni,cantidad)
        self._bonifiacion=bonificacion

    @property
    def bonificacion(self):
        return self._bonifiacion
    
    @bonificacion.setter
    def bonificacion(self,porcentaje):
        self._bonifiacion=porcentaje

    def es_titular_valido(self):
        
        if self.edad < 25:
            return True
        else:
            return False
        
    def retirar(self,cantidad):
        if self.es_titular_valido():
             super().retirar(cantidad)
        else:
            print(f"No es un titular válido para retirar ${cantidad}")

    def detalle(self):
        print(f"Cuenta joven")        
        print(f"Bonificacion: {self._bonifiacion}%")
        