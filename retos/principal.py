# principal.py

import retos
import utilerias


def ejercicio_1():
    utilerias.mostrar_titulo("COMISIÓN DE VENTAS")

    ventas = utilerias.leer_float("Ingrese las ventas: ")
    porcentaje = utilerias.leer_float("Ingrese el porcentaje de comisión: ")

    comision = retos.calcular_comision(ventas, porcentaje)

    print(f"\nComisión: {comision:.2f}")


def ejercicio_2():
    utilerias.mostrar_titulo("CLASIFICACIÓN DE CAFÉ")

    humedad = utilerias.leer_float("Ingrese el porcentaje de humedad: ")

    resultado = retos.clasificar_cafe(humedad)

    print(f"\nClasificación: {resultado}")


def ejercicio_3():
    utilerias.mostrar_titulo("TARIFA DE ENTREGA")

    distancia = utilerias.leer_float("Ingrese la distancia en km: ")
    zona = input("Ingrese la zona (urbana/rural): ")

    tarifa = retos.calcular_tarifa(distancia, zona)

    if tarifa is None:
        print("Zona no válida.")
    else:
        print(f"Tarifa de entrega: {tarifa:.2f}")


def ejercicio_4():
    utilerias.mostrar_titulo("RESUMEN SEMANAL")

    ventas = []

    for dia in range(1, 8):
        venta = utilerias.leer_float(
            f"Ingrese las ventas del día {dia}: "
        )
        ventas.append(venta)

    total, promedio, minima, maxima = retos.resumen_semanal(ventas)

    print(f"\nTotal: {total:.2f}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Venta mínima: {minima:.2f}")
    print(f"Venta máxima: {maxima:.2f}")


def ejercicio_5():
    utilerias.mostrar_titulo("INVENTARIO MÍNIMO")

    existencias = {}

    cantidad = utilerias.leer_entero(
        "Cantidad de productos: "
    )

    for i in range(cantidad):
        nombre = input(f"\nProducto {i + 1}: ")
        existencia = utilerias.leer_entero("Existencia: ")

        existencias[nombre] = existencia

    limite = utilerias.leer_entero(
        "\nIngrese el límite mínimo: "
    )

    productos = retos.inventario_minimo(
        existencias,
        limite
    )

    print("\nProductos que deben reponerse:")

    if productos:
        for producto in productos:
            print("-", producto)
    else:
        print("No hay productos por reponer.")


def ejercicio_6():
    utilerias.mostrar_titulo("CONVERSIÓN DE MONEDA")

    cantidad = utilerias.leer_float(
        "Ingrese la cantidad: "
    )

    tasa = utilerias.leer_float(
        "Ingrese la tasa de cambio: "
    )

    resultado = retos.convertir_moneda(
        cantidad,
        tasa
    )

    print(f"Resultado: {resultado:.2f}")


def ejercicio_7():
    utilerias.mostrar_titulo("NOTA FINAL")

    notas = []
    ponderaciones = []

    for i in range(3):
        nota = utilerias.leer_float(
            f"Nota {i + 1}: "
        )

        porcentaje = utilerias.leer_float(
            f"Ponderación de la nota {i + 1} (%): "
        )

        notas.append(nota)
        ponderaciones.append(porcentaje / 100)

    nota_final, clasificacion = retos.calcular_nota_final(
        notas,
        ponderaciones
    )

    print(f"\nNota final: {nota_final:.2f}")
    print(f"Clasificación: {clasificacion}")


def ejercicio_8():
    utilerias.mostrar_titulo("FACTURACIÓN MODULAR")

    producto = input("Producto: ")

    precio = utilerias.leer_float("Precio: ")
    cantidad = utilerias.leer_entero("Cantidad: ")

    subtotal = retos.calcular_subtotal(
        precio,
        cantidad
    )

    impuesto = retos.calcular_impuesto(subtotal)

    total = retos.calcular_total(
        subtotal,
        impuesto
    )

    print("\n----- FACTURA -----")
    print(f"Producto: {producto}")
    print(f"Precio: {precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Impuesto: {impuesto:.2f}")
    print(f"Total: {total:.2f}")


def mostrar_menu():
    print("""
========================================
          PRÁCTICA DE FUNCIONES
========================================
1. Comisión de ventas
2. Clasificación de café
3. Tarifa de entrega
4. Resumen semanal
5. Inventario mínimo
6. Conversión de moneda
7. Nota final
8. Facturación modular
0. Salir
========================================
""")


def main():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio_1()

        elif opcion == "2":
            ejercicio_2()

        elif opcion == "3":
            ejercicio_3()

        elif opcion == "4":
            ejercicio_4()

        elif opcion == "5":
            ejercicio_5()

        elif opcion == "6":
            ejercicio_6()

        elif opcion == "7":
            ejercicio_7()

        elif opcion == "8":
            ejercicio_8()

        elif opcion == "0":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida.")

        utilerias.pausar()


main()