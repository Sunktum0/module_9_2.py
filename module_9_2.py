# Исходные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Переменная first_result: длины строк из first_strings >= 5
first_result = [len(word) for word in first_strings if len(word) >= 5]

# Переменная second_result: кортежи одинаковой длины
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]

# Переменная third_result: словарь с чётными длинами строк
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
