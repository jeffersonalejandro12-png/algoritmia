total_recaudado = 0
contador_autos = 0

precio_actual = int(input("Digite el costo del servicio (0 para cerrar caja): "))

while precio_actual != 0:
    total_recaudado += precio_actual
    contador_autos += 1
    precio_actual = int(input("Digite el costo del siguiente vehículo (0 para cerrar caja): "))

print(f"Dinero total reunido: ${total_recaudado}")
print(f"Total de autos atendidos: {contador_autos}")