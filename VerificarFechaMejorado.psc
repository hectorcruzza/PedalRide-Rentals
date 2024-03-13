Algoritmo VerificarFechaMejorado
	Definir fecha_actual, fecha_reserva Como Cadena
	Definir dia_actual, mes_actual, a�o_actual, dia_reserva, mes_reserva, a�o_reserva Como Entero
	Definir fecha_valida, condiciones_fecha_valida Como Logico
	fecha_actual = ConvertirATexto(FechaActual())
	dia_actual = ConvertirANumero(SubCadena(fecha_actual, 7, 8))
	mes_actual = ConvertirANumero(SubCadena(fecha_actual, 5, 6))
	a�o_actual = ConvertirANumero(SubCadena(fecha_actual, 1, 4))
	fecha_reserva = ""
	dia_reserva = 0
	mes_reserva = 0
	a�o_reserva = 0
	
	Escribir "Fecha Actual: ", dia_actual, "/", mes_actual, "/", a�o_actual, "."
	
	Dimension dias_meses(12)
	Escribir Sin Saltar "Meses-D�as: | "
	Para i = 1 Hasta 12 Con Paso 1 Hacer
		Si i = 2 Entonces
			Si (a�o_actual MOD 4 = 0 Y a�o_actual MOD 100 <> 0) O (a�o_actual MOD 400 = 0)
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
	
	Escribir "Secci�n: Hacer una reservaci�n."
	Repetir
		fecha_valida = Falso
		condiciones_fecha_valida = Falso
		
		Escribir "- Es importante mencionar que las reservaciones se deben realizar para el a�o y mes en curso."
		Escribir Sin Saltar "- Ingrese la fecha de la reservaci�n (Formato: DD/MM/AAAA): "
		Leer fecha_reserva
		
		dia_reserva = ConvertirANumero(SubCadena(fecha_reserva, 1, 2))
		mes_reserva = ConvertirANumero(SubCadena(fecha_reserva, 4, 5))
		a�o_reserva = ConvertirANumero(SubCadena(fecha_reserva, 7, 10))
		Escribir "Fecha de Reserva: ", dia_reserva, "/", mes_reserva, "/", a�o_reserva, "."
		
		Si a�o_reserva >= 0 Entonces
			Si mes_reserva >= 1 Y mes_reserva <= 12 Entonces
				Si dia_reserva >= 1 Y dia_reserva <= dias_meses(mes_reserva) Entonces
					fecha_valida = Verdadero
					Si a�o_reserva = a�o_actual Y mes_reserva = mes_actual Y dia_reserva >= dia_actual Entonces
						condiciones_fecha_valida = Verdadero
					FinSi
				FinSi
			FinSi
		FinSi
		
		Si NO fecha_valida Entonces
			Escribir "La fecha ingresada no es v�lida. Int�ntelo de nuevo."
			Escribir ""
		SiNo
			Si NO condiciones_fecha_valida Entonces
				Escribir "La fecha de reserva ingresada no cumple con los par�metros establecidos. Int�ntelo de nuevo."
				Escribir ""
			FinSi
		FinSi
		
	Hasta Que fecha_valida Y condiciones_fecha_valida
FinAlgoritmo