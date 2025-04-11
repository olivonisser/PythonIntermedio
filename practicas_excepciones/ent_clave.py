def acceder(diccionario, posicion):
    try:
        contenido=diccionario[posicion]
        return contenido
    except KeyError:
        return f"La posicion '{posicion}' no existe en el diccionario ingresado"

dicc = {
    "Nombre":   "Juan",
    "Edad"  :   "25",
    "email" :   "info@prueba.com"
    }

lugar = input("Indique la posicion del diccionario a acceder: ")

resultado= acceder(dicc, lugar)

print(resultado)