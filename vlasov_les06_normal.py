import copy
import math
import random
import re
import os
import shutil
import sys

# NORMAL ______________________________________________________________
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")учебные классы
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Student:
    def __init__(self, name, surname, class_room, mother, father):
        self.name = name
        self.surname = surname
        self.class_room = class_room
        self.mother = mother
        self.father = father

    def full_name(self):
        full_name = self.name + ' ' + self.surname[0] + '.'
        return full_name

    def get_class(self):
        return self.class_room

    def get_parents(self):
        return [self.mother, self.father]


class Teacher:
    def __init__(self, name, surname, subject, classes):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.classes = classes

    def full_name(self):
        full_name = self.name + ' ' + self.surname[0] + '.'
        return full_name


class School:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers

    def get_classes(self):
        class_list = set([student_cur.get_class() for student_cur in self.students])
        return class_list

    def get_students(self, class_request):
        students_list = [student_cur.full_name() for student_cur in self.students
                         if student_cur.get_class() == class_request]
        return students_list

    def get_student_parents(self, student_request):
        students_parents = [student_cur.get_parents() for student_cur in self.students
                            if student_cur.full_name() == student_request]
        return students_parents

    def get_subjects(self, student_request):
        class_num = [student_cur.get_class() for student_cur in self.students if student_cur.full_name() == student_request]
        subjects_list = [teacher_cur.subject for teacher_cur in self.teachers if class_num[0] in teacher_cur.classes]
        return subjects_list

    def get_class_teachers(self, class_request):
        teachers_list = [teacher_cur.full_name() for teacher_cur in self.teachers if class_request in teacher_cur.classes]
        return teachers_list


students = [Student("Иванов", "Иван", "5А", "Иванов И.А", "Иванова А.Б."),
            Student("Петров", "Петр", "10А", "Петров П.Б", "Петрова В.Г"),
            Student("Сидоров", "Сидор", "11А", "Сидоров С.В", "Сидорова Д.Е"),
            Student("Попов", "Денис", "5А", "Попов Д.Г", "Попова Ж.И"),
            Student("Кузнецов", "Олег", "10А", "Кузнецов О.Д", "Кузнецова К.Л")
            ]

teachers = [Teacher('Машковская', 'Татьяна Николаевна', 'Высшая математика', ['10А', '11A']),
            Teacher('Сербин', 'Александр Иванович', 'История', ['5А', '10А', '11А']),
            Teacher('Слободина', 'Анна Яковлевна', 'Русский Язык', ['5А', '10А', '11А']),
            Teacher('Макарова', 'Инна Николаевна', 'Литература', ['5А', '10А', '11А']),
            Teacher('Вежновец', 'Наталья Николаевна', 'Алгебра', ['5А'])
            ]


school_149 = School(students, teachers)
print('Список задач:')
print('1 - Список классов школы №149')
print('2 - Список учеников в указанном классе')
print('3 - Список предметов указанного ученика')
print('4 - ФИО родителей указанного ученика')
print('5 - Список всех учителей, преподающих в указанном классе')
print('6 - Завершить работу')

while True:
    menu = input("Выберите задачу - ")
    if menu == '1':
        print('Список классов школы №149 -', school_149.get_classes())
    elif menu == '2':
        class_number = input("Укажите класс - ")
        print('Список учеников в классе', class_number, '-', school_149.get_students(class_number))
    elif menu == '3':
        student_name = input("Укажите ученика (Фамилия И.О.) - ")
        print('Список предметов ученика', student_name, '-', school_149.get_subjects(student_name))
    elif menu == '4':
        student_name = input("Укажите ученика (Фамилия И.О.) - ")
        print('ФИО родителей ученика', student_name, '-', school_149.get_student_parents(student_name))
    elif menu == '5':
        class_number = input("Укажите класс - ")
        print('Список всех учителей, преподающих в классе', class_number, '-', school_149.get_class_teachers(class_number))
    elif menu == '6':
        break
