import os

RUTA = "/tmp/registro_asistentes.txt" if os.environ.get("VERCEL") else "registro_asistentes.txt"

def puede_entrar(edad, tiene_entrada):
    if edad >= 18 and tiene_entrada.lower() == "si":
        return True
    else:
        return False

def archivar_asistentes(lista_asistentes):
    with open(RUTA, "w") as archivo:
        archivo.write("-----Registro de la noche-----\n")
        for persona in lista_asistentes:
            linea = f"Nombre: {persona['nombre']} | Edad: {persona['edad']}\n"
            archivo.write(linea)

def cargar_asistentes():
    lista_temporal = []
    if not os.path.exists(RUTA):
        return []
        
    try:
        with open(RUTA, "r") as archivo:
            next(archivo)
            for linea in archivo:
                if not linea.strip(): continue
                partes = linea.strip().split(" | ")
                nom = partes[0].replace("Nombre: ", "")
                ed = int(partes[1].replace("Edad: ", ""))
                cliente = {"nombre": nom, "edad": ed}
                lista_temporal.append(cliente)
    except (FileNotFoundError, IndexError, ValueError):
        print("Error al cargar registros. Iniciando lista vacía...")
        return []
        
    return lista_temporal