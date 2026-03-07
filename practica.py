from funciones import*
from datetime import datetime

asistencias = cargar_asistentes()
cont = 0

while True:
    nombre_input = input("Ingrese su nombre completo o 'salir': ")

    if nombre_input.lower() == "salir":
        print("Cerrando programa...")
        break

    edad_input = input("Ingrese su edad: ")
    
    nombre = nombre_input

    try:
        edad = int(edad_input)
    except ValueError:
        print("Error! Ingresa la edad con numero")
        continue

    tiene_entrada = input("¿Tienes entrada? ")
    
    if puede_entrar(edad, tiene_entrada):
        datos_cliente = {
                "nombre" : nombre.upper(),
                "edad" : edad,
                "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
                }
        asistencias.append(datos_cliente)
        print("Bienvenido al club!")
    else:
        print("Acceso denegado")


total = len(asistencias)
print(f"Total de asistencias: {total}")
for i in asistencias:
    cont += 1
    print(f"Asistencia numero {cont}  Nombre: {i['nombre']}  Edad: {i['edad']}")
if cont == 0:
    print("No hubo asistencias")

archivar_asistentes(asistencias)
