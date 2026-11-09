año = int(input("Escribe el año que deseas consultar: "))

es_multiplo_de_4 = año % 4 == 0
no_es_siglo = año % 100 != 0
es_multiplo_de_400 = año % 400 == 0

if (es_multiplo_de_4 and no_es_siglo) or es_multiplo_de_400:
    print(año, "es bisiesto.")
else:
    print(año, "no es bisiesto.")