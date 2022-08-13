def __replace__(string_to_replace:str):
    string_to_replace = string_to_replace.replace("á", "a")

    string_to_replace = string_to_replace.replace("é", "e")

    string_to_replace = string_to_replace.replace("í", "i")

    string_to_replace = string_to_replace.replace("ó", "o")

    string_to_replace = string_to_replace.replace("ú", "u")

    string_to_replace = string_to_replace.replace("ü", "u")

    string_to_replace = string_to_replace.replace("ñ", "n")


    # kk = string_to_replace.encode('utf8')

    return string_to_replace