from persona import Persona
from cuenta import Cuenta
from cuenta_joven import CuentaJoven

p = Persona("Pablo",26,"26932629")
p1=Persona("PAL",33,"123412125")
c = Cuenta(p,4000)
cj = CuentaJoven(c,25)

cj.retiro(1000)
cj.mostrar()
cj.retiro(500)

print(cj._cuenta.persona.mostrar())
cj._cuenta.persona.nombre = "Juan"
print(cj._cuenta.persona.mostrar())
