suma_notas = 0
total_aprobados = 0
hay_reprobados = False

for i in range(1, 6):
    nota = float(input(f"Digite la nota del alumno {i} (1.0 a 5.0): "))
    
    suma_notas += nota
    
    if nota >= 3.0:
        total_aprobados += 1
    else:
        hay_reprobados = True
        
    # Control para hallar la nota más alta y la más baja
    if i == 1:
        nota_mayor = nota
        nota_menor = nota
    else:
        if nota > nota_mayor:
            nota_mayor = nota
        if nota < nota_menor:
            nota_menor = nota

print("-" * 45)
print(f"Promedio general: {suma_notas / 5}")
print(f"Estudiantes que aprobaron: {total_aprobados}")
print(f"La nota más alta fue: {nota_mayor}")
print(f"La nota más baja fue: {nota_menor}")

if hay_reprobados:
    print("¿Hubo algún reprobado?: Sí")
else:
    print("¿Hubo algún reprobado?: No")