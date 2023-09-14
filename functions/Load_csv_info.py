import csv

def Load_csv_info(csv_route: str):
    # cargo el archivo CSV
    with open('ejemplo.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        list_of_data = []

            # recorro las filas del archivo CSV
        for row in csv_reader:
                # agrego el nuevo diccionario a la lista
            list_of_data.append(row["ID DB"])

    # print(list_of_data)
    return list_of_data


# Load_csv_info("ejemplo.csv")

