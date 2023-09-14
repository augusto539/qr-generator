from ast import If
from posixpath import split
from colorama import init

init()
# functions
from functions.rite_in_the_svg import rite_in_the_svg
from functions.make_qrs import make_the_qr
from functions.Load_excel_info import Load_excel_info
from functions.convert_the_last_name import Apellido
from functions.Load_csv_info import Load_csv_info

info = Load_csv_info("ejemplo.csv")

index = 0

for asistente in info:
    index += 1

    # creo la variable nonbre: dividiendo y tomando el primer valor la variable asistente[Nombres] y capitalizo el string
    # nombre = asistente['Nombre'].split()[0].capitalize()
    nombre = asistente

    qr = make_the_qr(asistente)

    rite_in_the_svg(qr, nombre)

    print(f"\033[1;32m Done:\033[39m Index: \033[1;33m {str(index).zfill(4)}\033[39m Nombre y Apellido: \033[1;33m {nombre}\033[39m")