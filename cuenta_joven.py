from cuenta import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self,cuenta,bonificacion):
        self._cuenta=cuenta
        self._bonifiacion=bonificacion

    @property
    def bonificacion(self):
        return self._bonifiacion
    
    @bonificacion.setter
    def bonificacion(self,porcentaje):
        self._bonifiacion=porcentaje

    def es_titular_valido(self):
        
        if self._cuenta.persona.edad < 25:
            return True
        else:
            return False
        
    def retiro(self,cantidad):
        if self.es_titular_valido():
             self._cuenta.retirar(cantidad)
        else:
            print(f"No es un titular válido para retirar ${cantidad}")

    def mostrar(self):
        print(f"Cuenta joven")        
        print(f"Bonificacion: {self._bonifiacion}%")