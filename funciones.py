def puede_entrar(edad, tiene_entrada):
    if edad >= 18 and tiene_entrada.lower() == "si":
        return True
    else:
        return False
    
def archivar_asistentes(lista_asistentes):
    with open("registro_asistentes.txt", "w") as archivo:
        archivo.write("-----Registro de la noche-----\n")
        for persona in lista_asistentes:
            linea = f"Nombre: {persona['nombre']} | Edad: {persona['edad']}\n"
            archivo.write(linea)

def cargar_asistentes():
    lista_temporal = []
    try:
        with open("registro_asistentes.txt", "r") as archivo:
            next(archivo)
            for linea in archivo:
                partes = linea.strip().split(" | ")
                nom = partes[0].replace("Nombre: ", "")
                ed = int(partes[1].replace("Edad: ", ""))
                cliente = {"nombre": nom, "edad": ed}
                lista_temporal.append(cliente)
    except FileNotFoundError:
        print("No hay registros previos. Iniciando lista vacia...")
    return lista_temporal
