# Вася и Маша играют в игру: Вася пишет какое-то слово не меньше 6 букв, а затем Маша начинает составлять слова из букв
# Васиного слова. Составьте программу, которая проверяет для какого-либо слова, может ли Маша использовать его в игре.
# Буквы могут повторяться (например, если Вася написал "кошмар", Маша может написать "мама" — и "м", и "а" есть в
# исходном слове)
#
# ФОРМАТ ВВОДА
# На первой строке — слово Васи со строчной буквы;
# на второй — слово от Маши.
#
# ФОРМАТ ВЫВОДА
# Если Машино слово можно использовать: "ДА".
# Если слово нельзя использовать: "НЕТ".

word_v, word_m = set(input()), set(input())

print('ДА' if word_m & word_v == word_m else 'НЕТ')
