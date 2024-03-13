Algoritmo HoraMayorQueOtra
	Definir cantidad_reservaciones, primer_elemento_hora_inicio_int, segundo_elemento_hora_inicio_int, primer_elemento_hora_termino_int, segundo_elemento_hora_termino_int, i, j Como Entero
	Definir hora_inicio_reserva, hora_termino_reserva, primer_elemento_hora_inicio_str, segundo_elemento_hora_inicio_str, primer_elemento_hora_termino_str, segundo_elemento_hora_termino_str Como Cadena
	Definir condicion, reservaciones_disponibles Como Logico
	cantidad_reservaciones = 4
	hora_inicio_reserva = ""
	hora_termino_reserva = ""
	primer_elemento_hora_inicio_str = ""
	segundo_elemento_hora_inicio_str = ""
	primer_elemento_hora_termino_str = ""
	segundo_elemento_hora_termino_str = ""
	primer_elemento_hora_inicio_int = 0
	segundo_elemento_hora_inicio_int = 0
	primer_elemento_hora_termino_int = 0
	segundo_elemento_hora_termino_int = 0
	Dimension reservaciones(cantidad_reservaciones, 3)
	reservaciones(1, 1) = "08:00"
	reservaciones(1, 2) = "10:00"
	reservaciones(1, 3) = "067"
	reservaciones(2, 1) = "13:00"
	reservaciones(2, 2) = "14:00"
	reservaciones(2, 3) = "045"
	reservaciones(3, 1) = "16:00"
	reservaciones(3, 2) = "20:00"
	reservaciones(3, 3) = "010"
	reservaciones(4, 1) = "08:00"
	reservaciones(4, 2) = "11:00"
	reservaciones(4, 3) = "004"

	Escribir "Sección: Hacer una reservación."
	Escribir "- Nuestro horario de trabajo es de las 08:00 a las 20:00."
	Escribir "- Las reservaciones se deben realizar con al menos una hora de anticipación. "
	Escribir "- Las reservaciones se realizan en bloques por hora. "
	Escribir "-  Las reservaciones pueden ser de más de una hora."
	Escribir Sin Saltar "- Ingrese la hora de inicio de la reservación (Formato de 24 horas: 13:00): "
	Leer hora_inicio_reserva
	
	condicion = Verdadero
	i = 1
	
	Mientras condicion Hacer
		elemento = SubCadena(hora_inicio_reserva, i, i)
		Si elemento = ":" Entonces
			primer_elemento_hora_inicio_str = SubCadena(hora_inicio_reserva, 1, i - 1)
			segundo_elemento_hora_inicio_str = SubCadena(hora_inicio_reserva, i + 1, Longitud(hora_inicio_reserva))
			condicion = Falso
		FinSi
		i = i + 1
	FinMientras
	
	Si primer_elemento_hora_inicio_str = "8" O primer_elemento_hora_inicio_str = "9" Entonces
		hora_inicio_reserva = "0" + primer_elemento_hora_inicio_str + ":" + segundo_elemento_hora_inicio_str
	FinSi
	
	Escribir "Hora de Inicio (String): ", hora_inicio_reserva, "." 
	
	primer_elemento_hora_inicio_int = ConvertirANumero(primer_elemento_hora_inicio_str)
	segundo_elemento_hora_inicio_int = ConvertirANumero(segundo_elemento_hora_inicio_str)
	
	Escribir "Hora de Inicio (Entero): ", primer_elemento_hora_inicio_int, ":", segundo_elemento_hora_inicio_int, "."
	
	Escribir Sin Saltar "- Ingrese la hora de término de la reservación (Formato de 24 horas: 20:00): "
	Leer hora_termino_reserva
	
	condicion = Verdadero
	i = 1
	
	Mientras condicion Hacer
		elemento = SubCadena(hora_termino_reserva, i, i)
		Si elemento = ":" Entonces
			primer_elemento_hora_termino_str = SubCadena(hora_termino_reserva, 1, i - 1)
			segundo_elemento_hora_termino_str = SubCadena(hora_termino_reserva, i + 1, Longitud(hora_termino_reserva))
			condicion = Falso
		FinSi
		i = i + 1
	FinMientras
	
	Si primer_elemento_hora_termino_str = "8" O primer_elemento_hora_termino_str = "9" Entonces
		hora_termino_reserva = "0" + primer_elemento_hora_termino_str + ":" + segundo_elemento_hora_termino_str
	FinSi
	
	Escribir "Hora de Término (String): ", hora_termino_reserva, "." 
	
	primer_elemento_hora_termino_int = ConvertirANumero(primer_elemento_hora_termino_str)
	segundo_elemento_hora_termino_int = ConvertirANumero(segundo_elemento_hora_termino_str)
	
	Escribir "Hora de Término (Entero): ", primer_elemento_hora_termino_int, ":", segundo_elemento_hora_termino_int, "."
	
	reservaciones_disponibles = Falso
	j = 1
	
	Mientras NO reservaciones_disponibles Y j <= cantidad_reservaciones Hacer
		container_primer_elemento_hora_termino_reserva = ConvertirANumero(SubCadena(reservaciones(j, 2), 1, 2))
		Si primer_elemento_hora_inicio_int >= container_primer_elemento_hora_termino_reserva Entonces
			reservaciones_disponibles = Verdadero
		FinSi
		j = j + 1
	FinMientras
	
	Si reservaciones_disponibles Entonces
		Escribir "- A continuación, se muestra la lista de bicicletas disponibles en la fecha elegida:"
		Escribir ""
		Escribir "| Número de Bicicleta |"
		Para h = 1 Hasta cantidad_reservaciones Con Paso 1 Hacer
			container_primer_elemento_hora_termino_reserva = ConvertirANumero(SubCadena(reservaciones(h, 2), 1, 2))
			Si primer_elemento_hora_inicio_int >= container_primer_elemento_hora_termino_reserva Entonces
				Escribir "          ", reservaciones(h, 3)
			FinSi
		FinPara
	SiNo
		Escribir "No hay bicicletas disponibles para el horario elegido."
	FinSi
FinAlgoritmo
