import os
from funciones import funciones_de_practica
from argumentos import leer_datos, imprimir_datos
from argumentos import tasa
from argumentosMut import agregar, aumentar, eliminar_primero, agregar_varios, duplicar, restar_uno
def main():
     os.system("cls")
     print("Bienvenido al programa de funciones")
     print("1. Ejemplos de funciones")
     print("2. Ejemplos de arugumentos")
     print("3. Ejemplos de argumentos mutables e inmutables")
     opcion = input("Selecciona una opción: ")

     if opcion == "1":
          funciones_de_practica()
          input("Presione Enter para continuar...")
     elif opcion == "2":
          os.system("cls")
          cif, nombre, promedio, becado, carrera = leer_datos()
          imprimir_datos(cif, nombre, promedio, carrera, becado)
          input("Presione Enter para continuar...")
     elif opcion == "3":
          os.system("cls")
          print("Ejemplos de argumentos mutables e inmutables")
          match opcion:
               case "1":
                    inventario = []
                    agregar(inventario, "Café")
                    print("Inventario:", inventario)
               case "2":
                    cantidad = 5
                    aumentar(cantidad)
                    print("Cantidad:", cantidad)
               case "3":
                    frutas = ["Manzana", "Pera", "Plátano"]
                    eliminar_primero(frutas)
                    print("Frutas:", frutas)
               case "4":
                    colores = ["Rojo"]
                    agregar_varios(colores, ["Verde", "Azul"])
                    print("Colores:", colores)
               case "5":
                    edad = 20
                    duplicar(edad)
                    print("Edad:", edad)
               case "6":
                    vidas = 3
                    restar_uno(vidas)
                    print("Has perdido una vida.")
                    print("Vidas:", vidas)
               case _:
                    print("Opción inválida. Saliendo del programa.")
     else:
          print("Opción inválida. Saliendo del programa.")

     print(f"Tipo de cambio actual: {tasa} córdobas por dólar.")     
main()