def Apellido(apellidos="apellido1 apellido2"):
    if apellidos.count(' ') == 0 :
        return apellidos.capitalize()

    if apellidos.count(' ') == 1 :
        if apellidos.split()[0] == "DEL" or apellidos.split()[0] == "DI":
            return apellidos.capitalize()
        else:
            return apellidos.split()[0].capitalize()

    if apellidos.count(' ') >= 2 :
        return apellidos.capitalize()