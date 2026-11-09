unidades = int(input("Escribe las unidades: "))

if unidades < 0:
    print("Error: Las unidades no pueden ser negativas.")
elif unidades == 0:
    print("Rojo: Agotado.")
elif unidades <= 10:
    print("Amarillo: Pedir.")
else:
    print("Verde: Disponible.")