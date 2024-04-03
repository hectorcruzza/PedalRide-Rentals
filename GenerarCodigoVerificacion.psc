Algoritmo GenerarCodigoVerificacion
	Definir codigo_verificacion, codigo_verificacion_usuario Como Cadena
	Definir codigo_verificacion_correcto Como Logico
	
	codigo_verificacion = ""
	codigo_verificacion_usuario = ""
	codigo_verificacion_correcto = Falso
	
	Para i = 1 Hasta 6 Con Paso 1 Hacer
		codigo_verificacion = codigo_verificacion + ConvertirATexto(azar(10))
	FinPara
	
	Escribir "| Código de Verificación: ", codigo_verificacion, " |"
	Escribir ""
	
	Escribir "Para terminar de crear su cuenta, deberá ingresar un código de 6 dígitos con el fin de verificarla. Este código se ha enviado a la dirección de correo electrónico ingresada."
	Escribir ""
	
	Repetir
		codigo_verificacion_correcto = Verdadero
		
		Escribir Sin Saltar "- Ingrese el código para verificar su cuenta: "
		Leer codigo_verificacion_usuario
		
		Si codigo_verificacion_usuario <> codigo_verificacion Entonces
			codigo_verificacion_correcto = Falso
			Escribir "El código de verificación ingresado no es válido. Inténtelo de nuevo."
			Escribir ""
		FinSi
	Hasta Que codigo_verificacion_correcto
	Escribir ""
	Escribir "Su cuenta ha sido creada exitosamente."
FinAlgoritmo
