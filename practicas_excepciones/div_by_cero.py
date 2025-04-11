def dividir(dividendo, divisor):

    try:
        resultado = dividendo/divisor
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir por cero."
    
primero= float(input("Ingresa el numero que se va a dividir: "))
segundo= float(input("Ingresa el numero por el cual se va a dividir: "))

resultado = dividir(primero, segundo)    

print("El calculo da como resultado: ", resultado)
