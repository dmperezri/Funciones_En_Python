# utilerias.py


def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))

            if valor < 0:
                print("El valor no puede ser negativo.")
                continue

            return valor

        except ValueError:
            print("Ingrese un número válido.")


def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))

            if valor < 0:
                print("El valor no puede ser negativo.")
                continue

            return valor

        except ValueError:
            print("Ingrese un número entero válido.")


def pausar():
    input("\nPresione Enter para continuar...")


def mostrar_titulo(titulo):
    print("\n" + "=" * 40)
    print(titulo.center(40))
    print("=" * 40)