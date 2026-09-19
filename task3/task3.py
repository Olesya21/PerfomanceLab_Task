import json
import argparse

#Объявление парсера для аргументов командной строки
parser = argparse.ArgumentParser()

#Добавление аргументов
parser.add_argument("values")
parser.add_argument("tests")
parser.add_argument("report")

#Парсинг аргументов командной строки
args = parser.parse_args()

#Открытие файла values
file = open(args.values)

#Загрузка json данных из файла values
jsonData = json.load(file)
#Получение словаря значений
jsonData = jsonData["values"]

#Инициализация нового словаря
valuesDict = dict()

#Для каждой пары в jsonData
for val in jsonData:
    #Создание листа значений
    valList = list(val.values())
    #Заполнение нового словаря: id - ключ, value - значение
    valuesDict[valList[0]] = valList[1]

#Закрытие файла values
file.close()

#Открытие файла tests
file = open(args.tests)
#Загрузка json данных
jsonData = json.load(file)
#Закрытие файла tests
file.close()

def setValues(tests, values):
    #Для каждого теста в списке
    for t in tests:
        #Есть ли в списке values такой айди как у текущего t
        if values.__contains__(t["id"]):
            #Установка значения в поле value для t
            t["value"] = values[int(t["id"])]
        #Если у текущего t есть список тестов в поле values
        if t.keys().__contains__("values"):
            #Рекурсивно проводим ту же операцию с этим списком
            setValues(t["values"], values)

#Установка значений из файла values в данные из tests
setValues(jsonData["tests"], valuesDict)

#Открытие файла report
file = open(args.report, 'w')

#Загрузка измененных данных tests в файл report.json
json.dump(jsonData, file, indent=2)

#Закрытие файла report
file.close()