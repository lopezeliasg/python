import calendar
from pathlib import Path

meses_Anio = list(calendar.month_name[1:])

'''Iterar con ciclo for dias del 1 al 30 y agregar en lista dia_Semana'''
dias_Semana = []
for i in range(1, 31):
    dias_Semana.append("Día " + str(i))
#print(dia_semana)

'''Crear carpetas con dias de semana/meses y año'''
for i, mes in enumerate(meses_Anio):
    for dia in dias_Semana:
        Path(f'2023/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)
        #Año 2023 elemento padre y si hay errores 'exist_ok' para no dar error