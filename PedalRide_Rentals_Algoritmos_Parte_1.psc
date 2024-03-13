Funcion opciones_menu_acceso // Funci�n que muestra las opciones del men� de acceso a fin de que el usuario elija una.
	Definir opcion_usuario Como Entero // Creaci�n de una variable de tipo entero: opcion_usuario.
	// Inicializaci�n de la variable:
	opcion_usuario = 0 // Variable que almacena la opci�n elegida por el usuario.
	Escribir "- Seleccione una de las siguientes opciones:" // Impresi�n de un mensaje.
	Escribir " 1-. Iniciar sesi�n." // Impresi�n de un mensaje.
	Escribir " 2-. Crear cuenta." // Impresi�n de un mensaje.
	Escribir " 3-. Salir del sistema." // Impresi�n de un mensaje.
	Leer opcion_usuario // Pedir al usuario que elija una opci�n.
	Segun opcion_usuario Hacer // Un switch case que evalua el input del usuario.
		1: // En caso de que haya ingresado el n�mero 1:
			iniciar_sesion // Acceder� a la secci�n para iniciar sesi�n.
		2: // En caso de que haya ingresado el n�mero 2:
			crear_cuenta // Acceder� a la secci�n para crear una cuenta.
	FinSegun // Fin del switch case.
FinFuncion // Fin de la funci�n opciones_menu_acceso.


Funcion menu_acceso // Funci�n que corresponde al men� de acceso.
	Escribir "Secci�n: Men� de acceso." // Impresi�n de un mensaje.
	opciones_menu_acceso // Se llama a la funci�n correspondiente para mostrar al usuario las opciones a elegir en el men� de acceso.
FinFuncion // Fin de la funci�n menu_acceso.


Funcion crear_cuenta // Funci�n que permite al usuario crear una cuenta.
	// Creaci�n de seis variables de tipo cadena: nombre_s_usuario, primer_apellido_usuario, segundo_apellido_usuario, numero_telefono_usuario, correo_electronico_usuario, contrase�a_usuario.
	Definir nombre_s_usuario, primer_apellido_usuario, segundo_apellido_usuario, numero_telefono_usuario, correo_electronico_usuario, contrase�a_usuario Como Cadena
	Definir contrase�a_invalida Como Logico // Creaci�n de una variable de tipo l�gico: contrase�a_invalida.
	// Inicializaci�n de variables:
	nombre_s_usuario = "" // Variable que almacena el/los nombre(s) ingresado(s) por el usuario.
	primer_apellido_usuario = "" // Variable que almacena el primer apellido ingresado por el usuario.
	segundo_apellido_usuario = "" // Variable que almacena el segundo apellido ingresado por el usuario.
	numero_telefono_usuario = "" // Variable que almacena el n�mero de tel�fono ingresado por el usuario.
	correo_electronico_usuario = "" // Variable que almacena el correo electr�nico ingresado por el usuario.
	contrase�a_usuario = "" // Variable que almacena la contrase�a ingresada por el usuario.
	contrase�a_invalida = Verdadero // Valor l�gico referente a si la contrase�a ingresada no es v�lida.	
	Escribir "Secci�n: Crear cuenta." // Impresi�n de un mensaje.
	Escribir "- Ingrese sus datos personales en los campos correspondientes:" // Impresi�n de un mensaje.
	Escribir " - Nombre(s): " // Impresi�n de un mensaje.
	// Se solicita al usuario ingresar su(s) nombre(s).
	Leer nombre_s_usuario // Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condici�n, entonces no es un nombre v�lido.
	informacion_usuarios(1, 1) = nombre_s_usuario // Se agrega el dato al arreglo que contiene la informaci�n de los usuarios.
	Escribir " - Primer apellido: " // Impresi�n de un mensaje.
	// Se solicita al usuario ingresar su primer apellido.
	Leer primer_apellido_usuario // Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condici�n, entonces no es un primer apellido v�lido.
	informacion_usuarios(1, 2) = primer_apellido_usuario // Se agrega el dato al arreglo que contiene la informaci�n de los usuarios.
	Escribir " - Segundo apellido: " // Impresi�n de un mensaje.
	// Se solicita al usuario ingresar su segundo apellido.
	Leer segundo_apellido_usuario // Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condici�n, entonces no es un segundo apellido v�lido.
	informacion_usuarios(1, 3) = segundo_apellido_usuario // Se agrega el dato al arreglo que contiene la informaci�n de los usuarios.
	Escribir " - N�mero de tel�fono: " // Impresi�n de un mensaje.
	// Se solicita al usuario ingresar un n�mero de tel�fono.
	Leer numero_telefono_usuario // Se revisa si todos los caracteres son d�gitos o si est�n presentes en la lista de caracteres v�lidos ["+", "-", "(", ")"]. Si no se cumple esa condici�n, entonces no es un n�mero de tel�fono v�lido.
	informacion_usuarios(1, 4) = numero_telefono_usuario // Se agrega el dato al arreglo que contiene la informaci�n de los usuarios.
	Escribir " - Correo electr�nico: " // Impresi�n de un mensaje.
	// Se solicita al usuario ingresar un correo electr�nico. 
	Leer correo_electronico_usuario // Se revisa si est� escrito en el formato correcto y si no est� registrado.
	informacion_usuarios(1, 5) = correo_electronico_usuario // Se agrega el dato al arreglo que contiene la informaci�n de los usuarios.
	// Ciclo infinito para evaluar si la contrase�a ingresada por el usuario es v�lida.
	Mientras contrase�a_invalida Hacer // Mientras el valor l�gico referente a si la contrase�a ingresada no es v�lida sea verdadero, hacer:
		Escribir " - Contrase�a: " // Impresi�n de un mensaje.
		// La contrase�a debe incluir: 
			// Al menos ocho caracteres.
			// Al menos una letra.
			// Al menos una letra may�scula.
			// Al menos un n�mero.
			// Al menos un caracter que no sea una letra ni un n�mero.
		// Asimismo:
			// No debe incluir espacios.
			// No debe incluir letras acentuadas.
			// No puede ser igual a la direcci�n de correo electr�nico.
		Leer contrase�a_usuario // Se solicita al usuario ingresar una contrase�a.
		// Si la contrase�a es distinta del correo electr�nico ingresado y cumple con las dem�s condiciones mencionadas, entonces:
		Si contrase�a_usuario <> correo_electronico_usuario Entonces
			contrase�a_invalida = Falso // El valor l�gico referente a si la contrase�a ingresada no es v�lida se vuelve falso.
			informacion_usuarios(1, 6) = contrase�a_usuario // Se agrega el dato al arreglo que contiene la informaci�n de los usuarios.
		SiNo // Si no:
			Escribir "- La contrase�a ingresada no es v�lida. Int�ntelo de nuevo." // Impresi�n de un mensaje.
		FinSi // Fin de la estructura si-entonces.
	FinMientras // Fin del ciclo mientras.
	Escribir "- El registro ha sido exitoso." // Impresi�n de un mensaje.
	menu_acceso // Se llama a la funci�n del men� de acceso.
FinFuncion // Fin de la funci�n crear_cuenta.


Funcion iniciar_sesion // Funci�n que permite al usuario iniciar sesi�n.
	Definir correo_electronico, contrase�a Como Cadena // Creaci�n de dos variables de tipo cadena: correo_electronico, contrase�a.
	Definir contrase�a_incorrecta Como Logico // Creaci�n de una variable de tipo l�gico: contrase�a_incorrecta.
	// Inicializaci�n de variables:
	correo_electronico = "" // Variable que almacena el correo electr�nico ingresado por el usuario.
	contrase�a = "" // Variable que almacena la contrase�a ingresada por el usuario.
	contrase�a_incorrecta = Verdadero // Valor l�gico referente a si la contrase�a ingresada es incorrecta.	
	Escribir "Secci�n: Iniciar sesi�n."
	Escribir "- Ingrese los siguientes datos:"
	Escribir " - Correo electr�nico: " // Impresi�n de un mensaje.
	Leer correo_electronico // Se solicita al usuario ingresar el correo electr�nico de su cuenta.
	Si correo_electronico = informacion_usuarios(1, 5) Entonces // Si el correo electr�nico ingresado est� registrado, entonces:
		// Ciclo infinito para evaluar si la contrase�a ingresada por el usuario corresponde a la de su cuenta.
		Mientras contrase�a_incorrecta Hacer // Mientras el valor l�gico referente a si la contrase�a ingresada es incorrecta sea verdadero, hacer:
			Escribir " - Contrase�a: " // Impresi�n de un mensaje.
			Leer contrase�a // Se solicita al usuario ingresar la contrase�a de su cuenta.
			// Si la contrase�a ingresada corresponde a la contrase�a de su cuenta, entonces:
			Si contrase�a = informacion_usuarios(1, 6) Entonces
				contrase�a_incorrecta = Falso // El valor l�gico referente a si la contrase�a ingresada es incorrecta se vuelve falso.
			SiNo // Si no:
				Escribir "- La contrase�a ingresada es incorrecta. Int�ntelo de nuevo." // Impresi�n de un mensaje.
			FinSi // Fin de la estructura si-entonces.
		FinMientras // Fin del ciclo mientras.
		menu_inicio // Se llama a la funci�n del men� de inicio.
	SiNo // Si no:
		Escribir "- No pudimos encontrar tu cuenta" // Impresi�n de un mensaje.
		opciones_menu_acceso // Se llama a la funci�n correspondiente para mostrar al usuario las opciones a elegir.
	FinSi // Fin de la estructura si-entonces.
FinFuncion // Fin de la funci�n iniciar_sesi�n.

Funcion opciones_menu_inicio // Funci�n que muestra las opciones del men� de acceso a fin de que el usuario elija una.
	Definir opcion_usuario Como Entero // Creaci�n de una variable de tipo entero: opcion_usuario.
	// Inicializaci�n de la variable:
	opcion_usuario = 0 // Variable que almacena la opci�n elegida por el usuario.
	Escribir "- Seleccione una de las siguientes opciones:" // Impresi�n de un mensaje.
	Escribir " 1-. Mi perfil." // Impresi�n de un mensaje.
	Escribir " 2-. Mis reservaciones." // Impresi�n de un mensaje.
	Escribir " 3-. Disponibilidad de bicicletas." // Impresi�n de un mensaje.
	Escribir " 4-. Hacer una reservaci�n."
	Escribir " 5-. Cerrar sesi�n."
	Escribir " 6-. Salir del sistema."
	Leer opcion_usuario 
	Segun opcion_usuario Hacer 
		1: 
			Escribir "Secci�n: Mi perfil." 
		2: 
			Escribir "Secci�n: Mis reservaciones."
		3:
			Escribir "Secci�n: Disponibilidad de bicicletas."
		4:
			Escribir "Secci�n: Hacer una reservaci�n."
		5:
			Escribir "Secci�n: Cerrar sesi�n."
		6:
			Escribir "Secci�n: Salir del sistema."
	FinSegun 
FinFuncion 

Funcion menu_inicio // Funci�n que corresponde al men� de inicio.
	Escribir "Secci�n: Men� de inicio." // Impresi�n de un mensaje.
	opciones_menu_inicio
FinFuncion // Fin de la funci�n menu_inicio.

Algoritmo PedalRide_Rentals_Algoritmos_Parte_1 // Inicio del algoritmo.
    Dimension informacion_usuarios(1, 6) // Inicializaci�n de un arreglo que contendr� la informaci�n de los usuarios registrados. Para este caso, solo se contempla a un usuario registrado.
	Escribir "�Bienvenido(a) al sistema de reservaciones para el servicio de alquiler de bicicletas!" // Impresi�n de un mensaje.
    menu_acceso // Se llama a la funci�n del men� de acceso.
FinAlgoritmo // Fin del algoritmo.

