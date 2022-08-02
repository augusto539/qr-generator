# colorama
from colorama import init
init()
# functions
from functions.rite_in_the_svg import rite_in_the_svg
from functions.make_qrs import make_the_qr
from functions.Load_excel_info import Load_excel_info

info = Load_excel_info("ejemplo.xlsx")

for asistente in info:

    qr = make_the_qr(asistente["ID"])

    rite_in_the_svg(qr, asistente['Nombres']+" "+asistente['Apellidos'])

    print ("qr de: "+asistente['Nombres']+" "+asistente['Apellidos']+"\033[1;32m listo \n \033[39m")
