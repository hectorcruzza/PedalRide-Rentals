Algoritmo VerInformacionPersonal
	Dimension informacion_usuario(1,6)
	informacion_usuario(1, 1) = "Jorge Julio"
	informacion_usuario(1, 2) = "Castro"
	informacion_usuario(1, 3) = "Alpuche"
	informacion_usuario(1, 4) = "9811265174"
	informacion_usuario(1, 5) = "jorge@gmail.com"
	informacion_usuario(1, 6) = "Jorge2004"
	
	nombre_usuario = informacion_usuario(1, 1)
	primer_apellido_usuario = informacion_usuario(1, 2)
	segundo_apellido_usuario = informacion_usuario(1, 3)
	numero_telefono_usuario = informacion_usuario(1, 4)
	correo_electronico_usuario = informacion_usuario(1, 5)
	contrase�a_usuario = informacion_usuario(1, 6)
	
	Escribir "Secci�n: Mi perfil."
	Escribir "- Informaci�n personal:"
	Escribir " - Nombre(s): ", nombre_usuario
	Escribir " - Primer apellido: ", primer_apellido_usuario
	Escribir " - Segundo apellido: ", segundo_apellido_usuario
	Escribir " - N�mero de tel�fono: ", numero_telefono_usuario
	Escribir " - Correo electr�nico: ", correo_electronico_usuario
	Escribir " - Contrase�a: ", contrase�a_usuario
	
	
FinAlgoritmo
