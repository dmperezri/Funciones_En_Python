import os
# Las listas son mutables: se pueden modificar dentro de la función.
# Por eso, el cambio permanece en la lista original que se pasó como argumento.

def agregar(lista, producto):
    lista.append(producto)

inventario = []
agregar(inventario, "Café")
print(inventario)


# Los enteros son inmutables: no se pueden modificar directamente.
# Esta asignación crea un nuevo valor solo para la variable local "numero";
# por eso la variable "cantidad" fuera de la función conserva su valor.
def aumentar(numero):
    numero = numero + 1

cantidad = 5
aumentar(cantidad)
print(cantidad)


# MUTABLES
def eliminar_primero(lista):
    lista.pop(0)

frutas = ["Manzana", "Pera", "Plátano"]
eliminar_primero(frutas)
print(frutas)


def agregar_varios(lista, elementos):
    lista.extend(elementos)

colores = ["Rojo"]
agregar_varios(colores, ["Verde", "Azul"])
print(colores)

# INMUTABLES
def duplicar(numero):
    numero = numero * 2

edad = 20
duplicar(edad)
print(edad)


def restar_uno(numero):
    numero = numero - 1

vidas = 3
restar_uno(vidas)
print(vidas)

