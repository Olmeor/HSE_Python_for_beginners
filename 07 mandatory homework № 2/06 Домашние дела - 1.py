# Домашние дела - 1
# Женя и Саша распределяют между собой домашние дела из общего списка, при этом стараясь поделить работу пополам: если
# в списке четное количество дел, то Женя делает первую половину, а Саша — вторую; если в списке нечетное число задач,
# то задачу, которая оказалась посередине, они делают вместе (она попадает в список задач и Саши, и Жени).
#
# Напишите программу, которая принимает на вход общий список дел и выводит списки дел для Саши и Жени.
#
# ФОРМАТ ВВОДА
# Общий непустой список дел, перечисленных через запятую и пробел.

# ФОРМАТ ВЫВОДА
# Два списка через запятую и пробел: сначала список дел Жени, затем список дел Саши каждый список выводится с новой
# строки.

todos = input().split(', ')
mid = len(todos) // 2 if len(todos) % 2 == 0 else len(todos) // 2 + 1
if len(todos) % 2:
    todo1 = todos[:mid]
    todo2 = todos[mid - 1:]
else:
    todo1 = todos[:mid]
    todo2 = todos[mid:]

print(', '.join(todo1), ', '.join(todo2), sep="\n")
