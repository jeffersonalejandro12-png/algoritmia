Algoritmo Propinas
	Escribir 'Cuenta: '
	Leer subtotal
	p_propina <- 0.1
	Escribir 'Personas para dividir cuenta: '
	Leer personas
	propina <- subtotal*0.1
	IVA <- subtotal*0.19
	total <- IVA+propina
	cada_uno <- total/personas
	Escribir 'El total es: ', total
	Escribir 'La propina es: ', propina
	Escribir 'Cada uno paga: ', cada_uno
FinAlgoritmo
