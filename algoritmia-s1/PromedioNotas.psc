Algoritmo CalcularPromedioNotas
	Definir n, i Como Entero
	Definir nota, suma, promedio Como Real
	Escribir 'Ingrese la cantidad de notas a evaluar:'
	Leer n
	Si n>0 Entonces
		suma <- 0
		Para i<-1 Hasta n Hacer
			Escribir 'Ingrese la nota ', i, ':'
			Leer nota
			suma <- suma+nota
		FinPara
		promedio <- suma/n
		Escribir 'El promedio final es: ', promedio
	SiNo
		Escribir 'La cantidad de notas debe ser mayor a cero.'
	FinSi
FinAlgoritmo
