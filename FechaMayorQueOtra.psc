Algoritmo FechaMayorQueOtra
	Definir cantidad_reservaciones, dia_reserva, mes_reserva, i Como Entero
	Definir fecha_reserva Como Cadena
	Definir reservaciones_disponibles Como Logico
	cantidad_reservaciones = 5
	fecha_reserva = ""
	dia_reserva = 0
	mes_reserva = 0
	Dimension reservaciones(cantidad_reservaciones, 2)
	reservaciones(1, 1) = "13/03/2024"
	reservaciones(1, 2) = "067"
	reservaciones(2, 1) = "08/03/2024"
	reservaciones(2, 2) = "089"
	reservaciones(3, 1) = "12/03/2024"
	reservaciones(3, 2) = "005"
	reservaciones(4, 1) = "22/03/2024"
	reservaciones(4, 2) = "010"
	reservaciones(5, 1) = "30/03/2024"
	reservaciones(5, 2) = "043"
	
	Escribir "Sección: Hacer una reservación."
	Escribir "- Es importante mencionar que las reservaciones se deben realizar para el año y mes en curso."
	Escribir Sin Saltar "- Ingrese la fecha de la reservación (Formato: DD/MM/AAAA): "
	Leer fecha_reserva
	
	dia_reserva = ConvertirANumero(SubCadena(fecha_reserva, 1, 2))
	mes_reserva = ConvertirANumero(SubCadena(fecha_reserva, 4, 5))
	
	reservaciones_disponibles = Falso
	i = 1
	
	Mientras NO reservaciones_disponibles Y i <= cantidad_reservaciones Hacer
		container_dia_reserva = ConvertirANumero(SubCadena(reservaciones(i, 1), 1, 2))
		container_mes_reserva = ConvertirANumero(SubCadena(reservaciones(i, 1), 4, 5))
		Si mes_reserva >= container_mes_reserva Y dia_reserva >= container_dia_reserva Entonces
			reservaciones_disponibles = Verdadero
		FinSi
		i = i + 1
	FinMientras
	
	Si reservaciones_disponibles Entonces
		Escribir "- A continuación, se muestra la lista de bicicletas disponibles en la fecha elegida:"
		Escribir ""
		Escribir "| Número de Bicicleta |"
		Para j = 1 Hasta cantidad_reservaciones Con Paso 1 Hacer
			container_dia_reserva = ConvertirANumero(SubCadena(reservaciones(j, 1), 1, 2))
			container_mes_reserva = ConvertirANumero(SubCadena(reservaciones(j, 1), 4, 5))
			Si mes_reserva >= container_mes_reserva Y dia_reserva >= container_dia_reserva Entonces
				Escribir "          ", reservaciones(j, 2)
			FinSi
		FinPara
	SiNo
		Escribir "No hay bicicletas disponibles para la fecha elegida."
	FinSi
FinAlgoritmo