Algoritmo PedalRide_Rentals_Algoritmos_Parte_2
	// Variables usadas para almacenar la fecha de la reservaci�n, y verfificar que dicha fecha sea correcta y cumpla con las condiciones establecidas.
	Definir fecha_actual, fecha_reserva Como Cadena 
	Definir dia_actual, mes_actual, a�o_actual, dia_reserva, mes_reserva, a�o_reserva Como Entero
	Definir fecha_valida, condiciones_fecha_valida, condicion_dia_valido Como Logico
	// Variables usadas para almacenar la hora de inicio y de t�rmino de la reservaci�n, y verificar que el horario ingresado sea correcto y cumpla con las condiciones establecidas.
	Definir hora_actual, hora_inicio_reserva, hora_termino_reserva, primer_elemento_hora_inicio_str, segundo_elemento_hora_inicio_str, primer_elemento_hora_termino_str, segundo_elemento_hora_termino_str Como Cadena
	Definir primer_elemento_hora_actual_int, segundo_elemento_hora_actual_int, i, h, l, primer_elemento_hora_inicio_int, segundo_elemento_hora_inicio_int, primer_elemento_hora_termino_int, segundo_elemento_hora_termino_int Como Entero
	Definir diferencia_horas Como Real
	Definir condicion, hora_inicio_valida, hora_termino_valida, condiciones_horario, horario_valido Como Logico
	// Variables usadas para establecer la cantidad de bicicletas a rentar, almacenar el correo del usuario, contabilizar cu�ntas reservaciones se han hecho, guardar la bicicleta elegida por el usuario, calcular el costo de la reservaci�n y guardar la respuesta del usuario en cuanto al costo.
	Definir cantidad_bicicletas, numero_reservaciones, numero_reservacion, costo_por_hora Como Entero
	Definir correo_usuario, numero_bicicleta, costo_total_reservacion, respuesta_usuario_costo Como Cadena
	Definir bicicletas_disponibles, bicicleta_disponible Como Logico
	
	// Inicializaci�n de las variables empleadas para la fecha de la reservaci�n.
	fecha_actual = ConvertirATexto(FechaActual()) // Obtener la fecha actual.
	dia_actual = ConvertirANumero(SubCadena(fecha_actual, 7, 8))
	mes_actual = ConvertirANumero(SubCadena(fecha_actual, 5, 6))
	a�o_actual = ConvertirANumero(SubCadena(fecha_actual, 1, 4))
	fecha_reserva = ""
	dia_reserva = 0
	mes_reserva = 0
	a�o_reserva = 0
	
	Escribir "Fecha Actual: ", dia_actual, "/", mes_actual, "/", a�o_actual, "." // Mostrar la fecha actual.
	
	Dimension dias_meses(12) // Array para almacenar cu�ntos d�as tiene cada mes.
	Escribir Sin Saltar "Meses-D�as: | "
	Para i = 1 Hasta 12 Con Paso 1 Hacer
		Si i = 2 Entonces
			// Verificar si el a�o es bisiesto o no.
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
		Escribir Sin Saltar i, "-", dias_meses(i), " | " // Mostrar los meses y cu�ntos d�as tiene cada uno.
	FinPara
	Escribir ""
	
	// Inicializaci�n de las variables empleadas para el horario de la reservaci�n.
	// hora_actual = ConvertirATexto(HoraActual())
	hora_actual = "102500"
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
	
	// Inicializaci�n de las variables empleadas para llevar a cabo las reservaciones.
	cantidad_bicicletas = 5
	numero_reservaciones = 10
	correo_usuario = ""
	numero_bicicleta = ""
	costo_por_hora = 80
	respuesta_usuario_costo = ""
	
	Dimension bicicletas(cantidad_bicicletas)
	bicicletas(1) = "010"
	bicicletas(2) = "020"
	bicicletas(3) = "030"
	bicicletas(4) = "040"
	bicicletas(5) = "067"
	
	Dimension reservaciones(numero_reservaciones, 6)
	
	Escribir "Hora de Actual: ", primer_elemento_hora_actual_int, ":", segundo_elemento_hora_actual_int "." 
	
	Escribir ""
	
	Escribir "Secci�n: Hacer una reservaci�n."
	Escribir "- Nuestro horario de trabajo es de las 08:00 a las 20:00."
	Escribir "- Las reservaciones se deben realizar para el a�o y mes en curso."
	Escribir "- Las reservaciones se realizan en bloques por hora."
	Escribir "- Las reservaciones pueden ser de m�s de una hora."
	Escribir "- Las reservaciones se deben realizar con al menos una hora de anticipaci�n."
	Escribir ""
	
	numero_reservacion = 0
	
	// Bloque que se ejecuta hasta que ya no se puedan hacer m�s reservaciones o hasta que el sistema est� cerrado por el horario.
	Mientras numero_reservacion < numero_reservaciones Hacer
		Escribir "N�mero de Reservaciones Hechas: ", numero_reservacion, "."
		// Pedir al usuario que ingrese su correo electr�nico.
		Escribir Sin Saltar "- Ingrese su correo electr�nico: "
		Leer correo_usuario
		
		// Bloque que se ejecuta hasta que la fecha de la reservaci�n sea v�lida y cumpla con las condiciones establecidas.
		Repetir
			fecha_valida = Falso
			condiciones_fecha_valida = Falso
			condicion_dia_valido = Falso
			Escribir Sin Saltar "- Ingrese la fecha de la reservaci�n (Formato: DD/MM/AAAA): "
			Leer fecha_reserva // Obtener la fecha de la reserva.
			
			dia_reserva = ConvertirANumero(SubCadena(fecha_reserva, 1, 2))
			mes_reserva = ConvertirANumero(SubCadena(fecha_reserva, 4, 5))
			a�o_reserva = ConvertirANumero(SubCadena(fecha_reserva, 7, 10))
			Escribir "Fecha de Reservaci�n: ", dia_reserva, "/", mes_reserva, "/", a�o_reserva, "." // Mostrar la fecha de la reserva.
			
			// Verificar que la fecha sea v�lida.
			Si a�o_reserva >= 0 Entonces
				Si mes_reserva >= 1 Y mes_reserva <= 12 Entonces
					Si dia_reserva >= 1 Y dia_reserva <= dias_meses(mes_reserva) Entonces
						fecha_valida = Verdadero
						Si a�o_reserva = a�o_actual Y mes_reserva = mes_actual Entonces
							condiciones_fecha_valida = Verdadero
							Si dia_reserva >= dia_actual Entonces
								condicion_dia_valido = Verdadero
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
			
			Si NO fecha_valida O NO condiciones_fecha_valida O NO condicion_dia_valido Entonces
				// Si no la fecha no es v�lida, se muestra un mensaje al usuario.
				Si NO fecha_valida Entonces
					Escribir "La fecha ingresada no es v�lida. Int�ntelo de nuevo."
					Escribir ""
				SiNo
					// Si la fecha no cumple con las condiciones establecidas para hacer una reservaci�n, se muestra un mensaje al usuario.
					Si NO condiciones_fecha_valida Entonces
						Escribir "La fecha de la reservaci�n ingresada no cumple con los par�metros establecidos. Int�ntelo de nuevo."
						Escribir ""
					SiNo
						// Si el d�a de la fecha de la reservaci�n no es v�lido, se muestra un mensaje al usuario.
						Escribir "El d�a de la fecha de la reservaci�n ingresado no es v�lido. Int�ntelo de nuevo."
						Escribir ""
					FinSi
				FinSi
				Escribir "- Recuerde que las reservaciones se deben realizar para el a�o y mes en curso."
				Escribir ""
			FinSi
			
		Hasta Que fecha_valida Y condiciones_fecha_valida Y condicion_dia_valido
		
		// Verificar que el horario ingresado cumpla con las condiciones establecidas.
		Repetir
			// Verificar que la hora de inicio de la reservaci�n sea v�lida.
			Repetir
				hora_inicio_valida = Falso
				
				Escribir Sin Saltar "- Ingrese la hora de inicio de la reservaci�n (Formato de 24 horas: 13:00): "
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
					Escribir "La hora de inicio ingresada no es v�lida. Int�ntelo de nuevo."
					Escribir ""
					Escribir "Recuerde que: "
					Escribir "- Nuestro horario de trabajo es de las 08:00 a las 20:00."
					Escribir "- Las reservaciones se realizan en bloques por hora."
					Escribir "- Las reservaciones pueden ser de m�s de una hora."
					Escribir "- Las reservaciones se deben realizar con al menos una hora de anticipaci�n."
					Escribir ""
				FinSi
			Hasta Que hora_inicio_valida
			
			// Verificar que la hora de t�rmino de la reservaci�n sea v�lida.
			Repetir
				hora_termino_valida = Falso
				
				Escribir Sin Saltar "- Ingrese la hora de t�rmino de la reservaci�n (Formato de 24 horas: 20:00): "
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
				
				Escribir "Hora de T�rmino (String): ", hora_termino_reserva, "." 
				
				primer_elemento_hora_termino_int = ConvertirANumero(primer_elemento_hora_termino_str)
				segundo_elemento_hora_termino_int = ConvertirANumero(segundo_elemento_hora_termino_str)
				
				Escribir "Hora de T�rmino (Entero): ", primer_elemento_hora_termino_int, ":", segundo_elemento_hora_termino_int, "."
				
				Si (primer_elemento_hora_termino_int >= 0 Y primer_elemento_hora_termino_int <= 23) Y (segundo_elemento_hora_termino_int >= 0 Y segundo_elemento_hora_termino_int <= 59) Entonces
					hora_termino_valida = Verdadero
				SiNo
					Escribir "La hora de t�rmino ingresada no es v�lida. Int�ntelo de nuevo."
					Escribir ""
					Escribir "Recuerde que: "
					Escribir ""
					Escribir "- Nuestro horario de trabajo es de las 08:00 a las 20:00."
					Escribir "- Las reservaciones se realizan en bloques por hora."
					Escribir "- Las reservaciones pueden ser de m�s de una hora."
					Escribir "- Las reservaciones se deben realizar con al menos una hora de anticipaci�n."
					Escribir ""
				FinSi
			Hasta Que hora_termino_valida
			
			condiciones_horario = Falso
			horario_valido = Falso
			diferencia_horas = primer_elemento_hora_inicio_int - (primer_elemento_hora_actual_int + (segundo_elemento_hora_actual_int / 60))
			Escribir "Diferencia de Horas: ", diferencia_horas, "."
			
			Si ((primer_elemento_hora_inicio_int >= 8 Y primer_elemento_hora_inicio_int <= 20) Y (segundo_elemento_hora_inicio_int = 0)) Y ((primer_elemento_hora_termino_int >= 8 Y primer_elemento_hora_termino_int <= 20) Y (segundo_elemento_hora_termino_int = 0)) Y (dia_reserva > dia_actual O diferencia_horas >= 1) Entonces
				condiciones_horario = Verdadero
				Si primer_elemento_hora_inicio_int < primer_elemento_hora_termino_int Entonces
					horario_valido = Verdadero
				FinSi
			FinSi
			
			Si NO condiciones_horario O NO horario_valido Entonces
				Si NO condiciones_horario Entonces
					Escribir "El horario ingresado no cumple con las condiciones establecidas. Int�ntelo de nuevo."
					Escribir ""
				SiNo
					Escribir "El horario ingresado no es v�lido. Int�ntelo de nuevo."
					Escribir ""
				FinSi
				Escribir "Recuerde que: "
				Escribir "- Nuestro horario de trabajo es de las 08:00 a las 20:00."
				Escribir "- Las reservaciones se realizan en bloques por hora."
				Escribir "- Las reservaciones pueden ser de m�s de una hora."
				Escribir "- Las reservaciones se deben realizar con al menos una hora de anticipaci�n."
				Escribir ""
			FinSi
		Hasta Que condiciones_horario Y horario_valido
		
		bicicletas_disponibles = Falso
		h = 1
		l = 1
		
		// Ciclo para verificar si hay bicicletas disponibles para la fecha y horario elegidos.
		Mientras h <= cantidad_bicicletas Y NO bicicletas_disponibles Hacer
			bicicletas_disponibles = Verdadero
			l = 1
			Mientras l <= numero_reservacion Y bicicletas_disponibles Hacer // Para cada reservaci�n en la lista de reservaciones.
				// Por cada bicicleta en la lista de bicicletas se revisa si est� reservada por alguien.
				Si bicicletas(h) = reservaciones(l, 5) Entonces
					container_dia_reserva = ConvertirANumero(SubCadena(reservaciones(l, 2), 1, 2))
					container_mes_reserva = ConvertirANumero(SubCadena(reservaciones(l, 2), 4, 5))
					Si NO (mes_reserva > container_mes_reserva) Entonces
						Si NO ((dia_reserva > container_dia_reserva) O (dia_reserva < container_dia_reserva)) Entonces
							container_primer_elemento_hora_inicio_reserva = ConvertirANumero(SubCadena(reservaciones(l, 3), 1, 2))
							container_primer_elemento_hora_termino_reserva = ConvertirANumero(SubCadena(reservaciones(l, 4), 1, 2))
							Si NO ((primer_elemento_hora_inicio_int >= container_primer_elemento_hora_termino_reserva) O (primer_elemento_hora_termino_int <= container_primer_elemento_hora_inicio_reserva)) Entonces
								bicicletas_disponibles = Falso
							FinSi
						FinSi
					FinSi
				FinSi
				l = l + 1
			FinMientras
			h = h + 1
		FinMientras
		
		Si bicicletas_disponibles Entonces
			Escribir "- A continuaci�n, se muestra la lista de bicicletas disponibles en la fecha elegida:"
			Escribir ""
			Escribir "| N�mero de Bicicleta |"
			
			l = 1
			
			// Ciclo para mostrar las bicicletas disponibles.
			Para h = 1 Hasta cantidad_bicicletas Con Paso 1 Hacer // Para cada bicicleta en la lista de bicicletas.
				bicicleta_disponible = Verdadero
				l = 1
				Mientras l <= numero_reservacion Y bicicleta_disponible Hacer // Para cada reservaci�n en la lista de reservaciones.
					// Por cada bicicleta en la lista de bicicletas se revisa si est� reservada por alguien.
					Si bicicletas(h) = reservaciones(l, 5) Entonces
						container_dia_reserva = ConvertirANumero(SubCadena(reservaciones(l, 2), 1, 2))
						container_mes_reserva = ConvertirANumero(SubCadena(reservaciones(l, 2), 4, 5))
						Si NO (mes_reserva > container_mes_reserva) Entonces
							Si NO ((dia_reserva > container_dia_reserva) O (dia_reserva < container_dia_reserva)) Entonces
								container_primer_elemento_hora_inicio_reserva = ConvertirANumero(SubCadena(reservaciones(l, 3), 1, 2))
								container_primer_elemento_hora_termino_reserva = ConvertirANumero(SubCadena(reservaciones(l, 4), 1, 2))
								Si NO ((primer_elemento_hora_inicio_int >= container_primer_elemento_hora_termino_reserva) O (primer_elemento_hora_termino_int <= container_primer_elemento_hora_inicio_reserva)) Entonces
									bicicleta_disponible = Falso
								FinSi
							FinSi
						FinSi
					FinSi
					l = l + 1
				FinMientras
				Si bicicleta_disponible Entonces
					Escribir "          ", bicicletas(h)
				FinSi
			FinPara
			Escribir ""
			
			Escribir Sin Saltar "- Elija la bicicleta a usar: "
			Leer numero_bicicleta
			
			costo_total_reservacion = "$" + ConvertirATexto((primer_elemento_hora_termino_int - primer_elemento_hora_inicio_int) * costo_por_hora)
			
			Repetir 
				Escribir Sin Saltar "El costo de la reservaci�n es de ", costo_total_reservacion, ". �Est� de acuerdo? "
				Leer respuesta_usuario_costo
				Si respuesta_usuario_costo <> "No" Y respuesta_usuario_costo <> "S�" Y respuesta_usuario_costo <> "Si" Entonces
					Escribir "La respuesta ingresada no es v�lida. Int�ntelo de nuevo."
				FinSi
			Hasta Que respuesta_usuario_costo = "No" O respuesta_usuario_costo = "S�" O respuesta_usuario_costo = "Si"
			
			Si respuesta_usuario_costo <> "No" Entonces
				numero_reservacion = numero_reservacion + 1
				// Se guardan los detalles de la reservaci�n en la lista general de reservaciones.
				reservaciones(numero_reservacion, 1) = correo_usuario
				reservaciones(numero_reservacion, 2) = fecha_reserva
				reservaciones(numero_reservacion, 3) = hora_inicio_reserva
				reservaciones(numero_reservacion, 4) = hora_termino_reserva
				reservaciones(numero_reservacion, 5) = numero_bicicleta
				reservaciones(numero_reservacion, 6) = costo_total_reservacion
				
				Escribir "- Su reservaci�n se ha realizado con �xito."
			 	Escribir "- En este momento, se muestran los detalles de la(s) reservacion(es) que ha realizado en su cuenta: "
				Escribir ""
				
				// Ciclo para mostrar las reservaciones del usuario en curso.
				Para a = 1 Hasta numero_reservacion Con Paso 1 Hacer
					Si reservaciones(a, 1) = correo_usuario Entonces
						Escribir "| Correo Electr�nico del Usuario | Fecha de la Reservaci�n | Hora de Inicio | Hora de T�rmino | N.� de Bicicleta | Costo |"
						Escribir "        ", reservaciones(a, 1), "                 ", reservaciones(a, 2), "              ", reservaciones(a, 3), "             ", reservaciones(a, 4), "              ", reservaciones(a, 5), "          ", reservaciones(a, 6)
					FinSi
				FinPara			
			FinSi
		SiNo
			Escribir "No hay bicicletas disponibles para la fecha y horario elegidos."
			Escribir "Intente cambiar la fecha y horario de la reservaci�n."
		FinSi
		
		Si numero_reservacion > 0 Entonces
			Escribir ""
			Escribir "Reservaciones Hechas: "
			Escribir ""
			Para b = 1 Hasta numero_reservacion Con Paso 1 Hacer
				Escribir "| Correo Electr�nico del Usuario | Fecha de la Reservaci�n | Hora de Inicio | Hora de T�rmino | N.� de Bicicleta | Costo |"
				Escribir "        ", reservaciones(b, 1), "                 ", reservaciones(b, 2), "              ", reservaciones(b, 3), "             ", reservaciones(b, 4), "              ", reservaciones(b, 5), "          ", reservaciones(b, 6)
			FinPara
			Escribir ""	
		FinSi
		// Ciclo para mostrar todas las reservaciones realizadas por todos los usuarios.
	FinMientras
FinAlgoritmo
