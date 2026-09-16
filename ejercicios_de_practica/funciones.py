import os


def convertir_a_dolares(cordobas):
    tasa = 36.80
    return cordobas / tasa

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal, porcentaje):
    return subtotal * porcentaje / 100

def leer_cantidad():
    while True:
        try:
            return int(input("Cantidad: "))
        except ValueError:
            print("Ingrese un número entero.")

def mostrar_encabezado(nombre_empresa):
    print("=" * 35)
    print(nombre_empresa.upper())
    print("=" * 35)

def calcular_total(subtotal, impuesto=0.15):
    monto_impuesto = subtotal * impuesto
    total = subtotal + monto_impuesto
    return total

def funciones_de_practica():
    os.system("cls")
    print("¿Qué quieres hacer?")
    print("1. Convertir córdobas a dólares")
    print("2. Calcular subtotal y porcentaje de descuento")
    print("3. Leer cantidad de productos")
    print("4. Mostrar encabezado de la empresa")
    print("5. Calcular total con impuesto")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        os.system("cls")
        monto = float(input("Monto en córdobas: "))
        resultado = convertir_a_dolares(monto)
        print("Equivalente en dólares:", round(resultado, 2))

    elif opcion == "2":
        subtotal = calcular_subtotal(120, 5)
        descuento = aplicar_descuento(subtotal, 10)
        total = subtotal - descuento

        print("Total C$:", total)

    elif opcion == "3":
        os.system("cls")
        cantidad = leer_cantidad()
        print("Dato recibido:", cantidad)

    elif opcion == "4":
        os.system("cls")
        resultado = mostrar_encabezado("Cafetería El Buen Sabor")
        print("Valor devuelto:", resultado)

    elif opcion == "5":
        os.system("cls")
        print(calcular_total(1000))
        print(calcular_total(1000, 0.10))

    else:
        print("Opción no válida.")

