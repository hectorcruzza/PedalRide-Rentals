import pandas as pd # Importación de librería para la carga de información del sistema
from email_validator import validate_email, EmailNotValidError # Importación de librería para la verificación de correos electrónicos
import re # Importación de librería para la creación de regular expressions

class PedalRide_Rentals: # Creación de la clase.
    def __init__(self, df: pd.DataFrame): # Función de inicialización.
        self.df = df #Cargar la información de los usuarios
        self.bicicletas = [] # Inicialización de la lista de bicicletas a alquilar.
        print("¡Bienvenido(a) al sistema de reservaciones para el servicio de alquiler de bicicletas!") # Impresión de un mensaje.
        self.menu_acceso() # Se llama a la función del menú de acceso.


    def opciones_menu_acceso(self): # Función que muestra las opciones del menú de acceso a fin de que el usuario elija una.
        print("- Seleccione una de las siguientes opciones: \n") # Impresión de un mensaje.
        print(" 1-. Iniciar sesión.") # Impresión de un mensaje.
        print(" 2-. Crear cuenta.") # Impresión de un mensaje.
        print(" 3-. Salir del sistema.") # Impresión de un mensaje.
        opcion_usuario = int(input()) # Pedir al usuario que elija una opción.
        match opcion_usuario: # Un switch case que evalua el input del usuario.
            case 1: # En caso de que haya ingresado el número 1:
                self.iniciar_sesion() # Accederá a la sección para iniciar sesión.
            case 2: # En caso de que haya ingresado el número 2:
                self.crear_cuenta() # Accederá a la sección para crear una cuenta.


    def menu_acceso(self): # Función que corresponde al menú de acceso.
        print("Sección: Menú de acceso.") # Impresión de un mensaje.
        self.opciones_menu_acceso() # Se llama a la función correspondiente para mostrar al usuario las opciones a elegir en el menú de acceso.


    def crear_cuenta(self): # Función que permite al usuario crear una cuenta.
        print("\nSección: Crear cuenta.") # Impresión de un mensaje.
        print("- Ingrese sus datos personales en los campos correspondientes:\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si el/los nombre(s) ingresado(s) por el usuario es válido.
            nombre_valido = True # Valor lógico referente a si el nombre ingresado es válido.
            self.nombre_usuario = input(" - Nombre(s): ") # Se solicita al usuario ingresar su(s) nombre(s).
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del nombre, y se convierten todos los caracteres a minúsculas.
            # La letra inicial de cada nombre se convierte en mayúscula.
            self.nombre_usuario = " ".join([nombre.capitalize() for nombre in self.nombre_usuario.strip().lower().split()])
            # Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un nombre válido.
            nombre_valido = all(caracter.isalpha() or caracter.isspace() for caracter in self.nombre_usuario)
            # Si el valor lógico referente a si el nombre ingresado es válido es verdadero y la cantidad de caracteres del nombre es mayor o igual a dos, entonces:
            if len(self.nombre_usuario) >= 2 and nombre_valido:
                break # Termina el ciclo.
            print("- El/los nombre(s) ingresado(s) no es/son válido(s). Inténtelo de nuevo.\n") # Impresión de un mensaje.

        print()

        while True: # Ciclo infinito para evaluar si el primer apellido ingresado por el usuario es válido.
            primer_apellido_valido = True # Valor lógico referente a si el primer apellido ingresado es válido.
            self.primer_apellido_usuario = input(" - Primer apellido: ") # Se solicita al usuario ingresar su primer apellido.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del primer apellido, y se convierten todos los caracteres a minúsculas.
            # La letra inicial del primer apellido se convierte en mayúscula.
            self.primer_apellido_usuario = " ".join([apellido.capitalize() for apellido in self.primer_apellido_usuario.strip().lower().split()])
            # Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un primer apellido válido.
            primer_apellido_valido = all(caracter.isalpha() or caracter.isspace() for caracter in self.primer_apellido_usuario)
            # Si la cantidad de caracteres del primer apellido es mayor o igual a dos y el valor lógico referente a si el primer apellido ingresado es válido es verdadero, entonces:
            if len(self.primer_apellido_usuario) >= 2 and primer_apellido_valido:
                break # Termina el ciclo.
            print("- El primer apellido ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.
        
        print()

        while True: # Ciclo infinito para evaluar si el segundo apellido ingresado por el usuario es válido.
            segundo_apellido_valido = True # Valor lógico referente a si el segundo apellido ingresado es válido.
            self.segundo_apellido_usuario = input(" - Segundo apellido: ") # Se solicita al usuario ingresar su segundo apellido.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del segundo apellido, y se convierten todos los caracteres a minúsculas.
            # La letra inicial del segundo apellido se convierte en mayúscula.
            self.segundo_apellido_usuario = " ".join([apellido.capitalize() for apellido in self.segundo_apellido_usuario.strip().lower().split()])
            # Se revisa si todos los caracteres son una letra del alfabeto o un espacio. Si no se cumple esa condición, entonces no es un segundo apellido válido.
            segundo_apellido_valido = all(caracter.isalpha() or caracter.isspace() for caracter in self.segundo_apellido_usuario)
            # Si la cantidad de caracteres del segundo apellido es mayor o igual a dos y el valor lógico referente a si el segundo apellido ingresado es válido es verdadero, entonces:
            if len(self.segundo_apellido_usuario) >= 2 and segundo_apellido_valido:
                break # Termina el ciclo.
            print("- El segundo apellido ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        print()

        # Pendiente cambiar lo del número.
        while True: # Ciclo infinito para evaluar si el número de teléfono ingresado por el usuario es válido.
            caracteres_validos = ["+", "-", "(", ")"] # Lista de caracteres que puede tener un número de teléfono.
            numero_telefono_valido = True # Valor lógico referente a si el número de teléfono ingresado es válido.
            self.numero_telefono_usuario = input(" - Número de teléfono: ") # Se solicita al usuario ingresar un número de teléfono.
            # Se remueven los espacios en blanco encontrados al inicio, al final y dentro del string del número de teléfono.
            self.numero_telefono_usuario = self.numero_telefono_usuario.strip().replace(" ", "")
            # Se revisa si todos los caracteres son dígitos o si están presentes en la lista de caracteres válidos. Si no se cumple esa condición, entonces no es un número de teléfono válido.
            numero_telefono_valido = all(caracter.isdigit() or caracter in caracteres_validos for caracter in self.numero_telefono_usuario)
            # Si la cantidad de caracteres del número de teléfono es mayor o igual a 5 y menor o igual a 15, y el valor lógico referente a si el número de teléfono ingresado es válido es verdadero, entonces:
            if (len(self.numero_telefono_usuario) >= 5 and len(self.numero_telefono_usuario) <= 15) and numero_telefono_valido:
                break # Termina el ciclo.
            print("- El número de teléfono ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        print()

        # Pendiente lo del correo para ver si se hace lo del API.
        while True: # Ciclo infinito para evaluar si el correo electrónico ingresado por el usuario es válido.
            self.correo_electronico_usuario = input(" - Correo electrónico: ") # Se solicita al usuario ingresar un correo electrónico.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string del correo electrónico.
            self.correo_electronico_usuario = self.correo_electronico_usuario.strip()

            try: # Se intenta validar el correo electrónico.
                # Se valida el correo electrónico y se almacena en su formato normalizado.
                self.correo_electronico_usuario = validate_email(self.correo_electronico_usuario).email
                # Si el correo electrónico ingresado no está registrado, entonces:
                if self.correo_electronico_usuario not in list(self.df["Correo Electrónico"]):
                    break # Termina el ciclo.
                print("- El correo electrónico ingresado ya está registrado. Ingrese otro.\n") # Impresión de un mensaje.
            except EmailNotValidError: # Si no es válido el correo electrónico, ocurre un error.
                print("- El correo electrónico ingresado no es válido. Inténtelo de nuevo.\n") # Impresión de un mensaje.

        print("\n - Elija una contraseña para su cuenta.\n") # Impresión de un mensaje.

        print(" - La contraseña debe incluir: ") # Impresión de un mensaje.
        print("  - Al menos ocho caracteres.") # Impresión de un mensaje.
        print("  - Al menos una letra.") # Impresión de un mensaje.
        print("  - Al menos una letra mayúscula.") # Impresión de un mensaje.
        print("  - Al menos un número.") # Impresión de un mensaje.
        print("  - Al menos un caracter que no sea una letra ni un número.\n") # Impresión de un mensaje.
        print(" - Asimismo: ") # Impresión de un mensaje.
        print("  - No debe incluir espacios.") # Impresión de un mensaje.
        print("  - No debe incluir letras acentuadas.") # Impresión de un mensaje.
        print("  - No puede ser igual a la dirección de correo electrónico.\n") # Impresión de un mensaje.

        while True: # Ciclo infinito para evaluar si la contraseña ingresada por el usuario es válida.
            self.contraseña_usuario = input(" - Contraseña: ") # Se solicita al usuario ingresar una contraseña.
            # Se remueven los espacios en blanco encontrados al inicio y al final del string de la contraseña.
            self.contraseña_usuario = self.contraseña_usuario.strip()
            regex = r"^(?=.*[a-zA-Z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])(?!.*[áéíóúüñ\s]).{8,}$" # Regular expression para verificar que la contraseña cumpla con las condiciones mencionadas.
            if re.match(regex, self.contraseña_usuario) and self.contraseña_usuario != self.correo_electronico_usuario: #Si la contraseña cumple con las condiciones mencionadas, entonces:
                break # Termina el ciclo.
            print("- La contraseña ingresada no es válida. Inténtelo de nuevo.\n") # Impresión de un mensaje.
            print(" - Recuerda que la contraseña debe incluir: ") # Impresión de un mensaje.
            print("  - Al menos ocho caracteres.") # Impresión de un mensaje.
            print("  - Al menos una letra.") # Impresión de un mensaje.
            print("  - Al menos una letra mayúscula.") # Impresión de un mensaje.
            print("  - Al menos un número.") # Impresión de un mensaje.
            print("  - Al menos un caracter que no sea una letra ni un número.\n") # Impresión de un mensaje.
            print(" - Asimismo: ") # Impresión de un mensaje.
            print("  - No debe tener espacios en blanco.") # Impresión de un mensaje.
            print("  - No debe incluir letras acentuadas, letras con diéresis ni la letra ñ.") # Impresión de un mensaje.
            print("  - No puede ser igual a la dirección de correo electrónico.\n") # Impresión de un mensaje.

        # Almacenar la información del usuario registrado en un diccionario para su posterior carga en el archivo csv de los usuarios.
        informacion_usuario = {
            "Nombre(s)": [self.nombre_usuario], # Nombre(s).
            "Primer Apellido": [self.primer_apellido_usuario], # Primer apellido.
            "Segundo Apellido": [self.segundo_apellido_usuario], # Segundo apellido.
            "Número de Teléfono": [self.numero_telefono_usuario], # Número de teléfono.
            "Correo Electrónico": [self.correo_electronico_usuario], # Correo electrónico.
            "Contraseña": [self.contraseña_usuario] # Contraseña.
            }
        
        df_informacion_usuario = pd.DataFrame(informacion_usuario) # Convertir el diccionario con la información del usuario registrado a un dataframe.
        # Se crea un nuevo dataframe concatenando el dataframe que contiene la información del usuario registrado con el dataframe del csv de los usuarios.
        df_modificado = pd.concat([self.df, df_informacion_usuario], ignore_index = True) 
        df_modificado.reset_index() # Se resetean los index del nuevo dataframe.
        df_modificado.to_csv("usuarios.csv", index = None) # Se guarda el nuevo dataframe en el archivo csv de los usuarios (se sobrescribe el contenido).
        self.df = pd.read_csv("usuarios.csv") # Se vuelve a leer el contenido del archivo csv de los usuarios.

        print("\n- El registro ha sido exitoso.\n") # Impresión de un mensaje.

        self.menu_acceso() # Se llama a la función del menú de acceso.


    def iniciar_sesion(self): # Función que permite al usuario iniciar sesión.
        print("\nSección: Iniciar sesión.")
        print("\n- Ingrese los siguientes datos:\n") # Impresión de un mensaje.
        correo_electronico = input(" - Correo electrónico: ") # Se solicita al usuario ingresar el correo electrónico de su cuenta.
        if correo_electronico in list(self.df["Correo Electrónico"]): # Si el correo electrónico ingresado está registrado, entonces:
            print()
            while True: # Ciclo infinito para evaluar si la contraseña ingresada por el usuario corresponde a la de su cuenta.
                contraseña = input(" - Contraseña: ") # Se solicita al usuario ingresar la contraseña de su cuenta.
                # Si la contraseña ingresada corresponde a la contraseña de su cuenta, entonces:
                if contraseña == self.df.loc[self.df["Correo Electrónico"] == correo_electronico].iloc[0]["Contraseña"]:
                    break # Termina el ciclo.
                print("- La contraseña ingresada es incorrecta. Inténtelo de nuevo.\n") # Impresión de un mensaje.
            self.menu_inicio() # Se llama a la función del menú de inicio.
        else:
            print("- No pudimos encontrar tu cuenta.\n")
            self.opciones_menu_acceso() # Se llama a la función correspondiente para mostrar al usuario las opciones a elegir.
                
    
    def menu_inicio(self): # Función que corresponde al menú de inicio.
        print("\nSección: Menú de inicio.") # Impresión de un mensaje.
        
def main(): # Función main.
    df = pd.read_csv("usuarios.csv") # Lectura del contenido del archivo csv de los usuarios por medio de la creación de un dataframe.
    PedalRide_Rentals(df) # Se crea una instancia de la clase (se pasa como argumento el dataframe del archivo csv de los usuarios).

if __name__ == "__main__": # Si el programa es ejecutado desde el archivo principal, entonces:
    main() # Se ejecuta el código.

