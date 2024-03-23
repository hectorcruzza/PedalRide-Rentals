import pandas as pd
import datetime as dt

bicicletas = {"Bicicleta de Ciudad": ["Urbana, práctica, ágil.", ["005", "010", "015"], 60],
              "Bicicleta de Montaña": ["Todo terreno, robusta.", ["020", "025", "030"], 90],
              "Bicicleta de Turismo": ["Largas distancias.", ["035", "040", "045"], 80],
              "Bicicleta Eléctrica": ["Eficiente, rápida.", ["050", "055", "067"], 100]} 

tipo_bicicleta = "Bicicleta Eléctrica"
bicicletas_disponibles_por_tipo = ["050", "067"]
bicicletas_disponibles = dict()
opcion_tipo_bicicleta = 1
bicicletas_disponibles[str(opcion_tipo_bicicleta)] = {tipo_bicicleta: bicicletas_disponibles_por_tipo}
print(bicicletas_disponibles)
tipo_bicicleta = "Bicicleta de Ciudad"
bicicletas_disponibles_por_tipo = ["010"]
opcion_tipo_bicicleta = 2
bicicletas_disponibles[str(opcion_tipo_bicicleta)] = {tipo_bicicleta: bicicletas_disponibles_por_tipo}
print(bicicletas_disponibles)

print()

opcion_usuario = input("Elija la bicicleta a rentar con base en su número de tipo: > ")
reserva_bicicleta = [*bicicletas_disponibles[opcion_usuario]][0]
print(reserva_bicicleta)

numero_bicicleta = bicicletas_disponibles[opcion_usuario][reserva_bicicleta]
numero_bicicleta_2 = [*bicicletas_disponibles[opcion_usuario].values()][0]

print(numero_bicicleta)
print(numero_bicicleta_2)

# fecha_hora_actual_datetime = dt.datetime.now().replace(microsecond = 0)
# print(f"Fecha y Hora Actual: {fecha_hora_actual_datetime}\n")

# df_reservaciones = pd.read_csv("reservaciones.csv", dtype = {
#     "Número de Reservación": int,
#     "Nombre(s)": str,
#     "Apellidos": str,
#     "Correo Electrónico": str,
#     "Fecha de la Reservación": str,
#     "Hora de Inicio": str,
#     "Hora de Término": str,
#     "Número de Bicicleta": str,
#     "Tipo de Bicicleta": str,
#     "Costo": str,
#     "Número de Teléfono": str
# })

# reservaciones = df_reservaciones.loc[df_reservaciones["Correo Electrónico"] == "gerardo@edvolution.io"].to_numpy().tolist()
# reservaciones.sort(key = lambda elemento: (dt.datetime.strptime(elemento[4], "%d/%m/%Y").date(), dt.datetime.strptime(elemento[5], "%H:%M").time()))

# reservaciones_confirmadas = [reservacion for reservacion in reservaciones if fecha_hora_actual_datetime < dt.datetime.strptime(f"{reservacion[4]} {reservacion[5]}", "%d/%m/%Y %H:%M")]

# if reservaciones_confirmadas:
#     print(f"Las reservaciones confirmadas del usuario son las siguientes: {reservaciones_confirmadas}.\n")
#     numeros_reservaciones_posible_cancelacion = [reservacion_confirmada[0] for reservacion_confirmada in reservaciones_confirmadas if fecha_hora_actual_datetime <= dt.datetime.strptime(f"{reservacion_confirmada[4]} {reservacion_confirmada[5]}", "%d/%m/%Y %H:%M") - dt.timedelta(hours = 24)]
#     if numeros_reservaciones_posible_cancelacion:
#         print("Las siguientes reservaciones pueden ser canceladas: ")
#         print("\n| N.º de Reservación |")
#         for numero_reservacion in numeros_reservaciones_posible_cancelacion:
#             print(f"\t {numero_reservacion}")
#     else:
#         print("Ninguna reservación puede ser cancelada.")
# else:
#     print("No hay reservaciones confirmadas.")

# try:
#     numero = int(input())
# except ValueError:
#     print("we puta")