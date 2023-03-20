# Цветочный магазин
# У Леши свой цветочный магазин, для которого он ведет статистику.
#
# Каждый заказ он записывает с новой строки в файл по типу "Роза 1500", где "Роза" — это цветок, который купили, а 1500
# — сумма покупки. Помогите Леше преобразовать статистику из его файла в словарь Python.
#
# ФОРМАТ ВВОДА
# Файл orders.txt, где на каждой строке записан заказ в формате "<название цветка> <сумма>", разделенные пробелом.
#
# ФОРМАТ ВЫВОДА
# Словарь Python, где ключи — названия цветов, а значения — общая выручка. Ключи добавляются в словарь в том порядке, в
# котором они впервые встречаются в файле.

try:
    with open('orders.txt', 'r', encoding='utf-8') as file:
        orders = file.readlines()
except FileNotFoundError:
    print("File Not Found")

dct = {}
for row in orders:
    flower = row.split()
    dct[flower[0]] = dct.get(flower[0], 0) + int(flower[1])

print(dct)
