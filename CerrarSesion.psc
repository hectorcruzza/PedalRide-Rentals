Algoritmo CerrarSesion
	Definir nombre_usuario, primer_apellido_usuario, segundo_apellido_usuario, numero_telefono_usuario, correo_electronico_usuario, contraseña_usuario, opcion_usuario Como Cadena
	Dimension informacion_usuario(1, 6)
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
	contraseña_usuario = informacion_usuario(1, 6)
	
	opcion_usuario = ""
	
	Escribir "1-. Cerrar Sesión."
	Leer opcion_usuario
	
	Si opcion_usuario = "1" Entonces
		nombre_usuario = ""
		primer_apellido_usuario = ""
		segundo_apellido_usuario = ""
		numero_telefono_usuario = ""
		correo_electronico_usuario = ""
		contraseña_usuario = ""
	FinSi
FinAlgoritmo
