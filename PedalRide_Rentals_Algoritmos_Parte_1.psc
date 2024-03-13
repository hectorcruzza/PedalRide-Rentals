Funcion opciones_menu_acceso // Función que muestra las opciones del menú de acceso a fin de que el usuario elija una.
	Definir opcion_usuario Como Entero // Creación de una variable de tipo entero: opcion_usuario.
	// Inicialización de la variable:
	opcion_usuario = 0 // Variable que almacena la opción elegida por el usuario.
	Escribir "- Seleccione una de las siguientes opciones:" // Impresión de un mensaje.
	Escribir " 1-. Iniciar sesión." // Impresión de un mensaje.
	Escribir " 2-. Crear cuenta." // Impresión de un mensaje.
	Escribir " 3-. Salir del sistema." // Impresión de un mensaje.
	Leer opcion_usuario // Pedir al usuario que elija una opción.
	Segun opcion_usuario Hacer // Un switch case que evalua el input del usuario.
		1: // En caso de que haya ingresado el número 1:
			iniciar_sesion // Accederá a la sección para iniciar sesión.
		2: // En caso de que haya ingresado el número 2:
			crear_cuenta // Accederá a la sección para crear una cuenta.
	FinSegun // Fin del switch case.
FinFuncion // Fin de la función opciones_menu_acceso.


Funcion menu_acceso // Función que corresponde al menú de acceso.
	Escribir "Sección: Menú de acceso." // Impresión de un mensaje.
	opciones_menu_acceso // Se llama a la función correspondiente para mostrar al usuario las opciones a elegir en el menú de acceso.
FinFuncion // Fin de la función menu_acceso.


Funcion crear_cuenta // Función que permite al usuario crear una cuenta.
	// Creación de seis variables de tipo cadena: nombre_s_usuario, primer_apellido_usuario, segundo_apellido_usuario, numero_telefono_usuario, correo_electronico_usuario, contraseña_usuario.
	Definir nombre_s_usuario, primer_apellido_usuario, segundo_apellido_usuario, numero_telefono_usuario, correo_electronico_usuario, contraseña_usuario Como Cadena
	Definir contraseña_invalida Como Logico // Creación de una variable de tipo lógico: contraseña_invalida.
	// Inicialización de variables:
	nombre_s_usuario = "" // Variable que almacena el/los nombre(s) ingresado(s) por el usuario.
	primer_apellido_usuario = "" // Variable que almacena el primer apellido ingresado por el usuario.
	segundo_apellido_usuario = "" // Variable que almacena el segundo apellido ingresado por el usuario.
	numero_telefono_usuario = "" // Variable que almacena el número de teléfono ingresado por el usuario.
	correo_electronico_usuario = "" // Variable que almacena el correo electrónico ingresado por el usuario.
	contraseña_usuario = "" // Variable que almacena la contraseña ingresada por el usuario.
	contraseña_invalida = Verdadero // Valor lógico referente a si la contraseña ingresada no es válida.	
	Escribir "Sección: Crear cuenta." // Impresión de un mensaje.
	Escribir "- Ingrese sus datos personales en los campos correspondientes:" // Impresión de un mensaje.
	Escribir " - Nombre(s): " // Impresión de un mensaje.
	// Se solicita al usuario ingresar su(s) nombre(s).
	Leer nombre_s_usuario // Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un nombre válido.
	informacion_usuarios(1, 1) = nombre_s_usuario // Se agrega el dato al arreglo que contiene la información de los usuarios.
	Escribir " - Primer apellido: " // Impresión de un mensaje.
	// Se solicita al usuario ingresar su primer apellido.
	Leer primer_apellido_usuario // Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un primer apellido válido.
	informacion_usuarios(1, 2) = primer_apellido_usuario // Se agrega el dato al arreglo que contiene la información de los usuarios.
	Escribir " - Segundo apellido: " // Impresión de un mensaje.
	// Se solicita al usuario ingresar su segundo apellido.
	Leer segundo_apellido_usuario // Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un segundo apellido válido.
	informacion_usuarios(1, 3) = segundo_apellido_usuario // Se agrega el dato al arreglo que contiene la información de los usuarios.
	Escribir " - Número de teléfono: " // Impresión de un mensaje.
	// Se solicita al usuario ingresar un número de teléfono.
	Leer numero_telefono_usuario // Se revisa si todos los caracteres son dígitos o si están presentes en la lista de caracteres válidos ["+", "-", "(", ")"]. Si no se cumple esa condición, entonces no es un número de teléfono válido.
	informacion_usuarios(1, 4) = numero_telefono_usuario // Se agrega el dato al arreglo que contiene la información de los usuarios.
	Escribir " - Correo electrónico: " // Impresión de un mensaje.
	// Se solicita al usuario ingresar un correo electrónico. 
	Leer correo_electronico_usuario // Se revisa si está escrito en el formato correcto y si no está registrado.
	informacion_usuarios(1, 5) = correo_electronico_usuario // Se agrega el dato al arreglo que contiene la información de los usuarios.
	// Ciclo infinito para evaluar si la contraseña ingresada por el usuario es válida.
	Mientras contraseña_invalida Hacer // Mientras el valor lógico referente a si la contraseña ingresada no es válida sea verdadero, hacer:
		Escribir " - Contraseña: " // Impresión de un mensaje.
		// La contraseña debe incluir: 
			// Al menos ocho caracteres.
			// Al menos una letra.
			// Al menos una letra mayúscula.
			// Al menos un número.
			// Al menos un caracter que no sea una letra ni un número.
		// Asimismo:
			// No debe incluir espacios.
			// No debe incluir letras acentuadas.
			// No puede ser igual a la dirección de correo electrónico.
		Leer contraseña_usuario // Se solicita al usuario ingresar una contraseña.
		// Si la contraseña es distinta del correo electrónico ingresado y cumple con las demás condiciones mencionadas, entonces:
		Si contraseña_usuario <> correo_electronico_usuario Entonces
			contraseña_invalida = Falso // El valor lógico referente a si la contraseña ingresada no es válida se vuelve falso.
			informacion_usuarios(1, 6) = contraseña_usuario // Se agrega el dato al arreglo que contiene la información de los usuarios.
		SiNo // Si no:
			Escribir "- La contraseña ingresada no es válida. Inténtelo de nuevo." // Impresión de un mensaje.
		FinSi // Fin de la estructura si-entonces.
	FinMientras // Fin del ciclo mientras.
	Escribir "- El registro ha sido exitoso." // Impresión de un mensaje.
	menu_acceso // Se llama a la función del menú de acceso.
FinFuncion // Fin de la función crear_cuenta.


Funcion iniciar_sesion // Función que permite al usuario iniciar sesión.
	Definir correo_electronico, contraseña Como Cadena // Creación de dos variables de tipo cadena: correo_electronico, contraseña.
	Definir contraseña_incorrecta Como Logico // Creación de una variable de tipo lógico: contraseña_incorrecta.
	// Inicialización de variables:
	correo_electronico = "" // Variable que almacena el correo electrónico ingresado por el usuario.
	contraseña = "" // Variable que almacena la contraseña ingresada por el usuario.
	contraseña_incorrecta = Verdadero // Valor lógico referente a si la contraseña ingresada es incorrecta.	
	Escribir "Sección: Iniciar sesión."
	Escribir "- Ingrese los siguientes datos:"
	Escribir " - Correo electrónico: " // Impresión de un mensaje.
	Leer correo_electronico // Se solicita al usuario ingresar el correo electrónico de su cuenta.
	Si correo_electronico = informacion_usuarios(1, 5) Entonces // Si el correo electrónico ingresado está registrado, entonces:
		// Ciclo infinito para evaluar si la contraseña ingresada por el usuario corresponde a la de su cuenta.
		Mientras contraseña_incorrecta Hacer // Mientras el valor lógico referente a si la contraseña ingresada es incorrecta sea verdadero, hacer:
			Escribir " - Contraseña: " // Impresión de un mensaje.
			Leer contraseña // Se solicita al usuario ingresar la contraseña de su cuenta.
			// Si la contraseña ingresada corresponde a la contraseña de su cuenta, entonces:
			Si contraseña = informacion_usuarios(1, 6) Entonces
				contraseña_incorrecta = Falso // El valor lógico referente a si la contraseña ingresada es incorrecta se vuelve falso.
			SiNo // Si no:
				Escribir "- La contraseña ingresada es incorrecta. Inténtelo de nuevo." // Impresión de un mensaje.
			FinSi // Fin de la estructura si-entonces.
		FinMientras // Fin del ciclo mientras.
		menu_inicio // Se llama a la función del menú de inicio.
	SiNo // Si no:
		Escribir "- No pudimos encontrar tu cuenta" // Impresión de un mensaje.
		opciones_menu_acceso // Se llama a la función correspondiente para mostrar al usuario las opciones a elegir.
	FinSi // Fin de la estructura si-entonces.
FinFuncion // Fin de la función iniciar_sesión.

Funcion opciones_menu_inicio // Función que muestra las opciones del menú de acceso a fin de que el usuario elija una.
	Definir opcion_usuario Como Entero // Creación de una variable de tipo entero: opcion_usuario.
	// Inicialización de la variable:
	opcion_usuario = 0 // Variable que almacena la opción elegida por el usuario.
	Escribir "- Seleccione una de las siguientes opciones:" // Impresión de un mensaje.
	Escribir " 1-. Mi perfil." // Impresión de un mensaje.
	Escribir " 2-. Mis reservaciones." // Impresión de un mensaje.
	Escribir " 3-. Disponibilidad de bicicletas." // Impresión de un mensaje.
	Escribir " 4-. Hacer una reservación."
	Escribir " 5-. Cerrar sesión."
	Escribir " 6-. Salir del sistema."
	Leer opcion_usuario 
	Segun opcion_usuario Hacer 
		1: 
			Escribir "Sección: Mi perfil." 
		2: 
			Escribir "Sección: Mis reservaciones."
		3:
			Escribir "Sección: Disponibilidad de bicicletas."
		4:
			Escribir "Sección: Hacer una reservación."
		5:
			Escribir "Sección: Cerrar sesión."
		6:
			Escribir "Sección: Salir del sistema."
	FinSegun 
FinFuncion 

Funcion menu_inicio // Función que corresponde al menú de inicio.
	Escribir "Sección: Menú de inicio." // Impresión de un mensaje.
	opciones_menu_inicio
FinFuncion // Fin de la función menu_inicio.

Algoritmo PedalRide_Rentals_Algoritmos_Parte_1 // Inicio del algoritmo.
    Dimension informacion_usuarios(1, 6) // Inicialización de un arreglo que contendrá la información de los usuarios registrados. Para este caso, solo se contempla a un usuario registrado.
	Escribir "¡Bienvenido(a) al sistema de reservaciones para el servicio de alquiler de bicicletas!" // Impresión de un mensaje.
    menu_acceso // Se llama a la función del menú de acceso.
FinAlgoritmo // Fin del algoritmo.

