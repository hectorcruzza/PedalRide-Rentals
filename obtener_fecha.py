import calendar as cd
import datetime as dt
import re

fecha_actual_datetime = dt.date.today()
dia_actual = fecha_actual_datetime.day
mes_actual = fecha_actual_datetime.month
año_actual = fecha_actual_datetime.year
fecha_actual = fecha_actual_datetime.strftime("%d/%m/%Y")
dias_mes = cd.monthrange(año_actual, mes_actual)[1]

print(f"Fecha Actual: {fecha_actual}.")
print(f"Día: {dia_actual} - Mes: {mes_actual} - Año: {año_actual}.")
print(f"Días del Mes: {dias_mes}.\n")

while True:
    fecha_reserva = input("- Ingrese la fecha de la reservación (Formato: DD/MM/AAAA): > ")
    formato_fecha = r"^\d{2}/\d{2}/\d{4}$"
    if re.match(formato_fecha, fecha_reserva):
        try:
            fecha_reserva_datetime = dt.datetime.strptime(fecha_reserva, "%d/%m/%Y").date()
            dia_reserva = fecha_reserva_datetime.day
            mes_reserva = fecha_reserva_datetime.month
            año_reserva = fecha_reserva_datetime.year
            print(f"Fecha de la Reservación: {fecha_reserva_datetime}.")
            print(f"Día: {dia_reserva} - Mes: {mes_reserva} - Año: {año_reserva}.")
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

hora_actual_container = dt.datetime.now()
horas_actual = hora_actual_container.hour
minutos_actual = hora_actual_container.minute
hora_actual = hora_actual_container.strftime("%H:%M")
print(f"Hora Actual: {hora_actual}.")
print(f"Horas: {horas_actual} - Minutos: {minutos_actual}.")

while True:
    while True:
        hora_inicio_reserva = input("- Ingrese la hora de inicio de la reservación (Formato de 24 horas: HH:MM): ")
        formato_hora = r"^\d{2}:\d{2}$"
        if re.match(formato_hora, hora_inicio_reserva):
            try:
                hora_inicio_reserva_datetime = dt.datetime.strptime(hora_inicio_reserva, "%H:%M")
                horas_inicio_reserva = hora_inicio_reserva_datetime.hour
                minutos_inicio_reserva = hora_inicio_reserva_datetime.minute
                print(f"Hora de Inicio de la Reservación: {hora_inicio_reserva}.")
                print(f"Horas: {horas_inicio_reserva} - Minutos: {minutos_inicio_reserva}.")
                print()
                break
            except:
                print("La hora de inicio ingresada no es válida. Inténtelo de nuevo.\n")
        else:
            print("El formato de la hora de inicio ingresada no es válido. Inténtelo de nuevo.\n")

    while True:
        hora_termino_reserva = input("- Ingrese la hora de término de la reservación (Formato de 24 horas: HH:MM): ")
        if re.match(formato_hora, hora_termino_reserva):
            try:
                hora_termino_reserva_datetime = dt.datetime.strptime(hora_termino_reserva, "%H:%M")
                horas_termino_reserva = hora_termino_reserva_datetime.hour
                minutos_termino_reserva = hora_termino_reserva_datetime.minute
                print(f"Hora de Término de la Reservación: {hora_termino_reserva}.")
                print(f"Horas: {horas_termino_reserva} - Minutos: {minutos_termino_reserva}.")
                print()
                break
            except:
                print("La hora de término ingresada no es válida. Inténtelo de nuevo.\n")
        else:
            print("El formato de la hora de término ingresada no es válido. Inténtelo de nuevo.\n")
    
    formato_hora_minutos = r"^\d{2}:00$"
    diferencia_horas = horas_inicio_reserva - (horas_actual + (minutos_actual / 60))
    print(f"Diferencia de Horas: {diferencia_horas}.")
    print(f"Fecha Actual Datetime: {fecha_actual_datetime}.")
    print(f"Fecha de Reservación Datetime: {fecha_reserva_datetime}.")
    print(f"La fecha de la reservación es mayor a la actual: {fecha_reserva_datetime > fecha_actual_datetime}")
    
    if re.match(formato_hora_minutos, hora_inicio_reserva) and re.match(formato_hora_minutos, hora_termino_reserva) \
    and horas_inicio_reserva >= 8 and horas_inicio_reserva <= 20 and horas_termino_reserva >= 8 and horas_termino_reserva <=20 \
    and (fecha_reserva_datetime > fecha_actual_datetime or diferencia_horas >= 1):
        if hora_inicio_reserva_datetime < hora_termino_reserva_datetime:
            break
        else:
            print("El horario ingresado no es válido. Inténtelo de nuevo.")
    else:
        print("El horario ingresado no cumple con las condiciones establecidas. Inténtelo de nuevo.")

    





