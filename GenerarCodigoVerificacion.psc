Algoritmo GenerarCodigoVerificacion
	Definir codigo_verificacion, codigo_verificacion_usuario Como Cadena
	Definir codigo_verificacion_correcto Como Logico
	
	codigo_verificacion = ""
	codigo_verificacion_usuario = ""
	codigo_verificacion_correcto = Falso
	
	Para i = 1 Hasta 6 Con Paso 1 Hacer
		codigo_verificacion = codigo_verificacion + ConvertirATexto(azar(10))
	FinPara
	
	Escribir "| C�digo de Verificaci�n: ", codigo_verificacion, " |"
	Escribir ""
	
	Escribir "Para terminar de crear su cuenta, deber� ingresar un c�digo de 6 d�gitos con el fin de verificarla. Este c�digo se ha enviado a la direcci�n de correo electr�nico ingresada."
	Escribir ""
	
	Repetir
		codigo_verificacion_correcto = Verdadero
		
		Escribir Sin Saltar "- Ingrese el c�digo para verificar su cuenta: "
		Leer codigo_verificacion_usuario
		
		Si codigo_verificacion_usuario <> codigo_verificacion Entonces
			codigo_verificacion_correcto = Falso
			Escribir "El c�digo de verificaci�n ingresado no es v�lido. Int�ntelo de nuevo."
			Escribir ""
		FinSi
	Hasta Que codigo_verificacion_correcto
	Escribir ""
	Escribir "Su cuenta ha sido creada exitosamente."
FinAlgoritmo
