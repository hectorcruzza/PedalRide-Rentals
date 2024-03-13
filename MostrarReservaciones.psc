Algoritmo MostrarReservaciones
	Definir correo_electronico Como Cadena
	Definir reservaciones_confirmadas Como Logico
	Definir i Como Entero
	Dimension reservaciones(3, 6)
	reservaciones(1, 1) = "01"
	reservaciones(1, 2) = "13/03/2024"
	reservaciones(1, 3) = "10:00 - 11:00"
	reservaciones(1, 4) = "067"
	reservaciones(1, 5) = "$60"
	reservaciones(1, 6) = "jorge@gmail.com"
	
	reservaciones(2, 1) = "02"
	reservaciones(2, 2) = "15/03/2024"
	reservaciones(2, 3) = "12:00 - 13:00"
	reservaciones(2, 4) = "054"
	reservaciones(2, 5) = "$60"
	reservaciones(2, 6) = "jorge@gmail.com"
	
	reservaciones(3, 1) = "03"
	reservaciones(3, 2) = "21/03/2024"
	reservaciones(3, 3) = "10:00 - 16:00"
	reservaciones(3, 4) = "103"
	reservaciones(3, 5) = "$360"
	reservaciones(3, 6) = "hector@gmail.com"
	
	correo_electronico = ""
	reservaciones_confirmadas = Falso
	
	Escribir Sin Saltar "Ingrese su correo electrónico: "
	Leer correo_electronico
	
	Escribir ""
	Escribir "Sección: Mis reservaciones."
	Escribir "- Reservaciones confirmadas:"
	Escribir ""
	
	i = 1
	
	Mientras NO reservaciones_confirmadas Y i <= 3 Hacer
		Si correo_electronico = reservaciones(i, 6) Entonces
			reservaciones_confirmadas = Verdadero
		FinSi
		i = i + 1
	FinMientras
	
	Si reservaciones_confirmadas Entonces
		Escribir "| N.° de Reservación |   Fecha   |    Horario    | N.° de Bicicleta | Costo |"
		Para j = 1 Hasta 3 Con Paso 1 Hacer
			Si correo_electronico = reservaciones(j, 6) Entonces
				Escribir  "          ", reservaciones(j, 1), "          ", reservaciones(j, 2), "   ", reservaciones(j, 3), "         ", reservaciones(j, 4), "           ", reservaciones(j, 5),"           "
			FinSi
		FinPara
	SiNo
		Escribir "No tiene ninguna reservación confirmada."
	FinSi
FinAlgoritmo
