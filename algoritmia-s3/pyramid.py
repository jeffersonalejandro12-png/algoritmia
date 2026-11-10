total_filas = int(input("Ingrese cuántos pisos tendrá la pirámide: "))

for r in range(1, total_filas + 1):
    # Espacios en blanco a la izquierda
    for esp in range(total_filas - r):
        print(" ", end="")
        
    # Asteriscos centrados
    for ast in range(2 * r - 1):
        print("*", end="")
        
    print()