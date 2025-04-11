def div_numeros(primero, segundo):
    try:
        pnum = float(primero)
        resultado = pnum / segundo
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except ValueError:
        return "El primer numero no es un numero valido"


priNum = input("Indique el primer numero: ")
segNum = input("Indique el segundo numero: ")

resultado= div_numeros(priNum, segNum)

print(resultado)
