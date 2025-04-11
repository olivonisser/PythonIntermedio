def unirCadenas(a,b):
    try:
        union = a + int(b)
        return union
    except TypeError as e:
        return ("Se genero el siguiente error: ", e)

pCadena = input("Indique la primera cadena: ")
numero = float(input("Indique un numero: "))

resultado = unirCadenas(pCadena, numero)

print(resultado)



