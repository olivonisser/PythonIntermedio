def abrir_archivo(nombre):
    try:
        archivo= open(nombre, "r")
        return archivo
    except FileNotFoundError:
        try:
            archivo = open(nombre, "w")
            print(f"El archivo '{nombre}' creado exitosamente")
            return archivo
        except Exception as e:
            return f"No se pudo crear el archivo '{nombre}' debido a: {e}"


nombre_archivo = input("Indique el nombre del archivo a buscar: ")

archi= abrir_archivo(nombre_archivo)

if archi:
    print(f"Archivo '{nombre_archivo}' abierto correctamente")
    archi.close()