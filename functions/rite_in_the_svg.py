def rite_in_the_svg(qr_string: str, nombre_asistente: str):
    from cgi import print_arguments

    old_qr = '<path id="qr-path"/>'

    # abro el texto de ejemplo
    my_file = open("plantilla_de_svg.txt")

    # Open file for reading
    content = my_file.read()
    # cambio el titulo
    new_title = content.replace("este_es_el_titulo", nombre_asistente)
    # cambio el qr
    new_qr = new_title.replace(old_qr, qr_string)

    # creo un nuevo documento
    new_file = open(f"qrs/{nombre_asistente}.svg", "w")
    # escrivo la nueva info en el documento
    new_file.write(new_qr)