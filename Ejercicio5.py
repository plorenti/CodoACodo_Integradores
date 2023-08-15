def get_int_iterativa():
    while True:
        try:

            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("Valor no válido ingrese un numero entero")

def get_int_recursiva():
    try:
        numero= int(input("Ingrese un numero entero: "))
        return numero
    except ValueError:
        print("Valor no válido , intentelo de nuevo")
        return get_int_recursiva()
    
get_int_recursiva()
get_int_iterativa()