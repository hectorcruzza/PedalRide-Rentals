import pandas as pd
import numpy as np
import datetime as dt

df_reservaciones = pd.read_csv("reservaciones_confirmadas.csv", dtype = str)
fecha_hora_actual = dt.datetime.now().replace(microsecond = 0)

fecha_actual_datetime = fecha_hora_actual.date()
fecha_actual = fecha_hora_actual.strftime("%d/%m/%Y")
hora_actual = fecha_hora_actual.strftime("%H:%M")

reservaciones = df_reservaciones[["Fecha de la Reservación", "Hora de Inicio", "Hora de Término"]].to_numpy()


# for i in range(len(df_reservaciones)):
#     print(f"Reservación {i + 1}:")
#     print(f"Fecha de la Reservación: {reservaciones[i][0]} - Hora de Inicio: {reservaciones[i][1]} - Hora de Término: {reservaciones[i][2]}.")
#     fecha_hora_reservacion_str = f"{reservaciones[i][0]} {reservaciones[i][1]}"
#     fecha_hora_reservacion_datetime = dt.datetime.strptime(fecha_hora_reservacion_str, "%d/%m/%Y %H:%M").replace()
#     print(f"Fecha y Hora de Inicio de la Reservación: {fecha_hora_reservacion_datetime}.")
#     if fecha_hora_actual >= fecha_hora_reservacion_datetime:
#         df_reservaciones.drop(i, inplace = True)
#         print(df_reservaciones.iloc[i])
#         df_reservaciones.to_csv("reservaciones_confirmadas.csv", index = None)
#         print(f"La reservación ya ha sucedido y se borrará de la lista de reservaciones confirmadas: {fecha_hora_actual >= fecha_hora_reservacion_datetime}.")

# reservaciones_confirmadas = df_reservaciones.loc[df_reservaciones["Correo Electrónico"] == "gerardo@edvolution.io"].to_numpy()

# print(len(reservaciones_confirmadas))

# print("| N.º de Reservación |    Fecha    |    Horario    | N.º de Bicicleta |  Costo  |")
# for j in range(len(reservaciones_confirmadas)):
#     horario_reserva = f"{reservaciones_confirmadas[j][5]} - {reservaciones_confirmadas[j][6]}"
#     print("        ", reservaciones_confirmadas[j][0], "           ", reservaciones_confirmadas[j][4], "  ", horario_reserva, "       ", reservaciones_confirmadas[j][7], "         ", reservaciones_confirmadas[j][8])

