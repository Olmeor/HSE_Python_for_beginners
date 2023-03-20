# Стихи
# Дан файл poetry.txt, который содержит в себе стихотворение. Выведите его построчно на экран.
#
# ФОРМАТ ВВОДА
# Файл poetry.txt в кодировке utf-8.
#
# ФОРМАТ ВЫВОДА
# Текст файла построчно.
# Не забудьте удалить знак перехода на новую строку из строки файла перед тем, как печатать ее!

try:
    with open('poetry.txt', 'r', encoding='utf-8') as file:
        poetry = file.read()
except FileNotFoundError:
    print("File Not Found")

for line in poetry:
    print(line, end="")
