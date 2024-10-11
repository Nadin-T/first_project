'''
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
'''

SPACE = ' '
STAR = '*'

rows = int(input('Введите количество рядов для ёлки: '))
spaces = rows - 1
stars = 1

for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    spaces -= 1
    stars += 2

