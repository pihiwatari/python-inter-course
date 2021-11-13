import json
from os import name


def run():

    # importamos los archivos de json y los asignamos a la constante DATA

    json_file = open('MOCK_DATA.json')

    DATA = json.load(json_file)

    # ciclo for para traer datos de json

    # for item in DATA:
    #     if item['age'] <= 45:
    #         print(item['first_name'])

    # list comprehension para procesar datos json

    # name_list = [item['first_name'] for item in DATA if item['age'] < 45]

    # filter y map para obtener datos de json

    name_list = list(filter(lambda item: item['age'] < 45, DATA))
    name_list = list(map(lambda item: item['first_name'], name_list))

    # crear diccionarios nuevos con llaves y valores nuevos
    # old_people = list(map(lambda item: item | {"old": item['age'] > 28}, DATA))

    old_people = [item | {'old': item['age'] > 28} for item in DATA]
    old_people = [item['first_name']
                  for item in old_people if item['old'] == True]

    print(old_people)

    # cerramos el archivo json

    json_file.close()


if __name__ == '__main__':
    run()
