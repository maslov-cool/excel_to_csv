import openpyxl
import csv

# Загрузите файл Excel
workbook = openpyxl.load_workbook(filename='data.xlsx', data_only=True)

# Выберите первый лист
sheet = workbook.worksheets[0]

# Создайте список для хранения значений
values_list = []

# Переберите все строки и столбцы, чтобы получить значения ячеек
for row in sheet.iter_rows(values_only=True):
    values_list.append(list(row))

# Теперь values_list содержит все значения из первой закладки

with open('output.csv', 'w', newline='', encoding="utf8") as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(values_list)




