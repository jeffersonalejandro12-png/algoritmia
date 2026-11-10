def registrar_consumo():
    acumulado_total = 0

    precio_item = float(input("Digite el valor del plato (0 para salir): "))

    while precio_item != 0:
        unidades = float(input("Digite cuántos platos son: "))

        acumulado_total += precio_item * unidades

        precio_item = float(input("Digite el siguiente valor (0 para salir): "))

    return acumulado_total


def calcular_porcentaje(valor, porcentaje):
    return valor * porcentaje / 100


def mostrar_recibo(subtotal, impuesto, propina):
    print("=" * 50)
    print(f"Subtotal de la orden: ${subtotal}")
    print(f"Impuesto estimado (8%): ${impuesto}")
    print(f"Propina sugerida (10%): ${propina}")
    print(f"Gran total a cancelar: ${subtotal + impuesto + propina}")


subtotal_cuenta = registrar_consumo()
valor_impuesto = calcular_porcentaje(subtotal_cuenta, 8)
valor_propina = calcular_porcentaje(subtotal_cuenta, 10)

mostrar_recibo(subtotal_cuenta, valor_impuesto, valor_propina)