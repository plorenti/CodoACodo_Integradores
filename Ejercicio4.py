def PalabrasRepetidas(texto):
  
    palabras = texto.split()
    repetidos = {}

    for palabra in palabras:
        if palabra in repetidos:
            repetidos[palabra]+=1
        else:
            repetidos[palabra]=1    

    return repetidos

def PalabraMasUsada(palabras):
    mas_usada=max(palabras,key=palabras.get)
    veces= palabras[mas_usada]

    return (mas_usada, veces)


texto=input("INGRESE UN TEXTO: ")
palabras =PalabrasRepetidas(texto)
print(PalabraMasUsada(palabras))
