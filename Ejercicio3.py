def PalabrasRepetidas(texto):
  
    palabras = texto.split()
    repetidos = {}

    for palabra in palabras:
        if palabra in repetidos:
            repetidos[palabra]+=1
        else:
            repetidos[palabra]=1    

    return repetidos


print(PalabrasRepetidas("HOLA COMO ESTAS HOLA COMO VA"))