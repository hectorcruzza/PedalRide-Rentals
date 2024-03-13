import pandas as pd # Importación de librería para la carga de información del sistema
from email_validator import validate_email, EmailNotValidError # Importación de librería para la verificación de correos electrónicos
import re # Importación de librería para la creación de regular expressions
import datetime as dt

class PedalRide_Rentals: # Creación de la clase.
    def __init__(self, df: pd.DataFrame, df_reservaciones_confirmadas: pd.DataFrame, df_reservaciones_en_curso: pd.DataFrame): # Función de inicialización.
        self.obtener_fecha_hora()

        self.bicicletas = ["010", "020", "030", "040", "067"] # Inicialización de la lista de bicicletas a alquilar.
        self.df = df #Cargar la información de los usuarios
        self.df_reservaciones_confirmadas = df_reservaciones_confirmadas
        self.df_reservaciones_en_curso = df_reservaciones_en_curso

        self.verificar_reservaciones_confirmadas()

        self.nombre_usuario = None
        self.primer_apellido_usuario = None
        self.segundo_apellido_usuario = None
        self.numero_telefono_usuario = None
        self.correo_electronico_usuario = None
        self.contraseña_usuario = None
        self.inicio_sesion_exitoso = None
        print(f"\n| Fecha: {self.fecha_actual} - Hora: {self.hora_actual} |")
        print("\n¡Bienvenido(a) al sistema de reservaciones para el servicio de alquiler de bicicletas!") # Impresión de un mensaje.
        self.menu_acceso() # Se llama a la función del menú de acceso.

    def obtener_fecha_hora(self):
        self.fecha_hora_actual_datetime = dt.datetime.now().replace(microsecond = 0)
        self.fecha_actual = self.fecha_hora_actual_datetime.strftime("%d/%m/%Y")
        self.hora_actual = self.fecha_hora_actual_datetime.strftime("%H:%M")

    def verificar_reservaciones_confirmadas(self):
        informacion_reservaciones_confirmadas = self.df_reservaciones_confirmadas[["Fecha de la Reservación", "Hora de Inicio"]].to_numpy()

        for i in range(len(self.df_reservaciones_confirmadas)):
            fecha_hora_reservacion_str = f"{informacion_reservaciones_confirmadas[i][0]} {informacion_reservaciones_confirmadas[i][1]}"
            fecha_hora_reservacion_datetime = dt.datetime.strptime(fecha_hora_reservacion_str, "%d/%m/%Y %H:%M").replace()
            if self.fecha_hora_actual_datetime >= fecha_hora_reservacion_datetime:
                self.df_reservaciones_confirmadas.drop(i, inplace = True)
                self.df_reservaciones_confirmadas.to_csv("reservaciones_confirmadas.csv", index = None)   
                self.df_reservaciones_confirmadas = pd.read_csv("reservaciones_confirmadas.csv", dtype = str)

    def verificar_reservaciones_en_curso(self):
        pass   


    def opciones_menu_acceso(self): # Función que muestra las opciones del menú de acceso a fin de que el usuario elija una.
        print("- Seleccione una de las siguientes opciones con base en su número: \n") # Impresión de un mensaje.
        print(" 1-. Iniciar sesión.") # Impresión de un mensaje.
        print(" 2-. Crear cuenta.") # Impresión de un mensaje.
        print(" 3-. Salir del sistema.") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.iniciar_sesion() # Accederá a la sección para iniciar sesión.
            case "2": # En caso de que haya ingresado el número 2:
                self.crear_cuenta() # Accederá a la sección para crear una cuenta.
            case "3":
                print("\nHa abandonado el sistema.")
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_menu_acceso()


    def menu_acceso(self): # Función que corresponde al menú de acceso.
        print("\nSección: Menú de acceso.") # Impresión de un mensaje.
        self.opciones_menu_acceso() # Se llama a la función correspondiente para mostrar al usuario las opciones a elegir en el menú de acceso.


    def opciones_post_crear_cuenta(self):
        print("- Seleccione una de las siguientes opciones con base en su número: \n") # Impresión de un mensaje.
        if self.inicio_sesion_exitoso != None:
            print(" 1-. ¿Quiere volver a intentar iniciar sesión?") # Impresión de un mensaje.
        else:
            print(" 1-. ¿Quiere iniciar sesión?") # Impresión de un mensaje.
        print(" 2-. ¿Desea volver al menú de acceso?") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.iniciar_sesion() # Accederá a la sección para iniciar sesión.
            case "2": # En caso de que haya ingresado el número 2:
                self.menu_acceso() 
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_post_crear_cuenta()


    def crear_cuenta(self): # Función que permite al usuario crear una cuenta.
        self.inicio_sesion_exitoso = None
        print("\nSección: Crear cuenta.") # Impresión de un mensaje.
        print("- Ingrese sus datos personales en los campos correspondientes:\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si el/los nombre(s) ingresado(s) por el usuario es válido.
            nombre_valido = True # Valor lógico referente a si el nombre ingresado es válido.
            nombre_usuario = input(" - Nombre(s): > ") # Se solicita al usuario ingresar su(s) nombre(s).
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del nombre, y se convierten todos los caracteres a minúsculas.
            # La letra inicial de cada nombre se convierte en mayúscula.
            nombre_usuario = " ".join([nombre.capitalize() for nombre in nombre_usuario.strip().lower().split()])
            # Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un nombre válido.
            nombre_valido = all(caracter.isalpha() or caracter.isspace() for caracter in nombre_usuario)
            # Si el valor lógico referente a si el nombre ingresado es válido es verdadero y la cantidad de caracteres del nombre es mayor o igual a dos, entonces:
            if len(nombre_usuario) >= 2 and nombre_valido:
                break # Termina el ciclo.
            print("El/los nombre(s) ingresado(s) no es/son válido(s). Inténtelo de nuevo.\n") # Impresión de un mensaje.

        print()

        while True: # Ciclo infinito para evaluar si el primer apellido ingresado por el usuario es válido.
            primer_apellido_valido = True # Valor lógico referente a si el primer apellido ingresado es válido.
            primer_apellido_usuario = input(" - Primer apellido: > ") # Se solicita al usuario ingresar su primer apellido.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del primer apellido, y se convierten todos los caracteres a minúsculas.
            # La letra inicial del primer apellido se convierte en mayúscula.
            primer_apellido_usuario = " ".join([apellido.capitalize() for apellido in primer_apellido_usuario.strip().lower().split()])
            # Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un primer apellido válido.
            primer_apellido_valido = all(caracter.isalpha() or caracter.isspace() for caracter in primer_apellido_usuario)
            # Si la cantidad de caracteres del primer apellido es mayor o igual a dos y el valor lógico referente a si el primer apellido ingresado es válido es verdadero, entonces:
            if len(primer_apellido_usuario) >= 2 and primer_apellido_valido:
                print()
                break # Termina el ciclo.
            print("El primer apellido ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si el segundo apellido ingresado por el usuario es válido.
            segundo_apellido_valido = True # Valor lógico referente a si el segundo apellido ingresado es válido.
            segundo_apellido_usuario = input(" - Segundo apellido: > ") # Se solicita al usuario ingresar su segundo apellido.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del segundo apellido, y se convierten todos los caracteres a minúsculas.
            # La letra inicial del segundo apellido se convierte en mayúscula.
            segundo_apellido_usuario = " ".join([apellido.capitalize() for apellido in segundo_apellido_usuario.strip().lower().split()])
            # Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un segundo apellido válido.
            segundo_apellido_valido = all(caracter.isalpha() or caracter.isspace() for caracter in segundo_apellido_usuario)
            # Si la cantidad de caracteres del segundo apellido es mayor o igual a dos y el valor lógico referente a si el segundo apellido ingresado es válido es verdadero, entonces:
            if len(segundo_apellido_usuario) >= 2 and segundo_apellido_valido:
                print()
                break # Termina el ciclo.
            print("El segundo apellido ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si el número de teléfono ingresado por el usuario es válido.
            caracteres_validos = ["+", "-", "(", ")"] # Lista de caracteres que puede tener un número de teléfono.
            numero_telefono_valido = True # Valor lógico referente a si el número de teléfono ingresado es válido.
            numero_telefono_usuario = input(" - Número de teléfono: > ") # Se solicita al usuario ingresar un número de teléfono.
            # Se remueven los espacios en blanco encontrados al inicio, al final y dentro del string del número de teléfono.
            numero_telefono_usuario = numero_telefono_usuario.strip().replace(" ", "")
            # Se revisa si todos los caracteres son dígitos o si están presentes en la lista de caracteres válidos. Si no se cumple esa condición, entonces no es un número de teléfono válido.
            numero_telefono_valido = all(caracter.isdigit() or caracter in caracteres_validos for caracter in numero_telefono_usuario)
            # Si la cantidad de caracteres del número de teléfono es mayor o igual a 5 y menor o igual a 15, y el valor lógico referente a si el número de teléfono ingresado es válido es verdadero, entonces:
            if (len(numero_telefono_usuario) >= 5 and len(numero_telefono_usuario) <= 15) and numero_telefono_valido:
                print()
                break # Termina el ciclo.
            print("El número de teléfono ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si el correo electrónico ingresado por el usuario es válido.
            correo_electronico_usuario = input(" - Correo electrónico: > ") # Se solicita al usuario ingresar un correo electrónico.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del correo electrónico.
            correo_electronico_usuario = correo_electronico_usuario.strip()

            try: # Se intenta validar el correo electrónico.
                # Se valida el correo electrónico y se almacena en su formato normalizado.
                correo_electronico_usuario = validate_email(correo_electronico_usuario).email
                # Si el correo electrónico ingresado no está registrado, entonces:
                if correo_electronico_usuario not in list(self.df["Correo Electrónico"]):
                    print()
                    break # Termina el ciclo.
                print("El correo electrónico ingresado ya está registrado. Intente con uno distinto.\n") # Impresión de un mensaje.
            except EmailNotValidError: # Si no es válido el correo electrónico, ocurre un error.
                print("El correo electrónico ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        print(" - Elija una contraseña para su cuenta.") # Impresión de un mensaje.

        print("  - La contraseña debe incluir: ") # Impresión de un mensaje.
        print("   - Al menos ocho caracteres.") # Impresión de un mensaje.
        print("   - Al menos una letra y una letra mayúscula.") # Impresión de un mensaje.
        print("   - Al menos un número.") # Impresión de un mensaje.
        print("   - Al menos un caracter que no sea una letra ni un número.") # Impresión de un mensaje.
        print("  - Además: ") # Impresión de un mensaje.
        print("   - No debe incluir espacios y letras acentuadas.") # Impresión de un mensaje.
        print("   - No puede ser idéntica a la dirección de correo electrónico.\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si la contraseña ingresada por el usuario es válida.
            contraseña_usuario = input(" - Contraseña: > ") # Se solicita al usuario ingresar una contraseña.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string de la contraseña.
            contraseña_usuario = contraseña_usuario.strip()
            regex = r"^(?=.*[a-zA-Z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])(?!.*[áéíóúüñ\s]).{8,}$" # Regular expression para verificar que la contraseña cumpla con las condiciones mencionadas.
            if re.match(regex, contraseña_usuario) and contraseña_usuario != correo_electronico_usuario: #Si la contraseña cumple con las condiciones mencionadas, entonces:
                break # Termina el ciclo.
            print("La contraseña ingresada no cumple con las especificaciones mencionadas. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        # Almacenar la información del usuario registrado en un diccionario para su posterior carga en el archivo csv de los usuarios.
        informacion_usuario = {
            "Nombre(s)": [nombre_usuario], # Nombre(s).
            "Primer Apellido": [primer_apellido_usuario], # Primer apellido.
            "Segundo Apellido": [segundo_apellido_usuario], # Segundo apellido.
            "Número de Teléfono": [numero_telefono_usuario], # Número de teléfono.
            "Correo Electrónico": [correo_electronico_usuario], # Correo electrónico.
            "Contraseña": [contraseña_usuario] # Contraseña.
            }
        
        df_informacion_usuario = pd.DataFrame(informacion_usuario, dtype = str) # Convertir el diccionario con la información del usuario registrado a un dataframe.
        # Se crea un nuevo dataframe concatenando el dataframe que contiene la información del usuario registrado con el dataframe del csv de los usuarios.
        df_modificado = pd.concat([self.df, df_informacion_usuario], ignore_index = True) 
        df_modificado.reset_index() # Se resetean los index del nuevo dataframe.
        df_modificado.to_csv("usuarios.csv", index = None) # Se guarda el nuevo dataframe en el archivo csv de los usuarios (se sobrescribe el contenido).
        self.df = pd.read_csv("usuarios.csv", dtype = str) # Se vuelve a leer el contenido del archivo csv de los usuarios.

        print("\nEl registro ha sido exitoso.\n") # Impresión de un mensaje.

        self.opciones_post_crear_cuenta() # Se muestran las opciones que puede elegir el usuario después de haber creado su cuenta.

    
    def proceso_inicio_sesion(self):
        self.inicio_sesion_exitoso = None
        print("- Ingrese el correo electrónico y contraseña de su cuenta:\n") # Impresión de un mensaje.
        correo_electronico = input(" - Correo electrónico: > ") # Se solicita al usuario ingresar el correo electrónico de su cuenta.
        if correo_electronico in list(self.df["Correo Electrónico"]): # Si el correo electrónico ingresado está registrado, entonces:
            print()
            while True: # Ciclo infinito para evaluar si la contraseña ingresada por el usuario corresponde a la de su cuenta.
                self.contraseña_usuario = input(" - Contraseña: > ") # Se solicita al usuario ingresar la contraseña de su cuenta.
                # Si la contraseña ingresada corresponde a la contraseña de su cuenta, entonces:
                informacion_usuario_logeado = list(self.df.loc[self.df["Correo Electrónico"] == correo_electronico].iloc[0])
                if self.contraseña_usuario == informacion_usuario_logeado[5]:
                    self.nombre_usuario = informacion_usuario_logeado[0]
                    self.primer_apellido_usuario = informacion_usuario_logeado[1]
                    self.segundo_apellido_usuario = informacion_usuario_logeado[2]
                    self.numero_telefono_usuario = informacion_usuario_logeado[3]
                    self.correo_electronico_usuario = informacion_usuario_logeado[4]
                    break # Termina el ciclo.
                print("La contraseña ingresada es incorrecta. Inténtelo de nuevo.\n") # Impresión de un mensaje.
            self.menu_inicio() # Se llama a la función del menú de inicio.
        else:
            print("No pudimos encontrar tu cuenta.\n")
            self.inicio_sesion_exitoso = False
            self.opciones_post_crear_cuenta() # Se llama a la función correspondiente para mostrar al usuario las opciones a elegir.


    def iniciar_sesion(self): # Función que permite al usuario iniciar sesión.
        print("\nSección: Iniciar sesión.")
        self.proceso_inicio_sesion()


    def opciones_menu_inicio(self): # Función que muestra las opciones del menú de acceso a fin de que el usuario elija una.
        print("- Seleccione una de las siguientes opciones con base en su número:\n") # Impresión de un mensaje.
        print(" 1-. Mi perfil.") # Impresión de un mensaje.
        print(" 2-. Mis reservaciones.") # Impresión de un mensaje.
        print(" 3-. Disponibilidad de bicicletas.") # Impresión de un mensaje.
        print(" 4-. Hacer una reservación.") # Impresión de un mensaje.
        print(" 5-. Cerrar sesión.") # Impresión de un mensaje.
        print(" 6-. Salir del sistema.") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.mi_perfil()
            case "2": # En caso de que haya ingresado el número 2:
                self.mis_reservaciones()
            case "3":
                print("\nSección: Disponibilidad de bicicletas.")
            case "4":
                self.hacer_reservaciones()
            case "5":
                self.nombre_usuario = None
                self.primer_apellido_usuario = None
                self.segundo_apellido_usuario = None
                self.numero_telefono_usuario = None
                self.correo_electronico_usuario = None
                self.contraseña_usuario = None
                self.menu_acceso()
            case "6":
                print(f"\nGracias {self.nombre_usuario} por usar nuestro sistema..")
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_menu_inicio()


    def menu_inicio(self): # Función que corresponde al menú de inicio.
        self.obtener_fecha_hora()
        print(f"\n| Fecha: {self.fecha_actual} - Hora: {self.hora_actual} |")
        print("\nSección: Menú de inicio.") # Impresión de un mensaje.
        self.opciones_menu_inicio()


    def opcion_mi_perfil(self):
        print("- Seleccione la opción con base en su número:\n")
        print(" 1-. Volver al menú de inicio.")
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.menu_inicio()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_mis_reservaciones()


    def mi_perfil(self):
        print("\nSección: Mi perfil.") # Impresión de un mensaje.
        print("- Información personal:\n")
        print(f" - Nombre(s): {self.nombre_usuario}")
        print(f" - Primer apellido: {self.primer_apellido_usuario}")
        print(f" - Segundo apellido: {self.segundo_apellido_usuario}")
        print(f" - Número de teléfono: {self.numero_telefono_usuario}")
        print(f" - Correo electrónico: {self.correo_electronico_usuario}")
        print(f" - Contraseña: {self.contraseña_usuario}\n")

        self.opcion_mi_perfil()


    def opciones_mis_reservaciones(self):
        print("- Seleccione una de las siguientes opciones con base en su número:\n") # Impresión de un mensaje.
        print(" 1-. Hacer una reservación.") # Impresión de un mensaje.
        print(" 2-. Cancelar una reservación.") # Impresión de un mensaje.
        print(" 3-. Volver al menú de inicio.") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.hacer_reservaciones()
            case "2": # En caso de que haya ingresado el número 2:
                print("\nSección: Cancelar una reservación.")
            case "3":
                self.menu_inicio()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_mis_reservaciones()
    

    def mis_reservaciones(self):
        self.obtener_fecha_hora()
        self.verificar_reservaciones_confirmadas()
        print("\nSección: Mis reservaciones.")
        print("- Reservaciones confirmadas:\n")

        reservaciones_confirmadas = self.df_reservaciones_confirmadas.loc[self.df_reservaciones_confirmadas["Correo Electrónico"] == self.correo_electronico_usuario].to_numpy()

        if len(reservaciones_confirmadas):
            print("| N.º de Reservación |    Fecha    |    Horario    | N.º de Bicicleta |  Costo  |")
            for j in range(len(reservaciones_confirmadas)):
                horario_reserva = f"{reservaciones_confirmadas[j][5]} - {reservaciones_confirmadas[j][6]}"
                print("        ", reservaciones_confirmadas[j][0], "           ", reservaciones_confirmadas[j][4], "  ", horario_reserva, "       ", reservaciones_confirmadas[j][7], "         ", reservaciones_confirmadas[j][8])
        else:
            print(" - No tiene ninguna reservación confirmada.")
            print()
        self.opciones_mis_reservaciones()


    def opciones_hacer_reservaciones(self):
        print("- Seleccione una de las siguientes opciones con base en su número: \n") # Impresión de un mensaje.
        if not self.bicicletas_disponibles:
            print(" 1-. Cambiar la fecha y horario de la reservación.") # Impresión de un mensaje.
        elif not self.acuerdo_precio_usuario:   
            print(" 1-. Hacer una reservación.") # Impresión de un mensaje.
        else:
            print(" 1-. Hacer otra reservación.")
        print(" 2-. Volver al menú de inicio.") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.proceso_hacer_reservaciones() # Accederá a la sección para iniciar sesión.
            case "2": # En caso de que haya ingresado el número 2:
                self.menu_inicio()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_hacer_reservaciones()


    def proceso_hacer_reservaciones(self):
        print(f"\n| Fecha: {self.fecha_actual} - Hora: {self.hora_actual} |\n")
        dia_actual = self.fecha_hora_actual_datetime.day
        mes_actual = self.fecha_hora_actual_datetime.month
        año_actual = self.fecha_hora_actual_datetime.year
        horas_actual = self.fecha_hora_actual_datetime.hour
        minutos_actual = self.fecha_hora_actual_datetime.minute
        costo_reserva_por_hora = 60

        print("- Nuestro horario de trabajo es de las 08:00 a las 20:00.")
        print("- Las reservaciones se deben realizar para el año y mes en curso.")
        print("- Las reservaciones se realizan en bloques por hora.")
        print("- Las reservaciones pueden ser de más de una hora.")
        print("- Las reservaciones se deben realizar con al menos una hora de anticipación.\n")

        while True:
            fecha_reserva = input(" - Ingrese la fecha de la reservación (Formato: DD/MM/AAAA): > ")
            formato_fecha = r"^\d{2}/\d{2}/\d{4}$"
            if re.match(formato_fecha, fecha_reserva):
                try:
                    fecha_reserva_datetime = dt.datetime.strptime(fecha_reserva, "%d/%m/%Y").date()
                    dia_reserva = fecha_reserva_datetime.day
                    mes_reserva = fecha_reserva_datetime.month
                    año_reserva = fecha_reserva_datetime.year
                    if año_reserva == año_actual and mes_reserva == mes_actual:
                        if dia_reserva >= dia_actual:
                            print()
                            break
                        else:
                            print("El día de la reservación ingresado no es válido. Inténtelo de nuevo.\n")
                    else:
                        print("La fecha de la reservación ingresada no cumple con los parámetros establecidos. Inténtelo de nuevo.\n")
                except:
                    print("La fecha ingresada no es válida. Inténtelo de nuevo.\n")
            else:
                print("El formato de la fecha ingresada no es válido. Inténtelo de nuevo.\n")
            print("- Recuerde que las reservaciones se deben realizar para el año y mes en curso.\n")

        while True:
            while True:
                hora_inicio_reserva = input(" - Ingrese la hora de inicio de la reservación (Formato de 24 horas: HH:MM): > ")
                formato_hora = r"^\d{2}:\d{2}$"
                if re.match(formato_hora, hora_inicio_reserva):
                    try:
                        hora_inicio_reserva_datetime = dt.datetime.strptime(hora_inicio_reserva, "%H:%M").time()
                        horas_inicio_reserva = hora_inicio_reserva_datetime.hour
                        minutos_inicio_reserva = hora_inicio_reserva_datetime.minute
                        print()
                        break
                    except:
                        print("La hora de inicio ingresada no es válida. Inténtelo de nuevo.\n")
                else:
                    print("El formato de la hora de inicio ingresada no es válido. Inténtelo de nuevo.\n")

            while True:
                hora_termino_reserva = input(" - Ingrese la hora de término de la reservación (Formato de 24 horas: HH:MM): > ")
                if re.match(formato_hora, hora_termino_reserva):
                    try:
                        hora_termino_reserva_datetime = dt.datetime.strptime(hora_termino_reserva, "%H:%M").time()
                        horas_termino_reserva = hora_termino_reserva_datetime.hour
                        minutos_termino_reserva = hora_termino_reserva_datetime.minute
                        print()
                        break
                    except:
                        print("La hora de término ingresada no es válida. Inténtelo de nuevo.\n")
                else:
                    print("El formato de la hora de término ingresada no es válido. Inténtelo de nuevo.\n")
            
            formato_hora_reservas = r"^\d{2}:00$"
            horas_anticipacion = horas_inicio_reserva - (horas_actual + (minutos_actual / 60))
            
            if re.match(formato_hora_reservas, hora_inicio_reserva) and re.match(formato_hora_reservas, hora_termino_reserva) \
            and horas_inicio_reserva >= 8 and horas_inicio_reserva <= 20 and horas_termino_reserva >= 8 and horas_termino_reserva <=20 \
            and (fecha_reserva_datetime > self.fecha_hora_actual_datetime.date() or horas_anticipacion >= 1):
                if hora_inicio_reserva_datetime < hora_termino_reserva_datetime:
                    print()
                    break
                else:
                    print("El horario ingresado no es válido. Inténtelo de nuevo.\n")
            else:
                print("El horario ingresado no cumple con las condiciones establecidas. Inténtelo de nuevo.\n")
                print("Recuerde que:")
                print("- Nuestro horario de trabajo es de las 08:00 a las 20:00.")
                print("- Las reservaciones se realizan en bloques por hora.")
                print("- Las reservaciones pueden ser de más de una hora.")
                print("- Las reservaciones se deben realizar con al menos una hora de anticipación.\n")

        self.bicicletas_disponibles = False
        h = 0

        # Ciclo para verificar si hay bicicletas disponibles
        while h < len(self.bicicletas) and not self.bicicletas_disponibles:
            self.bicicletas_disponibles = True
            l = 0
            while l < len(self.df_reservaciones_confirmadas) and self.bicicletas_disponibles:
                if self.bicicletas[h] == self.df_reservaciones_confirmadas["Número de Bicicleta"].iloc[l]:
                    container_fecha_reserva_datetime = dt.datetime.strptime(self.df_reservaciones_confirmadas["Fecha de la Reservación"].iloc[l], "%d/%m/%Y").date()
                    container_dia_reserva = container_fecha_reserva_datetime.day
                    container_mes_reserva = container_fecha_reserva_datetime.month
                    container_año_reserva = container_fecha_reserva_datetime.year
                    if container_año_reserva == año_reserva:
                        if container_mes_reserva == mes_reserva:
                            if container_dia_reserva == dia_reserva:
                                container_hora_inicio = dt.datetime.strptime(self.df_reservaciones_confirmadas["Hora de Inicio"].iloc[l], "%H:%M").hour
                                container_hora_termino = dt.datetime.strptime(self.df_reservaciones_confirmadas["Hora de Término"].iloc[l], "%H:%M").hour
                                if horas_inicio_reserva < container_hora_termino and horas_termino_reserva > container_hora_inicio:
                                    self.bicicletas_disponibles = False
                l += 1
            h += 1

        # Si hay bicicletas disponibles, entonces se muestran y sigue el proceso de la reservación.
        if self.bicicletas_disponibles:
            print("A continuación, se muestra la lista de bicicletas disponibles en la fecha y horario elegidos:\n")
            print("| Número de Bicicleta |")

            lista_bicicletas_disponibles = list()

            for a in range(len(self.bicicletas)):
                bicicleta_disponible = True
                b = 0
                while b < len(self.df_reservaciones_confirmadas) and bicicleta_disponible:
                    if self.bicicletas[a] == self.df_reservaciones_confirmadas["Número de Bicicleta"].iloc[b]:
                        container_fecha_reserva_datetime = dt.datetime.strptime(self.df_reservaciones_confirmadas["Fecha de la Reservación"].iloc[b], "%d/%m/%Y").date()
                        container_dia_reserva = container_fecha_reserva_datetime.day
                        container_mes_reserva = container_fecha_reserva_datetime.month
                        container_año_reserva = container_fecha_reserva_datetime.year
                        if container_año_reserva == año_reserva:
                            if container_mes_reserva == mes_reserva:
                                if container_dia_reserva == dia_reserva:
                                    container_hora_inicio = dt.datetime.strptime(self.df_reservaciones_confirmadas["Hora de Inicio"].iloc[b], "%H:%M").hour
                                    container_hora_termino = dt.datetime.strptime(self.df_reservaciones_confirmadas["Hora de Término"].iloc[b], "%H:%M").hour
                                    if horas_inicio_reserva < container_hora_termino and horas_termino_reserva > container_hora_inicio:
                                        bicicleta_disponible = False
                    b += 1
                if bicicleta_disponible:
                    lista_bicicletas_disponibles.append(self.bicicletas[a])
                    print("         ", self.bicicletas[a])

            while True:
                reserva_bicicleta = input("\n - Elija la bicicleta a rentar con base en su número: > ")
                if reserva_bicicleta in lista_bicicletas_disponibles:
                    print()
                    break
                print("El número de bicicleta ingresado no es válido. Inténtelo de nuevo.\n")
            
            costo_total_reserva = f"${(horas_termino_reserva - horas_inicio_reserva) * costo_reserva_por_hora}"

            print(f"El costo total de la reservación es de {costo_total_reserva}.")

            self.acuerdo_precio_usuario = False

            while True:
                respuesta_usuario_precio = input(" - ¿Está de acuerdo con el precio (Sí/No)? > ")
                if respuesta_usuario_precio == "Sí" or respuesta_usuario_precio == "No":
                    print()
                    break
                print("La respuesta ingresada no es válida. Inténtelo de nuevo.\n")

            if respuesta_usuario_precio == "Sí":
                self.acuerdo_precio_usuario = True
                numero_reservacion = len(self.df_reservaciones_confirmadas) + 1
                apellidos = f"{self.primer_apellido_usuario} {self.segundo_apellido_usuario}"

                informacion_reservacion = {
                    "Número de Reservación": [numero_reservacion],
                    "Nombre(s)": [self.nombre_usuario],
                    "Apellidos": [apellidos],
                    "Correo Electrónico": [self.correo_electronico_usuario],
                    "Fecha de la Reservación": [fecha_reserva],
                    "Hora de Inicio": [hora_inicio_reserva],
                    "Hora de Término": [hora_termino_reserva],
                    "Número de Bicicleta": [reserva_bicicleta],
                    "Costo": [costo_total_reserva],
                    "Número de Teléfono": [self.numero_telefono_usuario]
                    }
                
                df_informacion_reservacion = pd.DataFrame(informacion_reservacion, dtype = str)
                df_reservacion_modificado = pd.concat([self.df_reservaciones_confirmadas, df_informacion_reservacion])
                df_reservacion_modificado.reset_index()
                df_reservacion_modificado.to_csv("reservaciones_confirmadas.csv", index = None)
                self.df_reservaciones_confirmadas = pd.read_csv("reservaciones_confirmadas.csv", dtype = str)

                horario_reserva = f"{hora_inicio_reserva} - {hora_termino_reserva}"

                print("Su reservación se ha realizado con éxito.")
                print("A continuación, se muestran los detalles de su reservación:\n")
                print("| N.º de Reservación |       Nombre(s)       |       Apellidos       |      Fecha      |      Horario      |")
                print("        ", numero_reservacion, "               ", self.nombre_usuario, "       ", apellidos, "       ", fecha_reserva, "     ", horario_reserva, "\n")
                print("                                       | N.º de Bicicleta |   Costo   |")
                print("                                              ", reserva_bicicleta, "          ", costo_total_reserva)
            print()
            self.opciones_hacer_reservaciones()
        else:
            print("No hay bicicletas disponibles para la fecha y horario elegidos.\n")
            self.opciones_hacer_reservaciones()


    def hacer_reservaciones(self):
        self.obtener_fecha_hora()
        self.verificar_reservaciones_confirmadas()
        print("\nSección: Hacer una reservación.")
        self.proceso_hacer_reservaciones()

        
def main(): # Función main.
    df = pd.read_csv("usuarios.csv", dtype = str) # Lectura del contenido del archivo csv de los usuarios por medio de la creación de un dataframe.
    df_reservaciones_confirmadas = pd.read_csv("reservaciones_confirmadas.csv", dtype = str)
    df_reservaciones_en_curso = pd.read_csv("reservaciones_en_curso.csv", dtype = str)

    PedalRide_Rentals(df, df_reservaciones_confirmadas, df_reservaciones_en_curso) # Se crea una instancia de la clase (se pasa como argumento el dataframe del archivo csv de los usuarios).

if __name__ == "__main__": # Si el programa es ejecutado desde el archivo principal, entonces:
    main() # Se ejecuta el código.