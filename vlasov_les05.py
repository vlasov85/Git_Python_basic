import copy
import math
import random
import re
import os
import shutil
import sys

# EASY ______________________________________________________________
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('\n', 'EASY_Задание-1')

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
    except OSError:
        print(f"Не удалось создать - {dir_path}")
    else:
        print(f"Создана - {dir_path}")

def del_dir(paths):
    try:
        shutil.rmtree(paths)
    except OSError:
        print(f"Не удалось удалить {paths}")
    else:
        print(f"Удачно удалена - {paths}")

dir_name = [('dir_' + str(i + 1)) for i in range(9)]

for i in dir_name:
    make_dir(i)
    del_dir(i)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\n', 'EASY_Задание-2')

def dir_cur():
    return os.listdir(os.getcwd())

print('содержимое текущей директории = ', dir_cur())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n', 'EASY_Задание-3')

def copy_file(cur_file, new_file):
    shutil.copy(cur_file, new_file)

file_cur = sys.argv[0]
file_new = str(file_cur)[:-3] + '_copy.py'
copy_file(file_cur, file_new)