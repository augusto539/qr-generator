from ast import If
from functions.Replace_problematic_caracters import __replace__

def rite_in_the_svg(qr_string: str, nombre_asistente: str):
    from cgi import print_arguments

    old_qr = '<path id="qr-path"/>'

    # abro el texto de ejemplo
    my_file = open("plantilla_de_svg.txt")

    # Open file for reading
    content = my_file.read()
    # cambio el titulo
    new_title = content.replace("este_es_el_titulo", __replace__(nombre_asistente))
    # si el nombre del asistente es muy largo achico el font-size

    if len(nombre_asistente) <= 17:
        new_font_size = new_title
    if 17 < len(nombre_asistente) <= 22:
        new_font_size = new_title.replace(".st1{font-size:25px;}", ".st1{font-size:18px;}")
    if len(nombre_asistente) > 22:
        new_font_size = new_title.replace(".st1{font-size:25px;}", ".st1{font-size:13px;}")

    # cambio el qr
    new_qr = new_font_size.replace(old_qr, qr_string)


    # creo un nuevo documento
    new_file = open(f"qrs/{nombre_asistente}.svg", "w")
    # escrivo la nueva info en el documento
    new_file.write(new_qr)