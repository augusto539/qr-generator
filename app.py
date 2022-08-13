# colorama
from ast import If
from posixpath import split
from colorama import init
init()
# functions
from functions.rite_in_the_svg import rite_in_the_svg
from functions.make_qrs import make_the_qr
from functions.Load_excel_info import Load_excel_info
from functions.convert_the_last_name import Apellido

info = Load_excel_info("ejemplo.xlsx")

index = 0

for asistente in info:
    index += 1

    # creo la variable nobre: dividiendo y tomando el primer valor la variable asistente[Nombres] y capitalizo el string
    nombre = asistente['Nombres'].split()[0].capitalize()

    apellido = Apellido(asistente['Apellidos'])

    qr = make_the_qr(asistente["ID"])

    rite_in_the_svg(qr, nombre + " " + apellido)

    print(f"\033[1;32m Done:\033[39m Index: \033[1;33m {str(index).zfill(4)}\033[39m Nombre y Apellido: \033[1;33m {nombre} {apellido}\033[39m")
