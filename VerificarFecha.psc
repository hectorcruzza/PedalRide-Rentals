Algoritmo VerificarFecha
	Definir fecha_actual, fecha_reserva Como Cadena
	Definir año_actual, mes_actual, dia_actual, dias_febrero, año_reserva, mes_reserva, dia_reserva Como Entero
	Definir año_valido, mes_valido, dia_valido Como Logico
	 
	fecha_actual = ConvertirATexto(FechaActual())
	dia_actual = ConvertirANumero(SubCadena(fecha_actual, 7, 8))
	mes_actual = ConvertirANumero(SubCadena(fecha_actual, 5, 6))
	año_actual = ConvertirANumero(SubCadena(fecha_actual, 1, 4))
	Escribir "Fecha Actual: ", dia_actual, "/", mes_actual, "/", año_actual, "."
	
	Dimension dias_meses(12)
	Escribir Sin Saltar "Meses-Días: | "
	Para i = 1 Hasta 12 Con Paso 1 Hacer
		Si i = 2 Entonces
			Si (año_actual MOD 4 = 0 Y año_actual MOD 100 <> 0) O (año_actual MOD 400 = 0)
				dias_meses(i) = 29
			SiNo
				dias_meses(i) = 28
			FinSi
		SiNo
			Si (i MOD 2 <> 0 Y i <= 7) O (i MOD 2 = 0 Y i >= 8) Entonces
				dias_meses(i) = 31
			SiNo
				dias_meses(i) = 30
			FinSi
		FinSi
		Escribir Sin Saltar i, "-", dias_meses(i), " | "
	FinPara
	Escribir ""
	
	Escribir ""
	
	Escribir "Sección: Hacer una reservación."
	Escribir "- Es importante mencionar que las reservaciones se deben realizar para el año y mes en curso."
	Repetir
		año_valido = Falso
		mes_valido = Falso
		dia_valido = Falso
		Escribir Sin Saltar "- Ingrese la fecha de la reservación (Formato: DD/MM/AAAA): "
		Leer fecha_reserva
		
		dia_reserva = ConvertirANumero(SubCadena(fecha_reserva, 1, 2))
		mes_reserva = ConvertirANumero(SubCadena(fecha_reserva, 4, 5))
		año_reserva = ConvertirANumero(SubCadena(fecha_reserva, 7, 10))
		Escribir "Fecha de Reservación: ", dia_reserva, "/", mes_reserva, "/", año_reserva, "."
		
		Si año_reserva = año_actual Entonces
			año_valido = Verdadero
			Si mes_reserva = mes_actual Entonces
				mes_valido = Verdadero
				Si dia_reserva >= 1 Y dia_reserva <= dias_meses(mes_reserva) Y dia_reserva >= dia_actual Entonces
					dia_valido = Verdadero
				FinSi
			FinSi
		FinSi
		
		Si NO año_valido O NO mes_valido O NO dia_valido Entonces
			Escribir "La fecha ingresada no es válida. Inténtelo de nuevo."
			Escribir ""
		FinSi
	Hasta Que año_valido Y mes_valido Y dia_valido
FinAlgoritmo
