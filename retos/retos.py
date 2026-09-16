# retos.py

def calcular_comision(ventas, porcentaje):
    return ventas * porcentaje / 100


def clasificar_cafe(humedad):
    if 10 <= humedad <= 12:
        return "Aceptado"
    return "Revisar"


def calcular_tarifa(distancia, zona):
    zona = zona.lower()

    if zona == "urbana":
        return distancia * 10
    elif zona == "rural":
        return distancia * 15

    return None


def resumen_semanal(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    minima = min(ventas)
    maxima = max(ventas)

    return total, promedio, minima, maxima


def inventario_minimo(existencias, limite):
    productos_reponer = []

    for producto, cantidad in existencias.items():
        if cantidad <= limite:
            productos_reponer.append(producto)

    return productos_reponer


# EJERCICIO 6
def convertir_moneda(cantidad, tasa):
    return cantidad * tasa


# EJERCICIO 7
def calcular_nota_final(notas, ponderaciones):
    nota_final = 0

    for nota, ponderacion in zip(notas, ponderaciones):
        nota_final += nota * ponderacion

    if nota_final >= 90:
        clasificacion = "Excelente"
    elif nota_final >= 80:
        clasificacion = "Muy bueno"
    elif nota_final >= 70:
        clasificacion = "Bueno"
    elif nota_final >= 60:
        clasificacion = "Aprobado"
    else:
        clasificacion = "Reprobado"

    return nota_final, clasificacion


# EJERCICIO 8
def calcular_subtotal(precio, cantidad):
    return precio * cantidad


def calcular_impuesto(subtotal, porcentaje=15):
    return subtotal * porcentaje / 100


def calcular_total(subtotal, impuesto):
    return subtotal + impuesto