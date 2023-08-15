#Escribir una función que calcule el máximo común divisor entre dos números
def MaximoComunDivisor(num1, num2):
    '''
    Funcion basada en el algoritmo de Euclides (buscado por internet)
    '''
    numeros =[num1,num2]
    #veo si en la lista hay un negativo y lo paso a positivo
    for i in range(len(numeros)):
        if numeros[i]<0:
            numeros[i]= numeros[i]*-1
    #los ordeno de mayor a menor porque el algoritmo asi lo requiere
    numeros = sorted(numeros, reverse=True)
    while(numeros[0]%numeros[1]!=0):
        numeros[0]=numeros[0]%numeros[1]
        numeros = sorted(numeros, reverse=True)
        
    return numeros[1]




a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resultado = MaximoComunDivisor(a,b)   
print(f"El minimo común divisor entre {a} y {b} es: {resultado}") 

#Escribir una función que calcule el mínimo común múltiplo entre dos números

'''
Basado en el algoritmo de Euclides se muliplican los dos numeros y se divide por
el minimo comun divisor
'''
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resultado = (a*b)/MaximoComunDivisor(a,b)   
print(f"El minimo común multiplo entre {a} y {b} es: {resultado}") 