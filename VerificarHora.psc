Algoritmo VerificarHora
	Definir hora_actual, hora_inicio_reserva, hora_termino_reserva, primer_elemento_hora_inicio_str, segundo_elemento_hora_inicio_str, primer_elemento_hora_termino_str, segundo_elemento_hora_termino_str Como Cadena
	Definir primer_elemento_hora_actual_int, segundo_elemento_hora_actual_int, i, primer_elemento_hora_inicio_int, segundo_elemento_hora_inicio_int, primer_elemento_hora_termino_int, segundo_elemento_hora_termino_int Como Entero
	Definir diferencia_horas Como Real
	Definir condicion, hora_inicio_valida, hora_termino_valida, condiciones_horario, horario_valido Como Logico
	hora_actual = ConvertirATexto(HoraActual())
	primer_elemento_hora_actual_int = ConvertirANumero(Subcadena(hora_actual, 1, 1))
	segundo_elemento_hora_actual_int = ConvertirANumero(Subcadena(hora_actual, 2, Longitud(hora_actual) - 2))
	
	Si Longitud(hora_actual) <> 5 Entonces
		primer_elemento_hora_actual_int = ConvertirANumero(Subcadena(hora_actual, 1, 2))
		segundo_elemento_hora_actual_int = ConvertirANumero(Subcadena(hora_actual, 3, Longitud(hora_actual) - 2))
	FinSi
	
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
	diferencia_horas = 0
	
	Escribir "Hora de Actual: ", primer_elemento_hora_actual_int, ":", segundo_elemento_hora_actual_int "." 
	Escribir ""
	
	Escribir "Sección: Hacer una reservación."
	Escribir "- Nuestro horario de trabajo es de las 08:00 a las 20:00."
	Escribir "- Las reservaciones se deben realizar con al menos una hora de anticipación. "
	Escribir "- Las reservaciones se realizan en bloques por hora. "
	Escribir "- Las reservaciones pueden ser de más de una hora."
	
	// Verificar que el horario ingresado cumpla con las condiciones establecidas.
	Repetir
		// Verificar que la hora de inicio de la reservación sea válida.
		Repetir
			hora_inicio_valida = Falso
			
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
			
			Si (primer_elemento_hora_inicio_int >= 0 Y primer_elemento_hora_inicio_int <= 23) Y (segundo_elemento_hora_inicio_int >= 0 Y segundo_elemento_hora_inicio_int <= 59) Entonces
				hora_inicio_valida = Verdadero
			SiNo
				Escribir "La hora de inicio ingresada no es válida. Inténtelo de nuevo."
				Escribir ""
			FinSi
		Hasta Que hora_inicio_valida
		
		// Verificar que la hora de término de la reservación sea válida.
		Repetir
			hora_termino_valida = Falso
			
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
			
			Si (primer_elemento_hora_termino_int >= 0 Y primer_elemento_hora_termino_int <= 23) Y (segundo_elemento_hora_termino_int >= 0 Y segundo_elemento_hora_termino_int <= 59) Entonces
				hora_termino_valida = Verdadero
			SiNo
				Escribir "La hora de término ingresada no es válida. Inténtelo de nuevo."
				Escribir ""
			FinSi
		Hasta Que hora_termino_valida
		
		condiciones_horario = Falso
		horario_valido = Falso
		diferencia_horas = primer_elemento_hora_inicio_int - (primer_elemento_hora_actual_int + (segundo_elemento_hora_actual_int / 60))
		Escribir "Diferencia de Horas: ", diferencia_horas, "."
		
		Si ((primer_elemento_hora_inicio_int >= 8 Y primer_elemento_hora_inicio_int <= 20) Y (segundo_elemento_hora_inicio_int = 0)) Y ((primer_elemento_hora_termino_int >= 8 Y primer_elemento_hora_termino_int <= 20) Y (segundo_elemento_hora_termino_int = 0)) Y (diferencia_horas >= 1) Entonces
			condiciones_horario = Verdadero
			Si primer_elemento_hora_inicio_int < primer_elemento_hora_termino_int Entonces
				horario_valido = Verdadero
			SiNo
				Escribir "El horario ingresado no es válido. Inténtelo de nuevo."
				Escribir ""
			FinSi
		SiNo
			Escribir "El horario ingresado no cumple con las condiciones establecidas. Inténtelo de nuevo."
			Escribir ""
		FinSi
	Hasta Que condiciones_horario Y horario_valido
FinAlgoritmo
