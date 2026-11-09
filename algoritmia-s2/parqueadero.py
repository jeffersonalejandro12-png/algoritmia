tipo = int(input("Tipo de vehículo (1 = carro, 2 = moto): "))
minutos = int(input("Minutos de permanencia: "))
factura = input("¿Tiene factura de compra? (S/N): ").upper()

# no-negativos
if minutos < 0:
    print("Los minutos no pueden ser negativos.")
else:
    # tarifa según tipo de vehículo
    if tipo == 1:
        tarifa = 4000
    elif tipo == 2:
        tarifa = 2000
    else:
        tarifa = 0

    # validar si el tipo de vehículo existe
    if tarifa == 0:
        print("Tipo de vehículo no válido.")
    else:
        # calculo del total a pagar
        if minutos <= 15:
            total = 0
        else:
            horas = (minutos + 59) // 60
            total = horas * tarifa
            
            # tope máximo
            if total > 30000:
                total = 30000
                
            # descuento por factura
            if factura == "S":
                total = total / 2
                
        print("El valor a pagar es: $", int(total))