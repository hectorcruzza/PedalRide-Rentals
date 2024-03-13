import pandas as pd
import numpy as np

df = pd.read_csv("usuarios.csv")
print(df)
print()
print(df.loc[df["Nombre(s)"] == "Gerardo"])
print()
print(df.loc[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"])
print()
print(df.loc[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"].iloc[0])
print()
print(df.loc[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"].iloc[0]["Contraseña"])
print()
print(df["Nombre(s)"].loc[df.index[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"][0]])
print()
print(df["Nombre(s)"].iloc[df.index[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"][0]])
print()
print(df.index[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"][0])
print()
print(df["Nombre(s)"].loc[df.index[0]])
print()
print(df["Nombre(s)"].loc[0])
print()
print(df.loc[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"])
print()
print(df.loc[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"].iloc[0])
print()
informacion_usuario_logeado = list(df.loc[df["Correo Electrónico"] == "hectorivancruzalayola@gmail.com"].iloc[0]) # Lista de filas
print(informacion_usuario_logeado)
print()

df_2 = pd.read_csv("reservaciones_confirmadas.csv", dtype = str)
print("HOLA")
bicicleta = df_2["Número de Bicicleta"].iloc[0]
print(bicicleta)
print(type(bicicleta))

print(len(df_2))
print()
print(list(df["Nombre(s)"]))
print()
print("NUMPY")
print(df[["Nombre(s)", "Primer Apellido"]].to_numpy().tolist())
print()
print(df_2[["Número de Bicicleta", "Fecha de la Reservación", "Hora de Inicio", "Hora de Término"]])
print()
print(df.loc[:, ["Nombre(s)", "Primer Apellido"]])
print()
print(df["Nombre(s)"].iloc[1])
print(type(df["Nombre(s)"].iloc[1]))

set_ = [0, 1, 2, 3, 4, 5]
lista = list(range(1000))
lista_np = np.array(range(1000))

numero = 1
nombre = "Gerardo Luis"
apellidos = "Navarrete Teran"
fecha = "11/03/2024"
horario = "10:00 - 12:00"
numero_bici = "067"
costo = "360"

print("| N.º de Reservación |       Nombre(s)       |       Apellidos       |      Fecha      |      Horario      |")
print("         ",numero, "              ", nombre, "         ", apellidos, "       ", fecha, "     ", horario, "\n")
print("                                       | N.º de Bicicleta |   Costo   |")
print("                                              ", numero_bici, "           ", costo, "\n")

