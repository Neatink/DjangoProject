from django.db import models
import django
import os

# Налаштування Django для роботи поза середовищем сервера
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testORM.settings')
django.setup()

from album.models import Subject, Teacher, Class, Student

def add_subject():
    name = input("name: ")
    count_teachers = input("count_teachers: ")
    subject = Subject(name=name, count_teachers=count_teachers)
    subject.save()
    print("Предмет додано")


def add_teacher():
    name = input("name: ")
    surname = input("surname: ")
    subject_name = input("subject(можна пропустити): ")
    if subject_name:
        subject = Subject.objects.filter(name=subject_name).get()
    else:
        subject = None
    subjects_count = input("subjects_count: ")
    teacher = Teacher(name=name, surname=surname, subject=subject, subjects_count=subjects_count)
    teacher.save()
    print("Вчителя додано")

def add_class():
    name = input("name: ")
    clas = Class(name=name)
    clas.save()
    print("Клас додан")

def add_student():
    name = input("name: ")
    surname = input("surname: ")
    mail = input("mail: ")
    clas = input("clas: ")
    try:
        clas_get = Class.objects.get(name=clas)
    except:
        print("Напиши правильну назву класа(наприклад 10-A)")
        return
    birthday = input("birthday(РIК-МIСЯЦЬ-ДЕНЬ): ")
    student = Student(name=name, surname=surname, clas = clas_get, mail=mail, birthday=birthday)
    student.save()
    print("Учень додан")

while True:
    a = input("Що додати?\n(1-Subject, 2-Teacher, 3-Class, 4-Student): ")
    if a == "1":
        add_subject()
    elif a == "2":
        add_teacher()
    elif a == "3":
        add_class()
    elif a == "4":
        add_student()