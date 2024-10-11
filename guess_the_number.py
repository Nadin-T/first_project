from random import randint
'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT) 
'''

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ZERO = 0
GUESS_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = ZERO

for i in range(1, GUESS_COUNT + 1):
    try:
        user_num = int(input(f'Введите целое число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    except ValueError:
        print('Пожалуйста, введите целое число.')
        continue

    count += 1

    if user_num == num:
        if count == 1:
            guess = 'попытку'
        elif 2 <= count < 5:
            guess = 'попытки'
        else:
            guess = 'попыток'

        print(f'Вы угадали число за {count} {guess}!')
        break
    elif user_num < num:
        print(f'Ваше число меньше загаданного.')
    else:
        print(f'Ваше число больше загаданного.')

    if count == GUESS_COUNT:
        print(f'Попытки закончились! Загаданное число - {num}.')
    else:
        print(f'Использовано попыток: {count} из {GUESS_COUNT}. \nПопробуйте снова')
