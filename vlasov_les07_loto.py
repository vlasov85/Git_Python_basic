import copy
import json
import math
import os
import random
import re
import shutil
import sys
import array

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

barrel_num = 90
barrels = random.sample(range(1, 91), 90)
#print('бочонки', barrels)

p1_num = 15
p1_set = random.sample(range(1, 91), 15)
#print(p1_set)
p1_field = [sorted(p1_set[:5]), sorted(p1_set[5:10]), sorted(p1_set[10:])]

p2_num = 15
p2_set = random.sample(range(1, 91), 15)
#print(p2_set)
p2_field = [sorted(p2_set[:5]), sorted(p2_set[5:10]), sorted(p2_set[10:])]


def card(field, player):
    for line in field:
        while len(line) < 9:
            line.insert(random.randint(0, len(field)), ' ')
    print('{:-^26}'.format(player))

    for line in field:
        for i in line:
            print('{0:>2}'.format(i), end=' ')
        print()
    print('{:-^26}'.format('-'))


def p1_move():
    answer = input('Зачеркнуть цифру (в случае ошибки вы проиграете)? (y/n): ')
    if answer == 'y':
        if barrel in p1_set:
            for l in p1_field:
                try:
                    l.insert(l.index(barrel), '-')
                    l.pop(l.index(barrel))
                except ValueError:
                    continue
            print('   Идем дальше!')
            return 1
        else:
            print('   К сожалению вы проиграли!')
            sys.exit()
    if answer == 'n':
        if barrel in p1_set:
            print('   К сожалению вы ошиблись и проиграли!')
            sys.exit()
        else:
            print('   Идем дальше!')


def p2_move():
    if barrel in p2_set:
        for i in p2_field:
            try:
                i.insert(i.index(barrel), '-')
                i.pop(i.index(barrel))
            except ValueError:
                continue
        return 1


for barrel in barrels:
    barrel_num -= 1
    print('\nВыпавший бочонок номер: {} (в мешке осталось: {})'.format(barrel, barrel_num))
    card(p1_field, ' player ')
    card(p2_field, ' computer ')

    if p1_move() == 1:
        p1_num -= 1
    if p2_move() == 1:
        p2_num -= 1

    if p1_num == 0:
        print('   Поздравляем! Вы выиграли')
        sys.exit()
    if p2_num == 0:
        print('   Вы проиграли!')
        sys.exit()
