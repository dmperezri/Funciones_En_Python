# Dannia Maria Perez Rivera
import os

from sympy import true

tasa = 36.80
def imprimir_datos(cif, nombre, promedio, carrera, beca):
    os.system("cls")
    if (promedio >= 85) and (beca == true):
        status = "Renovada"
    elif (promedio <= 85) and (beca == true):
        status = "Renovada"
    else:
        status = "No becado"

    print("=" * 35)
    print("      DATOS DEL ESTUDIANTE")
    print(f"CIF: {cif}") # Interpolacion de cadenas
    print(f"Nombre: {nombre}")
    print(f"Promedio: {promedio}")
    print(f"Carrera: {carrera}")
    if beca == true:
        print("Beca: Revovada")
    else:
        print("Beca: No renovada")
    print(f"Status: {status}")
    print("=" * 35)

def leer_datos():
    os.system("cls")
    print("=" * 35)
    print("      DATOS DEL ESTUDIANTE")
    cif = input("Ingrese el CIF del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    while True:
        try:
            promedio = float(input("Ingrese el promedio del estudiante: "))
            break
        except ValueError:
            print("Ingrese un número válido para el promedio.")
    carrera = input("Ingrese la carrera del estudiante: ")
    beca = input("¿Tiene beca? (si/no): ")
    if beca.strip().lower() == "si":
        becado = True
    else:
        becado = False
    return cif, nombre, promedio, becado, carrera