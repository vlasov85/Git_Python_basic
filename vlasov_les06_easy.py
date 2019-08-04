import copy
import math
import random
import re
import os
import shutil
import sys

# EASY ______________________________________________________________
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, xA, yA, xB, yB, xC, yC):
        self.xA = xA
        self.yA = yA
        self.xB = xB
        self.yB = yB
        self.xC = xC
        self.yC = yC

    def sides(self):
        AB = round(((self.xB - self.xA) ** 2 + (self.yB - self.yA) ** 2) ** 0.5, 1)
        AC = round(((self.xC - self.xA) ** 2 + (self.yC - self.yA) ** 2) ** 0.5, 1)
        BC = round(((self.xC - self.xA) ** 2 + (self.yC - self.yA) ** 2) ** 0.5, 1)
        return AB, AC, BC

    def square(self):
        return round(0.5 * abs((self.xB - self.xA) * (self.yC - self.yA) - (self.xC - self.xA) * (self.yB - self.yA)), 1)

    def perimeter(cls):
        return round(cls.sides()[0] + cls.sides()[1] + cls.sides()[2], 1)

    def height(cls):
        h1 = round(2 * cls.square() / cls.sides()[0], 1)
        h2 = round(2 * cls.square() / cls.sides()[1], 1)
        h3 = round(2 * cls.square() / cls.sides()[2], 1)
        return h1, h2, h3


tr1 = Triangle(0, 0, 10, 30, 30, 40)
print('\n', 'EASY_Задание-1')
print('стороны треугольника =', tr1.sides())
print('площадь треугольника =', tr1.square())
print('периметр треугольника =', tr1.perimeter())
print('высоты треугольника =', tr1.height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:
    def __init__(self, xA, yA, xB, yB, xC, yC, xD, yD):
        self.xA = xA
        self.yA = yA
        self.xB = xB
        self.yB = yB
        self.xC = xC
        self.yC = yC
        self.xD = xD
        self.yD = yD

    def intersection(self):
        v1 = (self.xD - self.xC) * (self.yA - self.yC) - (self.yD - self.yC) * (self.xA - self.xC)
        v2 = (self.xD - self.xC) * (self.yB - self.yC) - (self.yD - self.yC) * (self.xB - self.xC)
        v3 = (self.xB - self.xA) * (self.yC - self.yA) - (self.yB - self.yA) * (self.xC - self.xA)
        v4 = (self.xB - self.xA) * (self.yD - self.yA) - (self.yB - self.yA) * (self.xD - self.xA)
        if (v1 * v2 < 0) and (v3 * v4 < 0):
            return True
        return False

    def sides(cls):
        if cls.intersection() == False:
            AB = round(((cls.xB - cls.xA) ** 2 + (cls.yB - cls.yA) ** 2) ** 0.5, 1)
            CD = round(((cls.xD - cls.xC) ** 2 + (cls.yD - cls.yC) ** 2) ** 0.5, 1)
            AC = round(((cls.xC - cls.xA) ** 2 + (cls.yC - cls.yA) ** 2) ** 0.5, 1)
            BD = round(((cls.xD - cls.xB) ** 2 + (cls.yD - cls.yB) ** 2) ** 0.5, 1)
            return AB, CD, AC, BD
        else:
            AC = round(((cls.xB - cls.xA) ** 2 + (cls.yB - cls.yA) ** 2) ** 0.5, 1)
            BD = round(((cls.xD - cls.xC) ** 2 + (cls.yD - cls.yC) ** 2) ** 0.5, 1)
            AD = round(((cls.xC - cls.xA) ** 2 + (cls.yC - cls.yA) ** 2) ** 0.5, 1)
            CB = round(((cls.xD - cls.xB) ** 2 + (cls.yD - cls.yB) ** 2) ** 0.5, 1)
            return AC, BD, AD, CB

    def is_trap(self):
        if (self.yB - self.yA) * (self.xB - self.xA) == (self.yD - self.yC) * (self.xD - self.xC):
            return 'type_1'
        elif (self.yC - self.yA) * (self.xC - self.xA) == (self.yD - self.yB) * (self.xD - self.xB):
            return 'type_2'
        return False

    def base_trapeza(cls):
        if cls.is_trap() == 'type_1':
            if cls.sides()[2] == cls.sides()[3]:
                return 'равнобочная с основаниями AB и CD'
            return 'неравнобочная с основаниями AB и CD'
        elif cls.is_trap() == 'type_2':
            if cls.sides()[2] == cls.sides()[3]:
                return 'равнобочная с основаниями AC и BD'
            return 'неравнобочная с основаниями AC и BD'
        return False

    def perimeter(cls):
        return round(cls.sides()[0] + cls.sides()[1] + cls.sides()[2] + cls.sides()[3], 1)

    def square(cls):
        if cls.is_trap() == 'type_1':
            h = (cls.sides()[2] ** 2 - abs((cls.sides()[0] - cls.sides()[1])) ** 2) ** 0.5
            return round(0.5 * h * (cls.sides()[0] + cls.sides()[1]), 1)
        elif cls.is_trap() == 'type_2':
            h = (cls.sides()[2] ** 2 - abs((cls.sides()[0] - cls.sides()[1])) ** 2) ** 0.5
            return round(0.5 * h * (cls.sides()[0] + cls.sides()[1]), 1)


tr2 = Trapeze(10, 10, 10, 30, 30, 0, 30, 40)
print('\n', 'EASY_Задание-2')
if tr2.is_trap() == False:
    print('четырехугольник не является трапецией')
else:
    print('пересечение отрезков =', tr2.intersection())
    print('это трапеция?', tr2.is_trap(), tr2.base_trapeza())
    print('стороны трапеции =', tr2.sides())
    print('периметр трапеции =', tr2.perimeter())
    print('площадь трапеции =', tr2.square())
