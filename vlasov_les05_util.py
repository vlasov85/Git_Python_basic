import copy
import math
import random
import re
import os
import shutil
import sys

import vlasov_les05

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print('Текущая директория {}'.format(os.getcwd()))

menu = 100
try:
    while (menu > 0 or menu <= 4):

        menu = int(input('''Выберите один из пунктов
        1. Перейти в папку
        2. Просмотреть содержимое текущей папки
        3. Создать папку
        4. Удалить папку
        0. Выход
        Ваш выбор: '''))

        if menu == 1:
            folder = str(input('В какую папку вы хотите перейти: '))
            os.chdir(folder)
        elif menu == 2:
            print('содержимое текущей папки = ', vlasov_les05.dir_cur())
        elif menu == 3:
            folder = str(input('Какую папку вы хотите создать: '))
            vlasov_les05.make_dir(folder)
        elif menu == 4:
            folder = str(input('Какую папку вы хотите удалить: '))
            vlasov_les05.del_dir(folder)
        elif menu == 0:
            pass

except (ValueError, FileNotFoundError, OSError):
    print('Невозможно выполнить действие')