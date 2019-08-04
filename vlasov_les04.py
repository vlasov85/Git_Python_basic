import copy
import math
import random
import re
import os

# EASY ______________________________________________________________

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('\n', 'EASY_Задание-1')

def listR (number, min, max, roundD):
    listN = []
    i = 0
    while i < number:
        listN.append(round(random.uniform(min, max), roundD))
        i += 1
    return listN

my_list = listR(10, -100, 100, 0)
print('первоначальный список =', my_list)

for i in range(len(my_list)):
    my_list[i] = my_list[i]**2
print('измененный список =', my_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('\n', 'EASY_Задание-2')

def listF (name, number):
    listN = []
    i = 0
    while i < number:
        elem = random.choice(name)
        if elem in listN:
            i = i
        else:
            listN.append(elem)
            i += 1
    return listN

fruits = ['apple', 'apricot', 'avocado',\
          'banana',\
          'grape', 'grapefruit',\
          'kiwi',\
          'lemon', 'lime',\
          'mandarin', 'mango', 'melon',\
          'orange',\
          'peach', 'pear', 'pineapple', 'pomelo', 'plum']

my_list1 = listF(fruits, 10)
my_list2 = listF(fruits, 10)
print('список my_list1 =', my_list1)
print('список my_list2 =', my_list2)

list_gen = []

for i in my_list2:
    if i in my_list1:
        list_gen.append(i)
print('объединенный список фруктов = ', list_gen)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('\n', 'EASY_Задание-3')

def listR (number, min, max, roundD):
    listN = []
    i = 0
    while i < number:
        listN.append(round(random.uniform(min, max), roundD))
        i += 1
    return listN

my_list = listR(20, -100, 100, 0)
print('первоначальный список =', my_list)

listN = []

for i in range(0, len(my_list)):
    if my_list[i] > 0 and my_list[i] % 3 == 0 and my_list[i] % 4 !=0:
        listN.append(my_list[i])
    i += 1
print('отфильтрованный список =', listN)

# NORMAL ____________________________________________________________

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

print('\n', 'NORMAL_Задание-1')

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

my_list = list(line)
my_reserv = ''
my_line1 = []

i = 0
while i < len(my_list):
       if my_list[i].islower():
           my_reserv = my_reserv + my_list[i]
           if i == len(my_list)-1:
               my_line1.append(my_reserv)
       elif my_list[i-1].islower():
           my_line1.append(my_reserv)
           my_reserv = ''
       i += 1

print('символы в нижнем регистре =', my_line1)

my_line2 = re.findall(r'[a-z]+', line)
print('символы в нижнем рег (re) =', my_line2)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

print('\n', 'NORMAL_Задание-2___через re решено, без re не додумал, решил поделать HARD - и не осталось времени')

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

my_list = list(line)
my_reserv = ''
my_line1 = []

i = 2
while i < len(my_list)-2:
       if my_list[i+1].isupper() and my_list[i+2].isupper():
           my_reserv = my_reserv + my_list[i]
       elif len(my_reserv) != 0:
           my_line1.append(my_reserv)
           my_reserv = ''
       i += 1

print('символы в верхнем регистре =', my_line1)

line_2 = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line)
print('символы в верхнем рег (re) =',line_2)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print('\n', 'NORMAL_Задание-3')

def listRI(number, min, max):
    listN = []
    i = 0
    while i < number:
        listN.append(random.randint(min, max))
        i += 1
    return listN

def str_list(my_list):
    my_str = ''
    for i in my_list:
        my_str = my_str + str(i)
    return my_str

my_list1 = listRI(2500, 0, 9)
print('сгенерированный список = ', my_list1)

my_str1 = str_list(my_list1)

f = open('text.txt', 'w+', encoding='UTF-8')
f.write(my_str1)
f.close()

f = open('text.txt', 'r+', encoding='UTF-8')
for line in f:
    my_str2 = line
    break

my_list2 = list(my_str2)
print('строка из файла = ', my_list2)

num = 1
max = 1

for i in range(1, len(my_list2)):
       if my_list2[i] == my_list2[i-1]:
              num = num + 1
              if num > max:
                     max = num
                     value = my_list2[i]
       else:
              num = 1
print('самая длинная последовательность =', max, ', из цифры = ', value)

f.write('\n')
f.write('самая длинная последовательность = ') + f.write(str(max)) + f.write(', из цифры = ') + f.write(str(value))

f.close()

# HARD ______________________________________________________________

# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков.
# Выполнить поворот (транспонирование) матрицы.
# Суть сложности hard: Решите задачу в одну строку

print('\n', 'HARD_Задание-1')

matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

print("матрица (исходная) = ", matrix)
print("матрица (транспортированная) = ", list(map(list, zip(*matrix))))

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.

print('\n', 'HARD_Задание-2')

number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

def one_str(string):
    my_list = list(string)
    for i in my_list:
        if i == '\n':
            my_list.remove(i)

    my_number = ''
    for i in my_list:
        my_number = my_number + i
    return my_number

def list_num5(string):
    patern = '(?=([0-9]{5}))'
    result = re.findall(patern, string)
    return result

def proizv(list):
    result = 1
    for i in range(len(list)):
        result *= int(list[i])
    return result

print('однострочное число =', one_str(number))

list5 = list_num5(one_str(number))
print('список из 5ти значных чисел =', list5)

proizv_max = 0
for i in list5:
    proizv_num5 = proizv(i)
    if proizv_num5 > proizv_max:
        proizv_max = proizv_num5
        ind = one_str(number).index(str(i))

print('max произведение 5ти чисел =', proizv_max)
print('числа -', one_str(number)[ind], one_str(number)[ind+1], one_str(number)[ind+2], one_str(number)[ind+3], one_str(number)[ind+4])
print('индекс первого числа max произведения =', ind)

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

print('\n', 'HARD_Задание-3___не хватило времени ')