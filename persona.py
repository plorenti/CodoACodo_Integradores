class Persona:
    def __init__(self, nombre=None,edad=None,dni=None):
        self._nombre=nombre
        self._edad=edad
        self._dni=dni

    def mostrar(self):
        print(f"Nombre: {self._nombre} - Edad: {self._edad} - DNI: {self._dni}")

    def es_mayor_de_edad(self):
        if self._edad >=18:
            return True
        else:
            return False

    @property
    def nombre(self):
        return self._nombre    
    
    @nombre.setter
    def nombre(self,nombre):
        if nombre != "":
            self._nombre=nombre
        else:
            print("El nombre no puede estar vacio")    

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        try:
            if edad < 0:
                print("La edad no puede ser menos a 0")
            else:
                self._edad=edad
        except TypeError:
            print("Dato no válido, ingrese solamente numeros enteros")        
        
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni):
        if len(dni) < 8:
           print("El DNI tiene que teer al menos 8 numeros. Complete con 0 a la izquierda de ser necesario")
        else:
           self._dni=dni
