'''
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
'''

REFORM = 1582
BIG_LEAP_YEAR = 400
SMALL_LEAP_YEAR = 4
LARGE_NON_LEAP_YEAR = 100
ZERO = 0

your_year = int(input('Введите год для проверки: '))

if  your_year < REFORM:
    result = 'Григорианский календарь ещё не был введён.'
elif your_year % BIG_LEAP_YEAR == ZERO:
    result = f'{your_year} год - високосный.'
elif your_year % LARGE_NON_LEAP_YEAR == ZERO:
    result = f'{your_year} год - не високосный.'
elif your_year % SMALL_LEAP_YEAR == ZERO:
    result = f'{your_year} год - високосный.'
else:
    result = f'{your_year} год - не високосный.'

print(result)