Algoritmo MostrarReservaciones_CancelarReservacion
	Definir fecha_actual, hora_actual, correo_electronico, numero_reservacion Como Cadena
	Definir reservaciones_confirmadas, numero_reservacion_encontrado, cancelacion Como Logico
	Definir dia_actual, mes_actual, año_actual, horas_actual, minutos_actual, cantidad_reservaciones, i, cantidad_reservaciones_confirmadas, h, l, dias_anticipacion, a Como Entero
	Definir horas_anticipacion Como Real
	
	fecha_actual = ConvertirATexto(FechaActual())
	dia_actual = ConvertirANumero(Subcadena(fecha_actual, 7, 8))
	mes_actual = ConvertirANumero(Subcadena(fecha_actual, 5, 6))
	año_actual = ConvertirANumero(Subcadena(fecha_actual, 1, 4))
	fecha_actual = Subcadena(fecha_actual, 7, 8) + "/" + Subcadena(fecha_actual, 5, 6) + "/" + Subcadena(fecha_actual, 1, 4)
	
	hora_actual = ConvertirATexto(HoraActual())
	horas_actual = ConvertirANumero(Subcadena(hora_actual, 1, 1))
	minutos_actual = ConvertirANumero(Subcadena(hora_actual, 2, Longitud(hora_actual) - 2))
	
	Si Longitud(hora_actual) <> 5 Entonces
		horas_actual = ConvertirANumero(Subcadena(hora_actual, 1, 2))
		minutos_actual = ConvertirANumero(Subcadena(hora_actual, 3, Longitud(hora_actual) - 2))
		hora_actual = Subcadena(hora_actual, 1, 2) + ":" + Subcadena(hora_actual, 3, Longitud(hora_actual) - 2)
	SiNo
		hora_actual = Subcadena(hora_actual, 1, 1) + ":" + Subcadena(hora_actual, 2, Longitud(hora_actual) - 2)
	FinSi
	
	Escribir "| Fecha: ", fecha_actual, " | ", "Hora: ", hora_actual, " |"
	
	cantidad_reservaciones = 6
	
	Dimension reservaciones(cantidad_reservaciones, 6)
	reservaciones(1, 1) = "01"
	reservaciones(1, 2) = "20/03/2024"
	reservaciones(1, 3) = "10:00 - 11:00"
	reservaciones(1, 4) = "067"
	reservaciones(1, 5) = "$60"
	reservaciones(1, 6) = "jorge@gmail.com"
	
	reservaciones(2, 1) = "02"
	reservaciones(2, 2) = "21/03/2024"
	reservaciones(2, 3) = "07:00 - 09:00"
	reservaciones(2, 4) = "054"
	reservaciones(2, 5) = "$120"
	reservaciones(2, 6) = "jorge@gmail.com"
	
	reservaciones(3, 1) = "03"
	reservaciones(3, 2) = "21/03/2024"
	reservaciones(3, 3) = "10:00 - 12:00"
	reservaciones(3, 4) = "103"
	reservaciones(3, 5) = "$180"
	reservaciones(3, 6) = "jorge@gmail.com"
	
	reservaciones(4, 1) = "04"
	reservaciones(4, 2) = "22/03/2024"
	reservaciones(4, 3) = "15:00 - 16:00"
	reservaciones(4, 4) = "015"
	reservaciones(4, 5) = "$60"
	reservaciones(4, 6) = "jorge@gmail.com"
	
	reservaciones(5, 1) = "05"
	reservaciones(5, 2) = "24/03/2024"
	reservaciones(5, 3) = "19:00 - 20:00"
	reservaciones(5, 4) = "097"
	reservaciones(5, 5) = "$60"
	reservaciones(5, 6) = "hector@gmail.com"
	
	reservaciones(6, 1) = "06"
	reservaciones(6, 2) = "31/03/2024"
	reservaciones(6, 3) = "12:00 - 17:00"
	reservaciones(6, 4) = "023"
	reservaciones(6, 5) = "$300"
	reservaciones(6, 6) = "hector@gmail.com"
	
	correo_electronico = ""

	Escribir ""
	
	Escribir Sin Saltar "Ingrese su correo electrónico: "
	Leer correo_electronico
	
	Escribir ""
	Escribir "Sección: Mis reservaciones."
	Escribir "- Reservaciones confirmadas:"
	Escribir ""
	
	reservaciones_confirmadas = Falso
	i = 1
	
	Mientras NO reservaciones_confirmadas Y i <= cantidad_reservaciones Hacer
		Si correo_electronico = reservaciones(i, 6) Entonces
			
			container_dia_reserva = ConvertirANumero(Subcadena(reservaciones(i, 2), 1, 2))
			container_mes_reserva = ConvertirANumero(Subcadena(reservaciones(i, 2), 4, 5))
			container_año_reserva = ConvertirANumero(Subcadena(reservaciones(i, 2), 7, 10))
			
			container_horas_inicio_reserva = ConvertirANumero(Subcadena(reservaciones(i, 3), 1, 2))
			
			Si (año_actual < container_año_reserva) O (año_actual = container_año_reserva Y (mes_actual < container_mes_reserva O mes_actual = container_mes_reserva Y (dia_actual < container_dia_reserva O (dia_actual = container_dia_reserva Y horas_actual < container_horas_inicio_reserva)))) Entonces
				reservaciones_confirmadas = Verdadero
			FinSi
		FinSi
		i = i + 1
	FinMientras
	
	Si reservaciones_confirmadas Entonces
		
		Dimension numeros_reservaciones_confirmadas(cantidad_reservaciones)
		cantidad_reservaciones_confirmadas = 0
		
		Escribir "| N.° de Reservación |   Fecha   |    Horario    | N.° de Bicicleta | Costo |"
		Para j = 1 Hasta cantidad_reservaciones Con Paso 1 Hacer
			Si correo_electronico = reservaciones(j, 6) Entonces
				
				container_dia_reserva = ConvertirANumero(Subcadena(reservaciones(j, 2), 1, 2))
				container_mes_reserva = ConvertirANumero(Subcadena(reservaciones(j, 2), 4, 5))
				container_año_reserva = ConvertirANumero(Subcadena(reservaciones(j, 2), 7, 10))
				
				container_horas_inicio_reserva = ConvertirANumero(Subcadena(reservaciones(j, 3), 1, 2))
				
				Si (año_actual < container_año_reserva) O (año_actual = container_año_reserva Y (mes_actual < container_mes_reserva O mes_actual = container_mes_reserva Y (dia_actual < container_dia_reserva O (dia_actual = container_dia_reserva Y horas_actual < container_horas_inicio_reserva)))) Entonces
					cantidad_reservaciones_confirmadas = cantidad_reservaciones_confirmadas + 1
					numeros_reservaciones_confirmadas(cantidad_reservaciones_confirmadas) = reservaciones(j, 1)
					Escribir  "          ", reservaciones(j, 1), "          ", reservaciones(j, 2), "   ", reservaciones(j, 3), "         ", reservaciones(j, 4), "           ", reservaciones(j, 5),"           "
				FinSi
			FinSi
		FinPara
		
		Escribir ""
		
		Repetir
			
			Escribir Sin Saltar "Ingrese el número de la reservación que desee cancelar: "
			Leer numero_reservacion
			
			numero_reservacion_encontrado = Falso
			h = 1
			
			Mientras h <= cantidad_reservaciones_confirmadas Y NO numero_reservacion_encontrado Hacer
				Si numero_reservacion = numeros_reservaciones_confirmadas(h) Entonces
					numero_reservacion_encontrado = Verdadero
				FinSi
				h = h + 1
			FinMientras
			
			Si numero_reservacion_encontrado Entonces
				
				cancelacion = Falso
				dias_anticipacion = 0
				horas_anticipacion = 0
				l = 1
				
				Mientras l <= cantidad_reservaciones Y NO cancelacion Hacer
					Si correo_electronico = reservaciones(l, 6) Entonces
						Si numero_reservacion = reservaciones(l, 1) Entonces
							container_dia_reserva = ConvertirANumero(Subcadena(reservaciones(l, 2), 1, 2))
							container_mes_reserva = ConvertirANumero(Subcadena(reservaciones(l, 2), 4, 5))
							container_año_reserva = ConvertirANumero(Subcadena(reservaciones(l, 2), 7, 10))
							
							container_horas_inicio_reserva = ConvertirANumero(Subcadena(reservaciones(l, 3), 1, 2))
							
							dias_anticipacion = container_dia_reserva - dia_actual 
							horas_anticipacion = container_horas_inicio_reserva - (horas_actual + (minutos_actual / 60))
							
							Si (año_actual < container_año_reserva) O (año_actual = container_año_reserva Y (mes_actual < container_mes_reserva O mes_actual = container_mes_reserva Y (dias_anticipacion > 1 O (dias_anticipacion = 1 Y horas_anticipacion >= 0)))) Entonces
								cancelacion = Verdadero
								reservaciones(l, 1) = ""
								reservaciones(l, 2) = ""
								reservaciones(l, 3) = ""
								reservaciones(l, 4) = ""
								reservaciones(l, 5) = ""
								reservaciones(l, 6) = ""
							FinSi
						FinSi
					FinSi
					l = l + 1
				FinMientras
				
				Si cancelacion Entonces
					Escribir "La reservación se ha cancelado correctamente."
					
					Escribir "- Reservaciones confirmadas:"
					Escribir ""
					
					reservaciones_confirmadas = Falso
					a = 1
					
					Mientras NO reservaciones_confirmadas Y a <= cantidad_reservaciones Hacer
						Si correo_electronico = reservaciones(a, 6) Entonces
							
							container_dia_reserva = ConvertirANumero(Subcadena(reservaciones(a, 2), 1, 2))
							container_mes_reserva = ConvertirANumero(Subcadena(reservaciones(a, 2), 4, 5))
							container_año_reserva = ConvertirANumero(Subcadena(reservaciones(a, 2), 7, 10))
							
							container_horas_inicio_reserva = ConvertirANumero(Subcadena(reservaciones(a, 3), 1, 2))
							
							Si (año_actual < container_año_reserva) O (año_actual = container_año_reserva Y (mes_actual < container_mes_reserva O mes_actual = container_mes_reserva Y (dia_actual < container_dia_reserva O (dia_actual = container_dia_reserva Y horas_actual < container_horas_inicio_reserva)))) Entonces
								reservaciones_confirmadas = Verdadero
							FinSi
						FinSi
						a = a + 1
					FinMientras
					
					Si reservaciones_confirmadas Entonces
						Escribir "| N.° de Reservación |   Fecha   |    Horario    | N.° de Bicicleta | Costo |"
						Para b = 1 Hasta cantidad_reservaciones Con Paso 1 Hacer
							Si correo_electronico = reservaciones(b, 6) Entonces
								
								container_dia_reserva = ConvertirANumero(Subcadena(reservaciones(b, 2), 1, 2))
								container_mes_reserva = ConvertirANumero(Subcadena(reservaciones(b, 2), 4, 5))
								container_año_reserva = ConvertirANumero(Subcadena(reservaciones(b, 2), 7, 10))
								
								container_horas_inicio_reserva = ConvertirANumero(Subcadena(reservaciones(b, 3), 1, 2))
								
								Si (año_actual < container_año_reserva) O (año_actual = container_año_reserva Y (mes_actual < container_mes_reserva O mes_actual = container_mes_reserva Y (dia_actual < container_dia_reserva O (dia_actual = container_dia_reserva Y horas_actual < container_horas_inicio_reserva)))) Entonces
									Escribir  "          ", reservaciones(b, 1), "          ", reservaciones(b, 2), "   ", reservaciones(b, 3), "         ", reservaciones(b, 4), "           ", reservaciones(b, 5),"           "
								FinSi
							FinSi
						FinPara
					SiNo
						Escribir "No tiene ninguna reservación confirmada."
					FinSi
				SiNo
					Escribir "No se pudo cancelar la reservación, ya que faltan menos de 24 horas para la misma."
				FinSi
			SiNo
				Escribir "No se ha encontrado una reservación con ese número. Inténtelo de nuevo."
				Escribir ""
			FinSi
		Hasta Que numero_reservacion_encontrado
	SiNo
		Escribir "No tiene ninguna reservación confirmada."
	FinSi
FinAlgoritmo