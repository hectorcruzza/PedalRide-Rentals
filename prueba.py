import pandas as pd
import datetime as dt

df_reservaciones = pd.read_csv("reservaciones.csv")

# index_reservacion = df_reservaciones.loc[df_reservaciones["Número de Reservación"] == 945].index

informacion_reservacion = df_reservaciones.loc[df_reservaciones["Número de Reservación"] == 945].to_numpy()

fecha_hora_actual_datetime = dt.datetime.now().replace(microsecond = 0)
fecha_actual = fecha_hora_actual_datetime.strftime("%d/%m/%Y")
hora_actual = fecha_hora_actual_datetime.strftime("%H:%M")

print(f"Fecha Actual: {fecha_actual}")
print(f"Hora Actual: {hora_actual}")

fecha_hora_reservacion_str = f"{informacion_reservacion[0][4]} {informacion_reservacion[0][5]}"
fecha_hora_reservacion_datetime = dt.datetime.strptime(fecha_hora_reservacion_str, "%d/%m/%Y %H:%M")

print(f"Fecha y Hora de la Reservación: {fecha_hora_reservacion_datetime}")

container = dt.datetime.strptime("14/03/2024 12:00", "%d/%m/%Y %H:%M")
print(container)

print(fecha_hora_reservacion_datetime - dt.timedelta(hours = 24))
print(f"Faltan al menos 24 horas para la reservación {fecha_hora_actual_datetime <= fecha_hora_reservacion_datetime - dt.timedelta(hours = 24)}.")
print(f"Faltan al menos 24 horas para la reservación {container <= fecha_hora_reservacion_datetime - dt.timedelta(hours = 24)}.")

print()

x = None
print(not x)
y = False
print(not y)

# df_reservaciones.drop(index_reservacion, inplace = True)
# df_reservaciones.to_csv("reservaciones.csv", index = None)
