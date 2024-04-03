import pandas as pd # Importación de librería para la carga de información del sistema
import os
from email_validator import validate_email, EmailNotValidError # Importación de librería para la verificación de correos electrónicos
import re # Importación de librería para la creación de regular expressions
import datetime as dt
import requests
import random
import datos_correo as dc
from email.message import EmailMessage
import ssl
import smtplib

class PedalRide_Rentals: # Creación de la clase.
    def __init__(self, df: pd.DataFrame, df_reservaciones: pd.DataFrame): # Función de inicialización.
        self.obtener_fecha_hora()
        # Inicialización de la lista de bicicletas a alquilar, con su descripción y respectivo precio por hora.
        self.bicicletas = {"Bicicleta de Ciudad": ["Urbana, práctica.", ["005", "010", "015"], 60],
                           "Bicicleta de Montaña": ["Todo terreno, ágil.", ["020", "025", "030"], 90],
                           "Bicicleta de Turismo": ["Largas distancias.", ["035", "040", "045"], 80],
                           "Bicicleta BMX": ["Aventuras increíbles.", ["050", "055", "060"], 85],
                           "Bicicleta Eléctrica": ["Eficiente, rápida.", ["065", "067", "070"], 100]} 
        self.df = df
        self.df_reservaciones = df_reservaciones
        self.numeros_reservacion_disponibles = set(range(1, 1001))
        self.numeros_reservacion_disponibles.difference_update(set(self.df_reservaciones["Número de Reservación"]))
        self.inicio_programa = None
        self.nombre_usuario = None
        self.primer_apellido_usuario = None
        self.segundo_apellido_usuario = None
        self.apellidos = None
        self.numero_telefono_usuario = None
        self.correo_electronico_usuario = None
        self.contraseña_usuario = None
        self.correo_electronico_registrado = None
        self.intento_envio_codigo_verificacion = None
        self.problema_verificacion_correo = None
        self.inicio_sesion_exitoso = None
        self.reservaciones_a_cancelar = None
        self.horario_trabajo = None
        self.bicicletas_disponibles = None
        self.horario_trabajo = None
        self.confirmacion_reservacion_usuario = None
        self.limpiar_terminal()
        print("¡Bienvenido(a) a PedalRide Rentals!\n") # Impresión de un mensaje.
        self.menu_acceso() # Se llama a la función del menú de acceso.


    def obtener_fecha_hora(self):
        self.fecha_hora_actual_datetime = dt.datetime.now().replace(microsecond = 0)
        self.fecha_actual = self.fecha_hora_actual_datetime.strftime("%d/%m/%Y")
        self.hora_actual = self.fecha_hora_actual_datetime.strftime("%H:%M")


    def limpiar_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")


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
                self.limpiar_terminal()
                print("Ha abandonado el sistema.\n")
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_menu_acceso()


    def menu_acceso(self): # Función que corresponde al menú de acceso.
        if self.inicio_programa:
            self.limpiar_terminal()
        else:
            self.inicio_programa = True
        print("Sección: Menú de acceso.") # Impresión de un mensaje.
        self.opciones_menu_acceso() # Se llama a la función correspondiente para mostrar al usuario las opciones a elegir en el menú de acceso.


    def opciones_post_crear_cuenta(self):
        print("- Seleccione una de las siguientes opciones con base en su número: \n") # Impresión de un mensaje.
        if self.inicio_sesion_exitoso != None:
            print(" 1-. ¿Quiere volver a intentar iniciar sesión?") # Impresión de un mensaje.
        else:
            print(" 1-. ¿Quiere iniciar sesión?") # Impresión de un mensaje.
        print(" 2-. ¿Desea regresar al menú de acceso?") # Impresión de un mensaje.

        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1" if self.inicio_sesion_exitoso == None: # En caso de que haya ingresado el número 1:
                self.iniciar_sesion() # Accederá a la sección para iniciar sesión.
            case "1" if self.inicio_sesion_exitoso != None:
                print()
                self.proceso_inicio_sesion() 
            case "2": # En caso de que haya ingresado el número 2:
                self.menu_acceso()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_post_crear_cuenta()

    
    def enviar_codigo_verificacion(self):
        self.codigo_verificacion = f"{random.randrange(1000000):06d}"

        mensaje_codigo_verificacion = EmailMessage()
        mensaje_codigo_verificacion["From"] = dc.correo_remitente
        mensaje_codigo_verificacion["To"] = self.correo_electronico_registro
        mensaje_codigo_verificacion["Subject"] = f"PedalRide Rentals - Código de Verificación de Cuenta: {self.codigo_verificacion}"

        cuerpo_texto_plano = """
        PedalRide Rentals

        
        Verifique su cuenta
        
        Ingrese el siguiente código para verificar su cuenta:

        {}

        Este código es válido durante la ejecución del programa.
        """

        mensaje_codigo_verificacion.set_content(cuerpo_texto_plano.format(self.codigo_verificacion))

        cuerpo_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital@0;1&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: "Montserrat", sans-serif;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                    color: #313030;
                }}

                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                }}

                .header {{
                    background-color: #004AAD;
                    color: white;
                    text-align: center;
                    padding: 40px;
                    font-size: 30px;
                    font-weight: bold;
                }}

                .divider {{
                    border-top: 2px solid #dbdbdb;
                    margin: 20px 0;
                }}

                .code {{
                    text-align: center;
                    font-size: 36px;
                    margin: 20px 0;
                    padding: 3px;
                    background-color: #f2f2f2;
                    font-weight: bold;
                    border-radius: 5px;
                    display: block;
                    max-width: 200px;
                    margin: 20px auto;
                }}

                h3 {{
                    font-size: 25px;
                    text-align: center;
                    margin: 20px 0;
                }}

                p {{
                    text-align: justify;
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    PedalRide Rentals
                </div>
                
                <h3>Verifique su cuenta</h3>
                
                <div class="divider"></div>

                <p>
                    Ingrese el siguiente código para verificar su cuenta:
                </p>

                <div class="code">
                    {}
                </div>

                <p>
                    Este código es válido durante la ejecución del programa.
                </p>
            </div>
        </body>
        """

        mensaje_codigo_verificacion.add_alternative(cuerpo_html.format(self.codigo_verificacion), subtype = "html")

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:
            smtp.login(dc.correo_remitente, dc.contraseña_correo)
            smtp.send_message(mensaje_codigo_verificacion)

        if self.intento_envio_codigo_verificacion:
            print("\nSe ha enviado un nuevo código de verificación.\n")
            self.intento_envio_codigo_verificacion = None


    def crear_cuenta(self): # Función que permite al usuario crear una cuenta.
        self.limpiar_terminal()
        self.inicio_sesion_exitoso = None
        print("Sección: Crear cuenta.") # Impresión de un mensaje.
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
            self.correo_electronico_registrado = None
            self.correo_electronico_registro = input(" - Correo electrónico: > ") # Se solicita al usuario ingresar un correo electrónico.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del correo electrónico.
            self.correo_electronico_registro = self.correo_electronico_registro.strip()
            try: # Se intenta validar el correo electrónico.
                # Se valida el correo electrónico y se almacena en su formato normalizado.
                self.correo_electronico_registro = validate_email(self.correo_electronico_registro).email
                if self.correo_electronico_registro not in list(self.df["Correo Electrónico"]):
                    parametros = {"autocorrect": False}
                    try:
                        respuesta = requests.get(f"https://emailvalidation.abstractapi.com/v1/?api_key=e06fb4dd03594ddea485b27d1ade4cc1&email={self.correo_electronico_registro}", params = parametros)
                        if respuesta.json()["deliverability"] == "DELIVERABLE":
                            print()
                            break
                        print("El correo electrónico ingresado no es válido. Inténtelo de nuevo.\n")
                    except:
                        self.problema_verificacion_correo = True
                        print("Hubo un problema de nuestro lado. Lamentamos las molestias y esperamos que el inconveniente se solucione más tarde.")
                        break

                else:
                    print("El correo electrónico ingresado ya está registrado.\n") # Impresión de un mensaje.
                    self.correo_electronico_registrado = True
                    while True:
                        print("- Seleccione una de las siguientes opciones con base en su número: \n")
                        print(" 1-. Iniciar sesión.")
                        print(" 2-. Ingresar otro correo.")
                        opcion_usuario = input("\n> ")
                        if opcion_usuario == "1" or opcion_usuario == "2":
                            break
                        print("La opción ingresada no es válida. Inténtelo de nuevo.\n")

                    if opcion_usuario == "1":
                        break
                    print()                
            except EmailNotValidError: # Si no es válido el correo electrónico, ocurre un error.
                print("El formato del correo electrónico ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        if not self.problema_verificacion_correo:
            if not self.correo_electronico_registrado:
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
                    if re.match(regex, contraseña_usuario) and contraseña_usuario != self.correo_electronico_registro: #Si la contraseña cumple con las condiciones mencionadas, entonces:
                        break # Termina el ciclo.
                    print("La contraseña ingresada no cumple con las especificaciones mencionadas. Inténtelo de nuevo.\n") # Impresión de un mensaje.

                self.enviar_codigo_verificacion()
                print(f"\nPara terminar de crear su cuenta, deberá ingresar un código de 6 dígitos con el fin de verificarla. Este código se ha enviado a {self.correo_electronico_registro}.\n")
                while True:
                    print("- Seleccione una de las siguientes opciones con base en su número:\n")
                    print(" 1-. Ingresar el código de verificación.")
                    print(" 2-. Enviar otro código si no ha recibido el correo electrónico.")
                    opcion_usuario = input("\n> ")
                    if opcion_usuario == "1":
                        break
                    elif opcion_usuario == "2":
                        self.intento_envio_codigo_verificacion = True
                        self.enviar_codigo_verificacion()
                    else:
                        print("La opción ingresada no es válida. Inténtelo de nuevo.\n")     
                    
                    if opcion_usuario == "1":
                        break

                while True:
                    codigo_verificacion_usuario = input((f"\n - Ingrese el código para verificar su cuenta: > "))
                    if codigo_verificacion_usuario == self.codigo_verificacion:
                        break
                    print("El código de verificación ingresado no es válido. Inténtelo de nuevo.")

                # Almacenar la información del usuario registrado en un diccionario para su posterior carga en el archivo csv de los usuarios.
                informacion_usuario = {
                    "Nombre(s)": [nombre_usuario], # Nombre(s).
                    "Primer Apellido": [primer_apellido_usuario], # Primer apellido.
                    "Segundo Apellido": [segundo_apellido_usuario], # Segundo apellido.
                    "Número de Teléfono": [numero_telefono_usuario], # Número de teléfono.
                    "Correo Electrónico": [self.correo_electronico_registro], # Correo electrónico.
                    "Contraseña": [contraseña_usuario] # Contraseña.
                    }
                
                df_informacion_usuario = pd.DataFrame(informacion_usuario, dtype = str) # Convertir el diccionario con la información del usuario registrado a un dataframe.
                # Se crea un nuevo dataframe concatenando el dataframe que contiene la información del usuario registrado con el dataframe del csv de los usuarios.
                df_modificado = pd.concat([self.df, df_informacion_usuario], ignore_index = True) 
                df_modificado.reset_index() # Se resetean los index del nuevo dataframe.
                df_modificado.to_csv("usuarios.csv", index = None) # Se guarda el nuevo dataframe en el archivo csv de los usuarios (se sobrescribe el contenido).
                self.df = pd.read_csv("usuarios.csv", dtype = str) # Se vuelve a leer el contenido del archivo csv de los usuarios.

                print("\nSu cuenta ha sido creada exitosamente.\n") # Impresión de un mensaje.

                self.opciones_post_crear_cuenta() # Se muestran las opciones que puede elegir el usuario después de haber creado su cuenta.
            else:
                self.iniciar_sesion()
        

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
                    self.apellidos = f"{self.primer_apellido_usuario} {self.segundo_apellido_usuario}"
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
        self.limpiar_terminal()
        print("Sección: Iniciar sesión.")
        self.proceso_inicio_sesion()


    def opciones_menu_inicio(self): # Función que muestra las opciones del menú de acceso a fin de que el usuario elija una.
        print("- Seleccione una de las siguientes opciones con base en su número:\n") # Impresión de un mensaje.
        print(" 1-. Mi perfil.") # Impresión de un mensaje.
        print(" 2-. Mis reservaciones.") # Impresión de un mensaje.
        print(" 3-. Hacer una reservación.") # Impresión de un mensaje.
        print(" 4-. Cerrar sesión.") # Impresión de un mensaje.
        print(" 5-. Salir del sistema.") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.mi_perfil()
            case "2": # En caso de que haya ingresado el número 2:
                self.mis_reservaciones()
            case "3":
                self.hacer_reservaciones()
            case "4":
                self.nombre_usuario = None
                self.primer_apellido_usuario = None
                self.segundo_apellido_usuario = None
                self.apellidos = None
                self.numero_telefono_usuario = None
                self.correo_electronico_usuario = None
                self.contraseña_usuario = None
                self.menu_acceso()                
            case "5":
                self.limpiar_terminal()
                print("Ha abandonado el sistema.\n")
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_menu_inicio()


    def menu_inicio(self): # Función que corresponde al menú de inicio.
        self.limpiar_terminal()
        self.obtener_fecha_hora()
        print(f"| Usuario: {self.nombre_usuario} {self.apellidos} |")
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
                self.opcion_mi_perfil()


    def mi_perfil(self):
        self.limpiar_terminal()
        print(f"| Usuario: {self.nombre_usuario} {self.apellidos} |")
        print("\nSección: Mi perfil.") # Impresión de un mensaje.
        print("- Información personal:\n")
        print(f" - Nombre: {self.nombre_usuario}")
        print(f" - Primer apellido: {self.primer_apellido_usuario}")
        print(f" - Segundo apellido: {self.segundo_apellido_usuario}")
        print(f" - Número de teléfono: {self.numero_telefono_usuario}")
        print(f" - Correo electrónico: {self.correo_electronico_usuario}")
        print(f" - Contraseña: {self.contraseña_usuario}\n")
        self.opcion_mi_perfil()


    def opciones_cancelar_reservaciones(self):
        if self.numeros_reservaciones_posible_cancelacion or (not self.numeros_reservaciones_posible_cancelacion and self.reservaciones_a_cancelar == None):
            print("- Seleccione una de las siguientes opciones con base en su número:\n")
            if self.numeros_reservaciones_posible_cancelacion:
                print(" 1-. Cancelar otra reservación.")
                print(" 2-. Ver sus reservaciones confirmadas.")
                print(" 3-. Volver al menú de inicio.")
            elif not self.numeros_reservaciones_posible_cancelacion and self.reservaciones_a_cancelar == None:
                print(" 1-. Ver sus reservaciones confirmadas.")
                print(" 2-. Volver al menú de inicio.")
        else:
            print("- Seleccione la opción con base en su número:\n")
            print(" 1-. Volver al menú de inicio.")
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1" if self.numeros_reservaciones_posible_cancelacion: # En caso de que haya ingresado el número 1:
                self.cancelar_reservaciones()
            case "1" if not self.numeros_reservaciones_posible_cancelacion and self.reservaciones_a_cancelar == None:
                self.mis_reservaciones()
            case "1" if self.reservaciones_a_cancelar == False:
                self.menu_inicio()
            case "2" if self.numeros_reservaciones_posible_cancelacion: # En caso de que haya ingresado el número 2:
                self.mis_reservaciones()
            case "2" if not self.numeros_reservaciones_posible_cancelacion and self.reservaciones_a_cancelar == None:
                self.menu_inicio()
            case "3" if self.numeros_reservaciones_posible_cancelacion:
                self.menu_inicio()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_cancelar_reservaciones()


    def enviar_correo_cancelacion(self):
        variables_mensaje_cancelacion = [self.nombre_usuario, self.numero_reservacion_cancelar]

        mensaje_cancelacion = EmailMessage()
        mensaje_cancelacion["From"] = dc.correo_remitente
        mensaje_cancelacion["To"] = self.correo_electronico_usuario
        mensaje_cancelacion["Subject"] = f"PedalRide Rentals - Cancelación de Reservación de Bicicleta: N.º {self.numero_reservacion_cancelar}"

        cuerpo_texto_plano = """
        PedalRide Rentals

        
        Estimado(a) {}:

        Le informamos que su reservación con número {} ha sido cancelada exitosamente.
        Se le reembolsará el monto total pagado en las próximas 24 horas a su método de pago original.
        Agradecemos su comprensión y esperamos poder atenderle en otra ocasión.

        
        ¿Tiene dudas?
        Contáctenos a través de nuestro correo: pedalriderentals@gmail.com
        """

        mensaje_cancelacion.set_content(cuerpo_texto_plano.format(*variables_mensaje_cancelacion))

        cuerpo_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital@0;1&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: "Montserrat", sans-serif;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                    color: #313030;
                }}

                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                }}

                .header {{
                    background-color: #004AAD;
                    color: white;
                    text-align: center;
                    padding: 40px;
                    font-size: 40px;
                    font-weight: bold;
                }}

                .divider {{
                    border-top: 2px solid #dbdbdb;
                    margin: 20px 0;
                }}

                .help-text {{
                    text-align: center;
                    font-size: 18px;
                    margin: 10px 0;
                    color: #505050;
                }}

                .contact-text {{
                    text-align: center;
                    font-size: 16px;
                    color: #505050;
                }}

                .contact-link a {{
                    color: #007BFF;
                    text-decoration: none;
                }}

                h3 {{
                    font-size: 25px;
                    text-align: center;
                    margin: 20px 0;
                }}

                p {{
                    text-align: justify;
                    font-size: 18px;
                }}

                .bold {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    PedalRide Rentals
                </div>
                
                <h3>Estimado(a) {}:</h3>
                
                <p>
                    Le informamos que su reservación con número <span class="bold">{}</span> ha sido cancelada exitosamente.<br>Se le reembolsará el monto total pagado en las próximas 24 horas a su método de pago original.<br>
                    Agradecemos su comprensión y esperamos poder atenderle en otra ocasión.
                </p>
            
                <div class="divider"></div>
            
                <div class="help-text">
                    ¿Tiene dudas?
                </div>
                <div class="contact-text">
                    Contáctenos a través de nuestro correo: <a href="mailto:pedalriderentals@gmail.com">pedalriderentals@gmail.com</a>
                </div>
            </div>
        </body>
        """

        mensaje_cancelacion.add_alternative(cuerpo_html.format(*variables_mensaje_cancelacion), subtype = "html")

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:
            smtp.login(dc.correo_remitente, dc.contraseña_correo)
            smtp.send_message(mensaje_cancelacion)

        print("Se ha enviado un mensaje de cancelación al correo electrónico asociado a su cuenta.\n")


    def checar_reservaciones_posible_cancelacion(self):
        self.obtener_fecha_hora()
        self.numeros_reservaciones_posible_cancelacion = [reservacion_confirmada[0] for reservacion_confirmada in self.reservaciones_confirmadas if self.fecha_hora_actual_datetime <= dt.datetime.strptime(f"{reservacion_confirmada[4]} {reservacion_confirmada[5]}", "%d/%m/%Y %H:%M") - dt.timedelta(hours = 24)]


    def cancelar_reservaciones(self):
        self.reservaciones_a_cancelar = None
        self.checar_reservaciones_confirmadas()
        self.checar_reservaciones_posible_cancelacion()
        if self.numeros_reservaciones_posible_cancelacion:
            print("\nLas siguientes reservaciones pueden ser canceladas:\n" if len(self.numeros_reservaciones_posible_cancelacion) > 1 else "\nLa siguiente reservación puede ser cancelada:\n")
            print("| N.º de Reservación |")
            for numero_reservacion in self.numeros_reservaciones_posible_cancelacion:
                print(f"{numero_reservacion:^22}")

            while True:
                try:
                    self.numero_reservacion_cancelar = int(input("\n- Ingrese el número de la reservación que desee cancelar: > "))
                    if self.numero_reservacion_cancelar in self.numeros_reservaciones_posible_cancelacion:
                        break
                    print("No se ha encontrado una reservación que se pueda cancelar con ese número asignado. Inténtelo de nuevo.")
                except ValueError:
                    print("El número de reservación ingresado no es válido. Inténtelo de nuevo.")

            self.numeros_reservacion_disponibles.add(self.numero_reservacion_cancelar)
            index_reservacion = self.df_reservaciones.loc[self.df_reservaciones["Número de Reservación"] == self.numero_reservacion_cancelar].index
            self.df_reservaciones.drop(index_reservacion, inplace = True)
            self.df_reservaciones.to_csv("reservaciones.csv", index = None)
            self.df_reservaciones = pd.read_csv("reservaciones.csv", dtype = {
                "Número de Reservación": int,
                "Nombre(s)": str,
                "Apellidos": str,
                "Correo Electrónico": str,
                "Fecha de la Reservación": str,
                "Hora de Inicio": str,
                "Hora de Término": str,
                "Número de Bicicleta": str,
                "Tipo de Bicicleta": str,
                "Costo": str,
                "Número de Teléfono": str
            })

            print("\nLa reservación se ha cancelado.")
            
            self.enviar_correo_cancelacion()

            self.checar_reservaciones_confirmadas()
            self.checar_reservaciones_posible_cancelacion()
        else:
            self.reservaciones_a_cancelar = False
            print("\nNinguna reservación puede ser cancelada.\n")
        self.opciones_cancelar_reservaciones()
        

    def opciones_mis_reservaciones(self):
        print("- Seleccione una de las siguientes opciones con base en su número:\n") # Impresión de un mensaje.
        print(" 1-. Hacer una reservación.") # Impresión de un mensaje.
        if self.reservaciones_confirmadas:
            print(" 2-. Cancelar una reservación.") # Impresión de un mensaje.
            print(" 3-. Volver al menú de inicio.") # Impresión de un mensaje.
        else:
            print(" 2-. Volver al menú de inicio.")
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.hacer_reservaciones()
            case "2" if self.reservaciones_confirmadas: # En caso de que haya ingresado el número 2:
                self.cancelar_reservaciones()
            case "2" if not self.reservaciones_confirmadas:
                self.menu_inicio()
            case "3" if self.reservaciones_confirmadas:
                self.menu_inicio()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_mis_reservaciones()


    def checar_reservaciones_confirmadas(self):
        reservaciones = self.df_reservaciones.loc[self.df_reservaciones["Correo Electrónico"] == self.correo_electronico_usuario].to_numpy().tolist()
        reservaciones.sort(key = lambda elemento: (dt.datetime.strptime(elemento[4], "%d/%m/%Y").date(), dt.datetime.strptime(elemento[5], "%H:%M").time()))
        self.reservaciones_confirmadas = [reservacion for reservacion in reservaciones if self.fecha_hora_actual_datetime < dt.datetime.strptime(f"{reservacion[4]} {reservacion[5]}", "%d/%m/%Y %H:%M")]


    def proceso_mostrar_reservaciones(self):
        self.checar_reservaciones_confirmadas()
        if self.reservaciones_confirmadas:
            print("| N.º de Reservación |     Fecha     |     Horario     |     Tipo de Bicicleta     | N.º de Bicicleta |   Costo   |")
            for reservacion_confirmada in self.reservaciones_confirmadas:
                print(f"{reservacion_confirmada[0]:^22}{reservacion_confirmada[4]:^15}{f"{reservacion_confirmada[5]} - {reservacion_confirmada[6]}":^20}{f"   {reservacion_confirmada[8]}":<25}{reservacion_confirmada[7]:^24}{reservacion_confirmada[9]:^5}")
        else:
            print(" - No tiene ninguna reservación confirmada.")
        print()


    def mis_reservaciones(self):
        self.limpiar_terminal()
        self.obtener_fecha_hora()
        print(f"| Usuario: {self.nombre_usuario} {self.apellidos} |")
        print("\nSección: Mis reservaciones.")
        print("- Reservaciones confirmadas:\n")
        self.proceso_mostrar_reservaciones()
        self.opciones_mis_reservaciones()


    def opciones_hacer_reservaciones(self):
        print("- Seleccione una de las siguientes opciones con base en su número: \n") # Impresión de un mensaje.
        if self.horario_trabajo != None or self.bicicletas_disponibles == False or self.confirmacion_reservacion_usuario == False:
            if self.horario_trabajo != None or self.bicicletas_disponibles == False :
                print(" 1-. Cambiar la fecha y horario de la reservación.") # Impresión de un mensaje.
            elif self.confirmacion_reservacion_usuario == False:   
                print(" 1-. Hacer una reservación.") # Impresión de un mensaje.
            print(" 2-. Volver al menú de inicio.") # Impresión de un mensaje.        
        else:
            print(" 1-. Hacer otra reservación.")
            print(" 2-. Ver sus reservaciones confirmadas.")
            print(" 3-. Volver al menú de inicio.") # Impresión de un mensaje.
        opcion_usuario = input("\n> ") # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case "1": # En caso de que haya ingresado el número 1:
                self.hacer_reservaciones() # Accederá a la sección para iniciar sesión.
            case "2" if self.horario_trabajo != None or self.bicicletas_disponibles == False or self.confirmacion_reservacion_usuario == False: # En caso de que haya ingresado el número 2:
                self.menu_inicio()
            case "2" if self.confirmacion_reservacion_usuario:
                self.mis_reservaciones()
            case "3" if self.confirmacion_reservacion_usuario:
                self.menu_inicio()
            case _:
                print("La opción ingresada no es válida. Inténtelo de nuevo.\n")
                self.opciones_hacer_reservaciones()


    def enviar_correo_confirmacion(self):
        variables_mensaje_confirmacion = [self.nombre_usuario, self.numero_reservacion, self.nombre_usuario, self.fecha_reserva, 
                            self.horario_reserva, self.reserva_bicicleta, self.numero_bicicleta, self.costo_total_reserva]

        mensaje_confirmacion = EmailMessage()
        mensaje_confirmacion["From"] = dc.correo_remitente
        mensaje_confirmacion["To"] = self.correo_electronico_usuario
        mensaje_confirmacion["Subject"] = f"PedalRide Rentals - Confirmación de Reservación de Bicicleta: N.º {self.numero_reservacion}"

        cuerpo_texto_plano = """
        PedalRide Rentals

        
        Hola {}:

        Nos complace confirmar su reservación de bicicleta. A continuación, encontrará los detalles de su reservación:

        Número de Reservación: {}
        Nombre: {}
        Fecha: {}
        Horario: {}
        Tipo de Bicicleta: {}
        Número de Bicicleta: {}
        Costo: {}

        ¡Gracias por reservar con nosotros y esperamos que disfrute su paseo!

        
        ¿Tiene dudas?
        Contáctenos a través de nuestro correo: pedalriderentals@gmail.com
        """

        mensaje_confirmacion.set_content(cuerpo_texto_plano.format(*variables_mensaje_confirmacion))

        cuerpo_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital@0;1&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: "Montserrat", sans-serif;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                    color: #313030;
                }}

                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                }}

                .header {{
                    background-color: #004AAD;
                    color: white;
                    text-align: center;
                    padding: 40px;
                    font-size: 40px;
                    font-weight: bold;
                }}

                .divider {{
                    border-top: 2px solid #dbdbdb;
                    margin: 20px 0;
                }}

                .help-text {{
                    text-align: center;
                    font-size: 18px;
                    margin: 10px 0;
                    color: #505050;
                }}

                .contact-text {{
                    text-align: center;
                    font-size: 16px;
                    color: #505050;
                }}

                .contact-link a {{
                    color: #007BFF;
                    text-decoration: none;
                }}

                h3 {{
                    font-size: 25px;
                    text-align: center;
                    margin: 20px 0;
                }}

                p {{
                    text-align: justify;
                    font-size: 18px;
                }}

                .bold {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    PedalRide Rentals
                </div>
                
                <h3>Hola {}:</h3>
                
                <p>
                    Nos complace confirmar su reservación de bicicleta. A continuación, encontrará los detalles de su reservación:<br><br>
                    <span class="bold">Número de Reservación: </span>{}<br>
                    <span class="bold">Nombre: </span>{}<br>
                    <span class="bold">Fecha: </span>{}<br>
                    <span class="bold">Horario: </span>{}<br>
                    <span class="bold">Tipo de Bicicleta: </span>{}<br>
                    <span class="bold">Número de Bicicleta: </span>{}<br>
                    <span class="bold">Costo: </span>{}<br><br>
                    ¡Gracias por reservar con nosotros y esperamos que disfrute su paseo!
                </p>
            
                <div class="divider"></div>
            
                <div class="help-text">
                    ¿Tiene dudas?
                </div>
                <div class="contact-text">
                    Contáctenos a través de nuestro correo: <a href="mailto:pedalriderentals@gmail.com">pedalriderentals@gmail.com</a>
                </div>
            </div>
        </body>
        """

        mensaje_confirmacion.add_alternative(cuerpo_html.format(*variables_mensaje_confirmacion), subtype = "html")

        contexto = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = contexto) as smtp:
            smtp.login(dc.correo_remitente, dc.contraseña_correo)
            smtp.send_message(mensaje_confirmacion)

        print("Se ha enviado un mensaje de confirmación, que contiene todos los detalles de su reservación, al correo electrónico asociado a su cuenta.\n")


    def proceso_hacer_reservaciones(self):
        self.horario_trabajo = None
        self.bicicletas_disponibles = None
        self.confirmacion_reservacion_usuario = None

        self.obtener_fecha_hora()

        dia_actual = self.fecha_hora_actual_datetime.day
        año_actual = self.fecha_hora_actual_datetime.year
        horas_actual = self.fecha_hora_actual_datetime.hour
        minutos_actual = self.fecha_hora_actual_datetime.minute

        print("\n- Nuestro horario de trabajo es de las 08:00 a las 20:00.")
        print("- Las reservaciones se deben realizar para el año en curso, y con al menos una hora de anticipación.")
        print("- Las reservaciones se realizan en bloques por hora, y pueden ser de más de una hora.\n")

        while True:
            self.fecha_reserva = input(" - Ingrese la fecha de la reservación (Formato: DD/MM/AAAA): > ")
            formato_fecha = r"^\d{2}/\d{2}/\d{4}$"
            if re.match(formato_fecha, self.fecha_reserva):
                try:
                    fecha_reserva_datetime = dt.datetime.strptime(self.fecha_reserva, "%d/%m/%Y").date()
                    dia_reserva = fecha_reserva_datetime.day
                    año_reserva = fecha_reserva_datetime.year
                    if año_reserva == año_actual:
                        if dia_reserva >= dia_actual:
                            print()
                            break
                        else:
                            print("El día de la reservación ingresado no es válido. Inténtelo de nuevo.\n")
                    else:
                        print("La fecha de la reservación ingresada no cumple con el parámetro establecido. Inténtelo de nuevo.\n")
                        print("- Recuerde que las reservaciones se deben realizar para el año en curso.\n")
                except:
                    print("La fecha ingresada no es válida. Inténtelo de nuevo.\n")
            else:
                print("El formato de la fecha ingresada no es válido. Inténtelo de nuevo.\n")

        if fecha_reserva_datetime == self.fecha_hora_actual_datetime.date() and self.fecha_hora_actual_datetime.time() > dt.datetime.strptime("18:00", "%H:%M").time():
            self.horario_trabajo = False
            print("No es posible hacer reservaciones para el día de hoy.\n")
            self.opciones_hacer_reservaciones()

        while True:
            while True:
                hora_inicio_reserva = input(" - Ingrese la hora de inicio de la reservación (Formato de 24 horas: HH:MM): > ")
                formato_hora = r"^\d{2}:\d{2}$"
                if re.match(formato_hora, hora_inicio_reserva):
                    try:
                        hora_inicio_reserva_datetime = dt.datetime.strptime(hora_inicio_reserva, "%H:%M").time()
                        horas_inicio_reserva = hora_inicio_reserva_datetime.hour
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
                        print()
                        break
                    except:
                        print("La hora de término ingresada no es válida. Inténtelo de nuevo.\n")
                else:
                    print("El formato de la hora de término ingresada no es válido. Inténtelo de nuevo.\n")
            
            formato_hora_reservas = r"^\d{2}:00$"
            horas_anticipacion = horas_inicio_reserva - (horas_actual + (minutos_actual / 60))
            
            if re.match(formato_hora_reservas, hora_inicio_reserva) and re.match(formato_hora_reservas, hora_termino_reserva) \
            and horas_inicio_reserva >= 8 and horas_inicio_reserva <= 20 and horas_termino_reserva >= 8 and horas_termino_reserva <=20:
                if fecha_reserva_datetime > self.fecha_hora_actual_datetime.date():
                    if hora_inicio_reserva_datetime < hora_termino_reserva_datetime:
                        break
                    else:
                        print("El horario ingresado no es válido. Inténtelo de nuevo.\n")
                elif hora_inicio_reserva_datetime > self.fecha_hora_actual_datetime.time() and hora_inicio_reserva_datetime < hora_termino_reserva_datetime:
                    if horas_anticipacion >= 1:
                        break
                    else:
                        print("El horario ingresado no es válido. Recuerde que las reservaciones se deben hacer con al menos una hora de anticipación. Inténtelo de nuevo.\n")
                else:
                    print("El horario ingresado no es válido. Inténtelo de nuevo.\n")
            else:
                print("El horario ingresado no cumple con las condiciones establecidas. Inténtelo de nuevo.\n")
                print("Recuerde que:")
                print("- Nuestro horario de trabajo es de las 08:00 a las 20:00.")
                print("- Las reservaciones se deben realizar con al menos una hora de anticipación.")
                print("- Las reservaciones se realizan en bloques por hora, y pueden ser de más de una hora.\n")

        informacion_reservaciones = self.df_reservaciones.to_numpy()
        self.bicicletas_disponibles = False
        
        # Ciclo para verificar si hay bicicletas disponibles
        for tipo_bicicleta in self.bicicletas.values():
            cantidad_bicicletas_disponibles = len(tipo_bicicleta[1])
            h = 0
            while h < len(tipo_bicicleta[1]):
                bicicleta_disponible = True
                l = 0
                while l < len(informacion_reservaciones) and bicicleta_disponible:
                    if tipo_bicicleta[1][h] == informacion_reservaciones[l][7]:
                        container_fecha_reserva_datetime = dt.datetime.strptime(informacion_reservaciones[l][4], "%d/%m/%Y").date()
                        if container_fecha_reserva_datetime == fecha_reserva_datetime:
                            container_hora_inicio_datetime = dt.datetime.strptime(informacion_reservaciones[l][5], "%H:%M").time()
                            container_hora_termino_datetime = dt.datetime.strptime(informacion_reservaciones[l][6], "%H:%M").time()
                            if hora_inicio_reserva_datetime < container_hora_termino_datetime and hora_termino_reserva_datetime > container_hora_inicio_datetime:
                                bicicleta_disponible = False
                                cantidad_bicicletas_disponibles -= 1
                    l += 1
                h += 1
            if cantidad_bicicletas_disponibles:
                self.bicicletas_disponibles = True
                break

        # Si hay bicicletas disponibles, entonces se muestran y sigue el proceso de la reservación.
        if self.bicicletas_disponibles:
            print("En este momento, se muestra la lista de bicicletas disponibles en la fecha y horario elegidos:\n")
            print("      |     Tipo de Bicicleta     |       Descripción       | Bicicletas Disponibles |   Costo por Hora   |")

        # Ciclo para mostrar las bicicletas disponibles
            
            opcion_por_tipo_bicicleta = 0
            bicicletas_disponibles = dict()

            for tipo_bicicleta, informacion_tipo_bicicleta in self.bicicletas.items():
                cantidad_bicicletas_disponibles = len(informacion_tipo_bicicleta[1])
                bicicletas_disponibles_por_tipo = list()
                a = 0
                while a < len(informacion_tipo_bicicleta[1]):
                    bicicleta_disponible = True
                    b = 0
                    while b < len(informacion_reservaciones) and bicicleta_disponible:
                        if informacion_tipo_bicicleta[1][a] == informacion_reservaciones[b][7]:
                            container_fecha_reserva_datetime = dt.datetime.strptime(informacion_reservaciones[b][4], "%d/%m/%Y").date()
                            if container_fecha_reserva_datetime == fecha_reserva_datetime:
                                container_hora_inicio_datetime = dt.datetime.strptime(informacion_reservaciones[b][5], "%H:%M").time()
                                container_hora_termino_datetime = dt.datetime.strptime(informacion_reservaciones[b][6], "%H:%M").time()
                                if hora_inicio_reserva_datetime < container_hora_termino_datetime and hora_termino_reserva_datetime > container_hora_inicio_datetime:
                                    bicicleta_disponible = False
                                    cantidad_bicicletas_disponibles -= 1
                        b += 1
                    if bicicleta_disponible:
                        bicicletas_disponibles_por_tipo.append(informacion_tipo_bicicleta[1][a])
                    a += 1
                if cantidad_bicicletas_disponibles:
                    opcion_por_tipo_bicicleta += 1
                    bicicletas_disponibles[str(opcion_por_tipo_bicicleta)] = {tipo_bicicleta: bicicletas_disponibles_por_tipo}
                    print(f"\t {f"{opcion_por_tipo_bicicleta}-. {tipo_bicicleta}":<25}{f"     {informacion_tipo_bicicleta[0]}":<29}{cantidad_bicicletas_disponibles:^21}{f"${informacion_tipo_bicicleta[2]}":^24}")

            while True:
                opcion_usuario = input("\n - Elija la bicicleta a rentar con base en su número de tipo: > ")
                if opcion_usuario in bicicletas_disponibles:
                    print()
                    break
                print("El número de tipo de bicicleta ingresado no es válido. Inténtelo de nuevo.")
            
            self.horario_reserva = f"{hora_inicio_reserva} - {hora_termino_reserva}"
            self.reserva_bicicleta = [*bicicletas_disponibles[opcion_usuario]][0]
            self.costo_total_reserva = f"${(horas_termino_reserva - horas_inicio_reserva) * self.bicicletas[self.reserva_bicicleta][2]}"

            print("A continuación, se muestran los detalles de su reservación, incluyendo el costo total de la misma:\n")

            print("|      Nombre      |      Apellidos      |     Fecha     |     Horario     |     Tipo de Bicicleta     |   Costo   |")
            print(f" {self.nombre_usuario:^20}{self.apellidos:^20} {self.fecha_reserva:^14}{self.horario_reserva:^21}{self.reserva_bicicleta:^25}{self.costo_total_reserva:^15}\n")

            self.confirmacion_reservacion_usuario = False

            while True:
                respuesta_usuario_precio = input(" - ¿Desea confirmar la reservación (Sí/No)? > ")
                respuesta_usuario_precio = respuesta_usuario_precio.strip().lower()
                if respuesta_usuario_precio == "sí" or respuesta_usuario_precio == "si" or respuesta_usuario_precio == "no":
                    print()
                    break
                print("La respuesta ingresada no es válida. Inténtelo de nuevo.\n")

            if respuesta_usuario_precio == "sí" or respuesta_usuario_precio == "si":
                self.confirmacion_reservacion_usuario = True

                self.numero_reservacion = random.choice(list(self.numeros_reservacion_disponibles))
                self.numeros_reservacion_disponibles.remove(self.numero_reservacion)

                self.numero_bicicleta = random.choice(bicicletas_disponibles[opcion_usuario][self.reserva_bicicleta])

                informacion_reservacion = {
                    "Número de Reservación": [self.numero_reservacion],
                    "Nombre(s)": [self.nombre_usuario],
                    "Apellidos": [self.apellidos],
                    "Correo Electrónico": [self.correo_electronico_usuario],
                    "Fecha de la Reservación": [self.fecha_reserva],
                    "Hora de Inicio": [hora_inicio_reserva],
                    "Hora de Término": [hora_termino_reserva],
                    "Número de Bicicleta": [self.numero_bicicleta],
                    "Tipo de Bicicleta": [self.reserva_bicicleta],
                    "Costo": [self.costo_total_reserva],
                    "Número de Teléfono": [self.numero_telefono_usuario]
                    }
                
                df_informacion_reservacion = pd.DataFrame(informacion_reservacion, dtype = str)
                df_reservacion_modificado = pd.concat([self.df_reservaciones, df_informacion_reservacion])
                df_reservacion_modificado.reset_index()
                df_reservacion_modificado.to_csv("reservaciones.csv", index = None)
                self.df_reservaciones = pd.read_csv("reservaciones.csv", dtype = {
                    "Número de Reservación": int,
                    "Nombre(s)": str,
                    "Apellidos": str,
                    "Correo Electrónico": str,
                    "Fecha de la Reservación": str,
                    "Hora de Inicio": str,
                    "Hora de Término": str,
                    "Número de Bicicleta": str,
                    "Tipo de Bicicleta": str,
                    "Costo": str,
                    "Número de Teléfono": str
                })

                print("Su reservación se ha realizado con éxito.")
                print("Seguidamente, se muestra el número de la reservación, así como el número de bicicleta asignado:\n")

                print("\t\t\t   | N.º de Reservación | N.º de Bicicleta |")
                print(f"\t\t\t   {self.numero_reservacion:^23}\t {self.numero_bicicleta}\n") 

                self.enviar_correo_confirmacion()
        else:
            print("No hay bicicletas disponibles para la fecha y horario elegidos.\n")
        self.opciones_hacer_reservaciones()


    def hacer_reservaciones(self):
        self.limpiar_terminal()
        print(f"| Usuario: {self.nombre_usuario} {self.apellidos} |")
        print("\nSección: Hacer una reservación.")
        self.proceso_hacer_reservaciones()

        
def main(): # Función main.
    df = pd.read_csv("usuarios.csv", dtype = str) # Lectura del contenido del archivo csv de los usuarios por medio de la creación de un dataframe.
    df_reservaciones = pd.read_csv("reservaciones.csv", dtype = {
        "Número de Reservación": int,
        "Nombre(s)": str,
        "Apellidos": str,
        "Correo Electrónico": str,
        "Fecha de la Reservación": str,
        "Hora de Inicio": str,
        "Hora de Término": str,
        "Número de Bicicleta": str,
        "Tipo de Bicicleta": str,
        "Costo": str,
        "Número de Teléfono": str
    })

    PedalRide_Rentals(df, df_reservaciones) # Se crea una instancia de la clase (se pasa como argumento el dataframe del archivo csv de los usuarios).

if __name__ == "__main__": # Si el programa es ejecutado desde el archivo principal, entonces:
    main() # Se ejecuta el código.